# Activity Mapping Universitas Diponegoro

🌐 **Demo Website**  
https://naylamaulidina.pythonanywhere.com

📂 **Repository GitHub**  
https://github.com/Naylamaulidina/activity-mapping-undip

---

## 📝 Deskripsi Singkat

**Activity Mapping UNDIP** adalah aplikasi web GIS berbasis Python Flask yang menampilkan:
- **Peta interaktif** menggunakan Folium dan OpenStreetMap
- **Heatmap keramaian** dengan 3 tingkat kategori (Hijau/Sepi, Oranye/Sedang, Merah/Ramai)
- **Marker lokasi** untuk 14 titik penting di UNDIP Tembalang
- **Data simulasi stabil** yang berubah setiap halaman di-refresh dengan variasi realistis
- **Popup informasi** pada setiap marker dengan detail keramaian

### Tujuan
Memberikan visualisasi keramaian di berbagai lokasi UNDIP secara semi-realtime untuk keperluan analisis geodesi dan urban mapping.

---

## Fitur Utama

### 🗺️ Peta Interaktif Kampus
- Menampilkan peta kampus berbasis OpenStreetMap.
- Menampilkan titik-titik lokasi penting di Universitas Diponegoro.
- Informasi lokasi dapat diakses langsung melalui marker pada peta.

### 🔥 Heatmap Keramaian
- Visualisasi persebaran tingkat keramaian kampus.
- Warna heatmap menunjukkan intensitas aktivitas pada suatu lokasi.

### 📢 Crowdsourcing Laporan
- Pengguna dapat mengirim laporan kondisi area secara langsung.
- Data laporan digunakan untuk memperbarui kondisi keramaian pada peta.

### 📸 Upload Foto
- Pengguna dapat menyertakan foto kondisi area saat melakukan pelaporan.
- Membantu meningkatkan validitas laporan yang diberikan.

### ⏳ Time Decay
- Laporan lama secara otomatis memiliki pengaruh yang semakin kecil.
- Sistem lebih memprioritaskan laporan terbaru.

### 📍 Haversine Distance
- Digunakan untuk menghitung jarak pengguna terhadap lokasi yang dilaporkan.
- Membantu validasi lokasi pelaporan.

### 📊 Statistik Aktivitas
- Menampilkan informasi jumlah laporan.
- Menampilkan kondisi aktivitas kampus secara ringkas.

### 👨‍💼 Halaman Admin
- Digunakan untuk memantau laporan yang masuk.
- Memudahkan proses pengelolaan data laporan.

---
## Teknologi yang Digunakan

| Komponen | Teknologi |
|-----------|-----------|
| Backend | Python |
| Framework | Flask |
| Frontend | HTML, CSS, JavaScript |
| Pemetaan | Folium |
| Basemap | OpenStreetMap |
| Pengolahan Data | Pandas |
| Penyimpanan Data | CSV |
| Deployment | PythonAnywhere |

## 🛠️ Persyaratan Sistem

### Requirement Software
- **Python** 3.8 atau lebih baru
- **pip** (package manager Python)
- **VS Code** atau text editor lainnya (opsional)
- **Browser modern** (Chrome, Firefox, Safari, Edge)

### Requirement Hardware
- RAM minimal 2 GB
- Koneksi internet untuk akses OpenStreetMap (saat pertama kali load)
- Port 5000 tersedia (default Flask)

---

## 📁 Struktur Folder

```
activity-mapping-undip/
│
├── app.py                      # File utama aplikasi Flask
├── requirements.txt            # Daftar library Python yang dibutuhkan
├── README.md                   # Dokumentasi ini
│
├── templates/
│   └── index.html             # Template HTML untuk halaman utama
│
└── static/                     # Folder untuk asset statis (CSS, JS custom, dll)
    └── (folder untuk future use)
```

---
## Instalasi dan Setup

### 1. Clone Repository

```bash
git clone https://github.com/Naylamaulidina/activity-mapping-undip.git
cd activity-mapping-undip
```

### 2. Buat Virtual Environment (Opsional)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependency

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

### 5. Akses Melalui Browser

```text
http://localhost:5000
```

---

## Deployment

Aplikasi telah berhasil dideploy menggunakan PythonAnywhere dan dapat diakses melalui:

https://naylamaulidina.pythonanywhere.com

Deployment dilakukan dengan langkah berikut:

1. Clone repository GitHub ke PythonAnywhere.
2. Install seluruh dependency dari `requirements.txt`.
3. Konfigurasi WSGI agar mengarah ke file `app.py`.
4. Reload web application melalui dashboard PythonAnywhere.
5. Aplikasi dapat diakses secara online melalui domain PythonAnywhere.

