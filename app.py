"""
Activity Mapping Universitas Diponegoro
WEB GIS ACTIVITY MAPPING UNDIP
Menggunakan Flask, Folium, Pandas, dan OpenStreetMap

Fitur baru: crowdsourcing laporan keramaian pengguna, Time Decay, Haversine Distance, & Layer Filtering.
"""

from flask import Flask, render_template, jsonify, request, redirect, url_for, send_from_directory, session
import folium
from folium import plugins
import pandas as pd
import os
import random
from datetime import datetime, timedelta
import math
import json

# Inisialisasi aplikasi Flask
app = Flask(__name__)
app.secret_key = 'rahasia_webgis_undip_2026'

# Path file laporan CSV dan upload foto
CSV_PATH = os.path.join(os.path.dirname(__file__), 'laporan.csv')
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
CSV_COLUMNS = ['timestamp', 'nama', 'lokasi', 'tingkat_keramaian', 'foto']

# ============================================
# DATA LOKASI
# ============================================
LOCATIONS = {
    "Perpustakaan Widya Puraya": {'lat': -7.0516, 'lon': 110.4381},
    "Gedung Fakultas Ilmu Budaya": {'lat': -7.0520, 'lon': 110.4375},
    "Gedung Fakultas Hukum": {'lat': -7.0535, 'lon': 110.4387},
    "Gedung Sekolah Vokasi": {'lat': -7.0530, 'lon': 110.4355},
    "Gedung Fakultas Ilmu Sosial dan Ilmu Politik": {'lat': -7.0528, 'lon': 110.4370},
    "Gedung Teknik Arsitektur": {'lat': -7.0517, 'lon': 110.4400},
    "Gedung Pertamina Teknik Geologi": {'lat': -7.0499, 'lon': 110.4409},
    "Gedung Prof Soedarto": {'lat': -7.0502, 'lon': 110.4420},
    "Gedung Fakultas Peternakan dan Pertanian": {'lat': -7.0483, 'lon': 110.4421},
    "Gedung Teknik Kimia": {'lat': -7.0508, 'lon': 110.4418},
    "Gedung Teknik Industri": {'lat': -7.0504, 'lon': 110.4428},
    "Dekanat Fakultas Teknik": {'lat': -7.0505, 'lon': 110.4412},
    "Gedung Kuliah Teknik Mesin": {'lat': -7.0500, 'lon': 110.4422},
    "Gedung Jurusan Biologi": {'lat': -7.0495, 'lon': 110.4430},
    "Gedung Dekanat FMIPA": {'lat': -7.0490, 'lon': 110.4425},
    "Gedung Laboratorium Geofisika": {'lat': -7.0487, 'lon': 110.4435},
    "Gedung Fakultas Kesehatan Masyarakat": {'lat': -7.0485, 'lon': 110.4442},
    "Gedung E FPIK": {'lat': -7.0492, 'lon': 110.4448},
    "Gedung F FPIK": {'lat': -7.0495, 'lon': 110.4450},
    "Gedung C FPIK": {'lat': -7.0490, 'lon': 110.4455},
    "Gedung D FPIK": {'lat': -7.0493, 'lon': 110.4457},
    "Gedung Departemen Ilmu Keperawatan": {'lat': -7.0479, 'lon': 110.4440},
    "Gedung Fakultas Teknologi Pangan": {'lat': -7.0481, 'lon': 110.4432},
    "Gedung ICT Centre": {'lat': -7.0510, 'lon': 110.4398},
    "Gedung Fakultas Psikologi": {'lat': -7.0540, 'lon': 110.4401},
    "Gedung Departemen Ilmu Gizi": {'lat': -7.0476, 'lon': 110.4435},
    "Gedung A Fakultas Kedokteran": {'lat': -7.0473, 'lon': 110.4445},
    "Kantin FPIK": {'lat': -7.0498, 'lon': 110.4443},
    "Gedung Teknik Geodesi": {'lat': -7.0507, 'lon': 110.4400},
    "Gedung Teknik Sipil": {'lat': -7.0512, 'lon': 110.4415},
    "Gedung Teknik Mesin": {'lat': -7.0500, 'lon': 110.4420},
    "Gedung Teknik Lingkungan": {'lat': -7.0509, 'lon': 110.4410},
    "Laboratorium Terintegrasi Fakultas Teknik": {'lat': -7.0503, 'lon': 110.4407},
    "Bus Stop Campus": {'lat': -7.0497, 'lon': 110.4449},
}

