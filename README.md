# 🗺️ Activity Mapping UNDIP - Aplikasi Web GIS

Aplikasi web untuk visualisasi peta keramaian di berbagai lokasi Universitas Diponegoro Tembalang secara semi-realtime.

## 📋 Daftar Isi
1. [Deskripsi Singkat](#deskripsi-singkat)
2. [Fitur Utama](#fitur-utama)
3. [Persyaratan Sistem](#persyaratan-sistem)
4. [Struktur Folder](#struktur-folder)
5. [Instalasi & Setup](#instalasi--setup)
6. [Cara Menjalankan](#cara-menjalankan)
7. [Cara Kerja Sistem](#cara-kerja-sistem)
8. [Penjelasan Logika](#penjelasan-logika)
9. [Troubleshooting](#troubleshooting)

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

## ✨ Fitur Utama

✅ **Peta Interaktif**
- Zoom dan pan untuk eksplorasi area
- Basemap OpenStreetMap yang akurat
- Center otomatis ke area UNDIP Tembalang

✅ **Heatmap Keramaian**
- Gradient warna: Hijau (Sepi) → Oranye (Sedang) → Merah (Ramai)
- Heat layer yang smooth dan mudah dibaca
- Update saat halaman di-refresh

✅ **14 Lokasi Penting UNDIP**
- Marker dengan circle yang berwarna sesuai keramaian
- Popup berisi: nama lokasi, koordinat GPS, nilai keramaian, status
- Tooltip untuk preview nama lokasi saat hover

✅ **Data Simulasi Stabil**
- Random integer (0-20) per lokasi per refresh
- Transisi realistis tanpa perubahan ekstrem
- Tidak ada update otomatis per detik (sesuai spesifikasi)

✅ **UI Modern & Bersih**
- Header gradient dengan informasi aplikasi
- Legend yang jelas dan mudah dipahami
- Info banner untuk penjelasan data simulasi
- Footer dengan timestamp update terakhir

✅ **API Endpoint**
- `/api/locations` untuk mendapatkan data dalam format JSON

---

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

## 🚀 Instalasi & Setup

### Step 1: Buka Folder Project di VS Code

1. Buka **VS Code**
2. Klik **File → Open Folder** (atau `Ctrl+K Ctrl+O`)
3. Pilih folder: `activity-mapping-undip`
4. Klik **Select Folder**

### Step 2: Buka Terminal di VS Code

Klik **Terminal → New Terminal** (atau `Ctrl+` pada keyboard)

Terminal akan terbuka di bagian bawah VS Code.

### Step 3: Buat Virtual Environment (Opsional tapi Recommended)

Virtual environment memisahkan dependencies project ini dari system Python.

**Windows (PowerShell):**
```powershell
# Buat virtual environment
python -m venv venv

# Aktivasi virtual environment
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Setelah aktivasi, prompt terminal akan berubah menjadi `(venv)`.

### Step 4: Install Library Dependencies

```bash
pip install -r requirements.txt
```

Library yang akan di-install:
- **Flask** 2.3.3 - Web framework
- **Folium** 0.14.0 - Library untuk membuat peta interaktif
- **Jinja2** 3.1.2 - Template engine
- **Werkzeug** 2.3.7 - WSGI utility library

### Step 5: Verifikasi Instalasi (Opsional)

Untuk memastikan library sudah terinstall dengan benar:

```bash
pip list
```

Anda akan melihat list semua library yang terinstall termasuk Flask dan Folium.

---

## ▶️ Cara Menjalankan

### 1. Pastikan di dalam folder project

```bash
# Di terminal, check current directory
# Harus menunjukkan: activity-mapping-undip atau C:\...\activity-mapping-undip
```

### 2. Jalankan aplikasi Flask

```bash
python app.py
```

### 3. Output Terminal Akan Menampilkan

```
============================================================
🚀 Activity Mapping UNDIP - Flask Application
============================================================
✅ Server sedang berjalan di: http://localhost:5000
📍 Buka URL tersebut di browser Anda
🔄 Tekan Ctrl+C untuk menghentikan server
============================================================
```

### 4. Buka Browser

Buka browser Anda (Chrome, Firefox, dll) dan navigasi ke:
```
http://localhost:5000
```

Atau klik link yang muncul di terminal dengan `Ctrl+Click` (Windows) atau `Cmd+Click` (Mac).

### 5. Explore Aplikasi

- **Zoom & Pan**: Gunakan mouse untuk zoom in/out dan geser peta
- **Lihat Marker**: Klik marker untuk melihat popup dengan informasi keramaian
- **Hover Marker**: Arahkan mouse ke marker untuk melihat tooltip nama lokasi
- **Lihat Legend**: Legend tersedia di kanan bawah peta

### 6. Refresh Data

Untuk mendapatkan data keramaian baru (simulasi berubah):
- Tekan **F5** atau **Ctrl+R** pada browser
- Atau klik tombol **Refresh** browser

### 7. Hentikan Server

Di terminal, tekan **Ctrl+C** untuk menghentikan Flask server:
```
^C
```

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

14 lokasi yang di-monitor:

| No | Nama Lokasi | Latitude | Longitude |
|:--:|:-----------|:--------:|:---------:|
| 1 | Universitas Diponegoro | -7.0507 | 110.4399 |
| 2 | Perpustakaan UNDIP | -7.0516 | 110.4381 |
| 3 | Muladi Dome | -7.0510 | 110.4406 |
| 4 | Rektorat UNDIP | -7.0516 | 110.4395 |
| 5 | Fakultas Teknik | -7.0507 | 110.4409 |
| 6 | Fakultas Hukum | -7.0535 | 110.4387 |
| 7 | Fakultas Ekonomika & Bisnis | -7.0547 | 110.4377 |
| 8 | FISIP | -7.0530 | 110.4369 |
| 9 | Fakultas Psikologi | -7.0540 | 110.4401 |
| 10 | Fakultas Kedokteran | -7.0488 | 110.4426 |
| 11 | FSM | -7.0498 | 110.4384 |
| 12 | FKM | -7.0519 | 110.4360 |
| 13 | FPP | -7.0475 | 110.4392 |
| 14 | FPIK | -7.0482 | 110.4413 |

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