---

## Dependencies

Dependency utama yang digunakan pada proyek ini:

| Library | Fungsi |
|----------|----------|
| Flask | Framework backend web |
| Folium | Visualisasi peta interaktif |
| Pandas | Pengolahan data laporan |
| Jinja2 | Template engine Flask |
| Werkzeug | Utilitas web Flask |
| Gunicorn | Web server deployment |

---

## 🔧 Cara Kerja Sistem

### Alur Kerja Aplikasi

```
User buka http://localhost:5000
           ↓
   Flask route / (index) dipanggil
           ↓
  Fungsi create_map() di-eksekusi
           ↓
   Loop semua 14 lokasi UNDIP
           ↓
   Setiap lokasi:
   - Generate random crowd_value (0-20)
   - Tentukan status (Sepi/Sedang/Ramai)
   - Tentukan warna (Hijau/Oranye/Merah)
   - Buat marker di peta
   - Tambahkan ke heatmap data
           ↓
   Render peta Folium ke HTML
           ↓
   Pass HTML ke template index.html
           ↓
   Browser menerima halaman HTML
           ↓
   Peta interaktif ditampilkan di browser
```

### Komponen Utama

#### 1. **app.py** - Backend Flask
- Mendefinisikan 14 lokasi UNDIP dengan koordinat GPS
- Generate data keramaian random per lokasi
- Membuat peta Folium dengan semua visualization
- Serve HTML ke browser

#### 2. **index.html** - Template Frontend
- Struktur HTML halaman
- Styling CSS untuk UI yang modern
- JavaScript untuk menampilkan timestamp
- Menampilkan peta yang di-generate dari Flask

#### 3. **Folium Library**
- Membuat peta interaktif berbasis OpenStreetMap
- Rendering circle markers untuk setiap lokasi
- Rendering heatmap layer dengan color gradient
- Membuat legend dan title pada peta

---

## 📊 Penjelasan Logika

### Logika Keramaian

Setiap lokasi memiliki nilai keramaian (0-20) yang di-generate secara random:

```
Crowd Value        Status    Warna    Display
0 - 5        →     Sepi      Hijau    🟢
6 - 15       →     Sedang    Oranye   🟠
16 - 20      →     Ramai     Merah    🔴
```

### Proses Generate Data

1. **Fungsi `get_crowd_level()`**
   - Generate random integer antara 0-20
   - Setiap lokasi mendapat nilai berbeda
   - Perubahan per refresh (tidak saved)

2. **Fungsi `get_crowd_status(crowd_value)`**
   - Input: nilai keramaian
   - Output: dictionary dengan status, warna, text
   - Digunakan untuk display di marker dan heatmap

### Kenapa Simulasi Stabil?

- **Range terbatas (0-20)**: Variasi realistis, tidak ekstrem
- **Setiap lokasi random**: Tidak semua lokasi ramai/sepi bersamaan
- **No auto-update**: Hanya berubah saat manual refresh
- **Smooth transition**: Range kecil membuat perubahan gradual

### Heatmap Visualization

Folium `HeatMap` layer:
- Input: list `[lat, lon, intensity]` untuk setiap lokasi
- Intensity: `crowd_value / 20.0` (normalize ke 0-1)
- Gradient color: 0.2 (hijau) → 0.5 (oranye) → 1.0 (merah)
- Radius: 25px untuk spreading yang natural
- Blur: 15px untuk smooth edges

---

## 📍 Data Lokasi UNDIP

lokasi yang di-monitor:

| Nama Lokasi | Latitude | Longitude |
|:-----------|:--------:|:---------:|
| Lokasi | Latitude | Longitude |
|---------|---------|---------|
| Perpustakaan Widya Puraya | -7.0516 | 110.4381 |
| Gedung Fakultas Ilmu Budaya | -7.0520 | 110.4375 |
| Gedung Fakultas Hukum | -7.0535 | 110.4387 |
| Gedung Sekolah Vokasi | -7.0530 | 110.4355 |
| Gedung Fakultas Ilmu Sosial dan Ilmu Politik | -7.0528 | 110.4370 |
| Gedung Teknik Arsitektur | -7.0517 | 110.4400 |
| Gedung Pertamina Teknik Geologi | -7.0499 | 110.4409 |
| Gedung Prof Soedarto | -7.0502 | 110.4420 |
| Gedung Fakultas Peternakan dan Pertanian | -7.0483 | 110.4421 |
| Gedung Teknik Kimia | -7.0508 | 110.4418 |
| Gedung Teknik Industri | -7.0504 | 110.4428 |
| Dekanat Fakultas Teknik | -7.0505 | 110.4412 |
| Gedung Kuliah Teknik Mesin | -7.0500 | 110.4422 |
| Gedung Jurusan Biologi | -7.0495 | 110.4430 |
| Gedung Dekanat FMIPA | -7.0490 | 110.4425 |
| Gedung Laboratorium Geofisika | -7.0487 | 110.4435 |
| Gedung Fakultas Kesehatan Masyarakat | -7.0485 | 110.4442 |
| Gedung E FPIK | -7.0492 | 110.4448 |
| Gedung F FPIK | -7.0495 | 110.4450 |
| Gedung C FPIK | -7.0490 | 110.4455 |
| Gedung D FPIK | -7.0493 | 110.4457 |
| Gedung Departemen Ilmu Keperawatan | -7.0479 | 110.4440 |
| Gedung Fakultas Teknologi Pangan | -7.0481 | 110.4432 |
| Gedung ICT Centre | -7.0510 | 110.4398 |
| Gedung Fakultas Psikologi | -7.0540 | 110.4401 |
| Gedung Departemen Ilmu Gizi | -7.0476 | 110.4435 |
| Gedung A Fakultas Kedokteran | -7.0473 | 110.4445 |
| Kantin FPIK | -7.0498 | 110.4443 |
| Gedung Teknik Geodesi | -7.0507 | 110.4400 |
| Gedung Teknik Sipil | -7.0512 | 110.4415 |
| Gedung Teknik Mesin | -7.0500 | 110.4420 |
| Gedung Teknik Lingkungan | -7.0509 | 110.4410 |
| Laboratorium Terintegrasi Fakultas Teknik | -7.0503 | 110.4407 |
| Bus Stop Campus | -7.0497 | 110.4449 |

---

## 🐛 Troubleshooting

### Error: "Port 5000 already in use"
**Solusi:**
```bash
# Gunakan port berbeda
# Edit app.py, baris terakhir:
app.run(debug=True, host='127.0.0.1', port=5001)  # Ganti 5000 ke 5001

# Atau stop aplikasi lain yang pakai port 5000
```

### Error: "Module not found: flask/folium"
**Solusi:**
```bash
# Pastikan virtual environment sudah aktif
# Reinstall dependencies
pip install -r requirements.txt

# Atau install manual
pip install Flask==2.3.3 folium==0.14.0
```

### Peta tidak muncul di browser
**Solusi:**
1. Cek apakah server masih running (lihat terminal Flask)
2. Refresh browser (F5)
3. Clear browser cache (Ctrl+Shift+Delete)
4. Buka developer tools (F12) untuk melihat error messages

### Server error "Address already in use"
**Solusi:**
```bash
# Windows (PowerShell):
Get-Process -Port 5000
Stop-Process -Id <PID> -Force

# Atau gunakan port berbeda seperti di atas
```

### Heatmap atau marker tidak terlihat
**Solusi:**
1. Pastikan zoom level cukup (minimal 15)
2. Cek bahwa data lokasi sudah di-load (lihat console browser F12)
3. Refresh halaman
4. Cek network tab di developer tools untuk error fetch

---

## 💡 Tips Pengembangan Lebih Lanjut

### Untuk menambah lokasi baru:
Edit `app.py`, dalam dictionary `LOCATIONS`:
```python
LOCATIONS = {
    'Nama Lokasi Baru': {'lat': -7.xxxx, 'lon': 110.xxxx},
    ...
}
```

### Untuk mengubah warna:
Edit di fungsi `get_crowd_status()`:
```python
# Ubah threshold
if crowd_value <= 10:  # Contoh: ubah dari 5 menjadi 10
    return {'status': 'Sepi', 'color': 'green', ...}
```

### Untuk menggunakan data real:
Replace `get_crowd_level()` dengan:
```python
# Query dari API GPS real atau database
# Contoh: fetch dari sensor IoT, mobile GPS tracking, dll
```

### Untuk menambah feature:
- Grafikhistory keramaian per lokasi
- Export data ke CSV
- Real-time update dengan WebSocket
- Weather integration
- Traffic data integration

---

## 📚 Referensi Library

- **Flask** https://flask.palletsprojects.com/
- **Folium** https://python-visualization.github.io/folium/
- **OpenStreetMap** https://www.openstreetmap.org/
- **Leaflet JS** https://leafletjs.com/ (backend Folium)

---

## 📧 Support

Jika ada pertanyaan atau error:
1. Cek console browser (F12)
2. Cek terminal Flask untuk error logs
3. Baca dokumentasi library (link di atas)
4. Cek syntax Python dengan VS Code

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan Teknik Geodesi UNDIP.

---

**Dibuat dengan ❤️ untuk Universitas Diponegoro**

Terakhir diupdate: Mei 2026