# ============================================
# UTILITIES
# ============================================

def ensure_reports_file():
    if not os.path.exists(CSV_PATH):
        pd.DataFrame(columns=CSV_COLUMNS).to_csv(CSV_PATH, index=False)

def ensure_upload_folder():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

def load_reports():
    """Memuat data laporan dari CSV dan mengembalikan DataFrame."""
    ensure_reports_file()
    try:
        df = pd.read_csv(CSV_PATH)
    except FileNotFoundError:
        df = pd.DataFrame(columns=CSV_COLUMNS)

    for col in CSV_COLUMNS:
        if col not in df.columns:
            df[col] = ''

    return df[CSV_COLUMNS]

def get_active_reports(reports, hours=2):
    """Menyaring laporan yang hanya dibuat dalam rentang X jam terakhir (Time Decay)"""
    if reports.empty:
        return reports
    
    df_filtered = reports.copy()    
    df_filtered['timestamp_dt'] = pd.to_datetime(df_filtered['timestamp'], errors='coerce')
    cutoff_time = datetime.now() - timedelta(hours=hours)
    active_reports = df_filtered[df_filtered['timestamp_dt'] >= cutoff_time].copy()
    active_reports = active_reports.drop(columns=['timestamp_dt'])
    
    return active_reports

def save_report(report_data):
    ensure_upload_folder()
    df = load_reports()
    df = pd.concat([df, pd.DataFrame([report_data])], ignore_index=True)
    df.to_csv(CSV_PATH, index=False)

def compute_stats(reports, active_reports):
    stats = {
        'total_historis': len(reports),
        'total_aktif': len(active_reports),
        'top_location': '-',
        'top_activity': '-'
    }
    
    if reports.empty:
        return stats

    target_df = active_reports if not active_reports.empty else reports
    
    if not target_df[target_df['tingkat_keramaian'] == 'Ramai'].empty:
        stats['top_location'] = target_df[target_df['tingkat_keramaian'] == 'Ramai']['lokasi'].mode().iloc[0]
    else:
        stats['top_location'] = target_df['lokasi'].mode().iloc[0]
        
    if active_reports.empty and not reports.empty:
        stats['top_location'] += " (Tren Historis)"
        
    return stats

def get_report_intensity(level):
    return {'Sepi': 0.2, 'Sedang': 0.55, 'Ramai': 1.0}.get(level, 0.4)

def get_crowd_level():
    return random.randint(0, 20)

def get_crowd_status(crowd_value):
    if crowd_value <= 5:
        return {'status': 'Sepi', 'color': 'green'}
    elif 6 <= crowd_value <= 15:
        return {'status': 'Sedang', 'color': 'orange'}
    else:
        return {'status': 'Ramai', 'color': 'red'}

def get_color_code(color_name):
    color_map = {'green': '#2ecc71', 'orange': '#e67e22', 'red': '#e74c3c'}
    return color_map.get(color_name, '#95a5a6')

def create_map(reports=None):
    """Buat peta Folium dengan marker, heatmap, dan fitur Filter Status (LayerControl)."""
    center_lat, center_lon = -7.0515, 110.4390
    m = folium.Map(location=[center_lat, center_lon], zoom_start=16, tiles='OpenStreetMap')
    
    # 1. Buat Layer Groups (Grup Filter untuk UI)
    fg_sepi = folium.FeatureGroup(name='🟢 Filter Tempat Sepi', show=True)
    fg_sedang = folium.FeatureGroup(name='🟠 Filter Tempat Sedang', show=True)
    fg_ramai = folium.FeatureGroup(name='🔴 Filter Tempat Ramai', show=True)

    heat_sepi, heat_sedang, heat_ramai = [], [], []

    if reports is not None and not reports.empty:
        for _, row in reports.iterrows():
            lokasi = row.get('lokasi')
            level = row.get('tingkat_keramaian')
            lokasi_coords = LOCATIONS.get(lokasi)
            if lokasi_coords is None:
                continue

            intensity = get_report_intensity(level)
            color_map_hex = {'Sepi': '#2ecc71', 'Sedang': '#e67e22', 'Ramai': '#e74c3c'}
            c_hex = color_map_hex.get(level, '#95a5a6')

            popup_html = f"<div style='font-family: Arial; width: 180px;'><h4 style='margin:0 0 4px 0'>{lokasi}</h4><p style='margin:0;font-size:13px;'>Status Laporan: <b>{level}</b></p></div>"
            
            # Buat Marker
            marker = folium.CircleMarker(
                location=[lokasi_coords['lat'], lokasi_coords['lon']],
                radius=7, color=c_hex, fill=True, fillColor=c_hex, fillOpacity=0.9,
                popup=folium.Popup(popup_html, max_width=250), tooltip=lokasi
            )

            # Pisahkan Marker ke dalam grup yang sesuai dengan statusnya
            if level == 'Sepi':
                marker.add_to(fg_sepi)
            elif level == 'Sedang':
                marker.add_to(fg_sedang)
            else:
                marker.add_to(fg_ramai)

            # Buat titik untuk Heatmap
            for _ in range(4):
                lat_j = lokasi_coords['lat'] + random.uniform(-0.00025, 0.00025)
                lon_j = lokasi_coords['lon'] + random.uniform(-0.00025, 0.00025)
                if level == 'Sepi':
                    heat_sepi.append([lat_j, lon_j, intensity])
                elif level == 'Sedang':
                    heat_sedang.append([lat_j, lon_j, intensity])
                else:
                    heat_ramai.append([lat_j, lon_j, intensity])

    else:
        # Data Simulasi (Jika belum ada laporan asli)
        for name, c in LOCATIONS.items():
            lat, lon = c['lat'], c['lon']
            crowd = get_crowd_level()
            status_color = get_crowd_status(crowd)
            status_text = status_color['status']
            color_hex = get_color_code(status_color['color'])

            popup_html = f"""
            <div style='font-family: Arial; width: 220px;'>
                <h4 style='margin:0 0 6px 0'>{name}</h4>
                <p style='margin:0; font-size:13px;'>Koordinat: {lat:.5f}, {lon:.5f}</p>
                <p style='margin:6px 0 0 0; font-size:13px;'><b>Jumlah:</b> {crowd} &nbsp; <b>Status:</b> {status_text}</p>
                <p style='margin:6px 0 0 0; font-size:11px; color:#666;'>Data simulasi — berubah pada refresh</p>
            </div>
            """

            marker = folium.CircleMarker(
                location=[lat, lon], radius=7, color=color_hex, fill=True, fillColor=color_hex, fillOpacity=0.9,
                weight=1, popup=folium.Popup(popup_html, max_width=260), tooltip=name
            )

            intensity = max(0.05, crowd / 20.0)
            num_points = 4 + (crowd // 4)
            points = []
            for _ in range(num_points):
                lat_j = lat + random.uniform(-0.00035, 0.00035)
                lon_j = lon + random.uniform(-0.00035, 0.00035)
                points.append([lat_j, lon_j, intensity])

            if status_text == 'Sepi':
                marker.add_to(fg_sepi)
                heat_sepi.extend(points)
            elif status_text == 'Sedang':
                marker.add_to(fg_sedang)
                heat_sedang.extend(points)
            else:
                marker.add_to(fg_ramai)
                heat_ramai.extend(points)

    # 2. Tambahkan algoritma Heatmap terpisah ke dalam grup masing-masing
    if heat_sepi:
        plugins.HeatMap(heat_sepi, min_opacity=0.4, radius=30, blur=20, max_zoom=18, gradient={0.0: '#2ecc71', 1.0: '#27ae60'}).add_to(fg_sepi)
    if heat_sedang:
        plugins.HeatMap(heat_sedang, min_opacity=0.4, radius=30, blur=20, max_zoom=18, gradient={0.0: '#f1c40f', 1.0: '#e67e22'}).add_to(fg_sedang)
    if heat_ramai:
        plugins.HeatMap(heat_ramai, min_opacity=0.4, radius=30, blur=20, max_zoom=18, gradient={0.0: '#e74c3c', 1.0: '#c0392b'}).add_to(fg_ramai)

    # 3. Gabungkan Layer Groups ke Peta Utama
    fg_sepi.add_to(m)
    fg_sedang.add_to(m)
    fg_ramai.add_to(m)

    # 4. AKTIFKAN FITUR FILTER (LayerControl box)
    folium.LayerControl(position='topright', collapsed=False).add_to(m)

    legend_text = 'Menampilkan laporan pengguna aktif' if reports is not None and not reports.empty else 'Data keramaian masih berupa simulasi'
    legend = f'''
    <div style="position: fixed; bottom: 60px; right: 12px; z-index:9999; background:white; padding:10px; border-radius:6px; box-shadow:0 1px 4px rgba(0,0,0,0.3); width:230px;">
      <b>Legend Keramaian</b><br>
      <div style="margin-top:6px"><span style="display:inline-block;width:14px;height:14px;background:#2ecc71;margin-right:8px;border:1px solid #ccc;"></span>Hijau = Sepi</div>
      <div style="margin-top:6px"><span style="display:inline-block;width:14px;height:14px;background:#e67e22;margin-right:8px;border:1px solid #ccc;"></span>Oranye = Sedang</div>
      <div style="margin-top:6px"><span style="display:inline-block;width:14px;height:14px;background:#e74c3c;margin-right:8px;border:1px solid #ccc;"></span>Merah = Ramai</div>
      <div style="margin-top:8px;font-size:11px;color:#666;">{legend_text}</div>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend))

    detail_text = 'Gunakan menu centang di kanan atas untuk filter tempat'
    title = f'''
    <div style="position: fixed; top: 12px; left: 12px; z-index:9999; background: rgba(255,255,255,0.95); padding:10px 14px; border-radius:6px; box-shadow:0 1px 4px rgba(0,0,0,0.2); max-width:320px;">
      <div style="font-weight:bold; font-size:16px;">WEB GIS ACTIVITY MAPPING UNDIP</div>
      <div style="font-size:12px; color:#555;">{detail_text}</div>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(title))

    return m._repr_html_()

def hitung_jarak(lat1, lon1, lat2, lon2):
    R = 6371000  # Radius bumi dalam meter
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

@app.route('/')
def index():
    reports = load_reports()
    active_reports = get_active_reports(reports, hours=2)
    stats = compute_stats(reports, active_reports)
    map_html = create_map(active_reports)
    return render_template('index.html', map_html=map_html, stats=stats)

@app.route('/laporkan', methods=['GET', 'POST'])
def laporkan():
    locations = sorted(LOCATIONS.keys())
    success = False
    error = None
    reports = load_reports()
    MAX_JARAK_METER = 50

    if request.method == 'POST':
        nama = request.form.get('nama', '').strip()
        lokasi = request.form.get('lokasi', '').strip()
        tingkat_keramaian = request.form.get('tingkat_keramaian', '').strip()
        user_lat = request.form.get('user_lat')
        user_lon = request.form.get('user_lon')
        foto_file = request.files.get('foto')

        if not lokasi or not tingkat_keramaian or not foto_file or foto_file.filename == '':
            error = 'Silakan isi semua kolom wajib dan unggah foto area.'
        elif not allowed_file(foto_file.filename):
            error = 'Foto harus berformat JPG, JPEG, atau PNG.'
        elif not user_lat or not user_lon:
            error = 'Gagal mendapatkan lokasi Anda. Pastikan izin GPS browser diaktifkan!'
        else:
            target = LOCATIONS.get(lokasi)
            jarak = hitung_jarak(float(user_lat), float(user_lon), target['lat'], target['lon'])
            
            if jarak > MAX_JARAK_METER:
                error = f'Laporan ditolak! Anda berada {int(jarak)} meter dari {lokasi}. Jarak maksimal adalah {MAX_JARAK_METER} meter.'
            else:
                timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
                ext = foto_file.filename.rsplit('.', 1)[1].lower()
                filename = f'foto_{timestamp_str}.{ext}'
                ensure_upload_folder()
                foto_path = os.path.join(UPLOAD_FOLDER, filename)
                foto_file.save(foto_path)
                relative_path = os.path.join('uploads', filename).replace('\\', '/')

                save_report({
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'nama': nama,
                    'lokasi': lokasi,
                    'tingkat_keramaian': tingkat_keramaian,
                    'foto': relative_path,
                })
                success = True
                reports = load_reports()

    report_records = reports.to_dict(orient='records')
    
    return render_template(
        'report.html', 
        locations=locations, 
        locations_json=json.dumps(LOCATIONS),
        success=success, 
        error=error, 
        reports=report_records
    )

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/api/locations')
def api_locations():
    locations = []
    for name, c in LOCATIONS.items():
        crowd = get_crowd_level()
        status = get_crowd_status(crowd)
        locations.append({
            'name': name,
            'latitude': c['lat'],
            'longitude': c['lon'],
            'crowd_value': crowd,
            'crowd_status': status['status'],
            'crowd_color': status['color'],
        })

    return jsonify({'timestamp': datetime.now().isoformat(), 'locations': locations})

# ============================================
# FITUR ADMIN (NON-CLIENT)
# ============================================
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')
        # Ganti 'admin123' dengan password rahasia yang Anda inginkan
        if password == 'admin123': 
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            error = 'Password salah! Akses ditolak.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None) # Hapus sesi login
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    # Cek apakah user sudah login, jika belum lempar ke halaman login
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    reports = load_reports()
    
    # Menambahkan ID (berdasarkan nomor baris) agar kita tahu data mana yang dihapus
    reports['id'] = reports.index
    report_records = reports.to_dict(orient='records')
    
    return render_template('admin.html', reports=report_records)

@app.route('/hapus_laporan/<int:report_id>', methods=['POST'])
def hapus_laporan(report_id):
    # Proteksi: hanya admin yang login yang bisa menghapus
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    df = load_reports()
    
    if report_id in df.index:
        # Opsional: Hapus file fotonya juga dari folder uploads agar memori laptop/server tidak penuh
        foto_path = df.at[report_id, 'foto']
        if pd.notna(foto_path) and foto_path != '':
            full_path = os.path.join(app.root_path, str(foto_path))
            if os.path.exists(full_path):
                try:
                    os.remove(full_path)
                except Exception as e:
                    print(f"Gagal menghapus foto: {e}")
        
        # Hapus baris data dari tabel, lalu simpan ulang CSV-nya
        df = df.drop(report_id)
        df.to_csv(CSV_PATH, index=False)
        
    return redirect(url_for('admin'))

if __name__ == '__main__':
    print('Starting WEB GIS Activity Mapping UNDIP on http://localhost:5000')
    app.run(debug=True, host='127.0.0.1', port=5000)