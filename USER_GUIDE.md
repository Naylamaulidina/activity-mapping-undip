# 📖 USER GUIDE - Activity Mapping UNDIP

Panduan lengkap cara menggunakan aplikasi Activity Mapping UNDIP.

## 🎯 Tujuan Aplikasi

Activity Mapping UNDIP adalah aplikasi web GIS yang menampilkan peta interaktif keramaian di berbagai lokasi Universitas Diponegoro Tembalang. Aplikasi ini dirancang untuk:

- 📊 **Visualisasi Keramaian**: Melihat pola keramaian di berbagai lokasi UNDIP
- 🗺️ **Peta Interaktif**: Eksplorasi lokasi dengan zoom, pan, dan filtering
- 📍 **Informasi Lokasi**: Detail lengkap setiap lokasi via popup marker
- 🔄 **Update Semi-Realtime**: Data keramaian berubah saat refresh
- 💡 **Alat Pembelajaran**: Untuk studi Teknik Geodesi, GIS, dan Urban Mapping

---

## 🚀 Quick Start (5 Menit)

### Opsi 1: Automatic Setup (Windows - Recommended)

1. **Buka PowerShell di folder project**
   - Klik folder project
   - Shift+Right-click → "Open PowerShell here"

2. **Jalankan setup script**
   ```powershell
   .\setup.bat
   ```
   - Script otomatis akan:
     - Check Python installation
     - Buat virtual environment
     - Install dependencies
     - Tampilkan instruksi selanjutnya

3. **Jalankan aplikasi**
   ```
   python app.py
   ```

4. **Buka browser**
   ```
   http://localhost:5000
   ```

### Opsi 2: Manual Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# 3. Install packages
pip install -r requirements.txt

# 4. Run app
python app.py

# 5. Open browser
# http://localhost:5000
```

### Opsi 3: Menggunakan VS Code Terminal

1. Buka folder di VS Code
2. Buka terminal (Ctrl+`)
3. Copy-paste perintah dari Opsi 2

---

## 🗺️ Cara Menggunakan Peta

### 1. Navigasi Peta

| Aksi | Cara |
|------|------|
| **Zoom In** | Scroll mouse ↑ atau Double-click |
| **Zoom Out** | Scroll mouse ↓ |
| **Pan/Geser** | Click & drag peta |
| **Full Screen** | Klik tombol fullscreen (top-right) |
| **Reset View** | Refresh halaman (F5) |

### 2. Interaksi Marker

**Hover (Arahkan mouse)**
```
├─ Marker berubah jadi lebih terang
└─ Tooltip muncul = nama lokasi
```

**Klik Marker**
```
├─ Popup muncul berisi:
│  ├─ Nama lokasi
│  ├─ Koordinat GPS (Lat/Lon)
│  ├─ Nilai keramaian (0-20)
│  └─ Status (Sepi/Sedang/Ramai)
└─ Klik di luar popup untuk tutup
```

### 3. Baca Heatmap

**Warna Heatmap:**
- 🟢 **Hijau** = Sepi (keramaian 0-5)
- 🟠 **Oranye** = Sedang (keramaian 6-15)
- 🔴 **Merah** = Ramai (keramaian >15)

**Cara Membaca:**
1. Lihat area dengan gradasi warna
2. Warna lebih merah = semakin ramai
3. Warna lebih hijau = semakin sepi
4. Intensity terlihat smooth (tidak abrupt)

### 4. Lihat Legend

Legend terdapat di **kanan bawah** peta:
- Menampilkan 3 kategori keramaian
- Warna reference untuk setiap status
- Info bahwa data masih simulasi

---

## 🔄 Update & Refresh Data

### Setiap kali Refresh:
- Data keramaian **berubah** secara random
- Warna marker **berubah** sesuai keramaian baru
- Heatmap **berubah** intensitasnya
- Judul dan legend **tetap sama**

### Cara Refresh:

| Metode | Shortcut |
|--------|----------|
| Browser Refresh | F5 atau Ctrl+R |
| Hard Refresh | Ctrl+Shift+R |
| Klik Refresh Button | Browser refresh icon |
| Reload di VS Code | Cmd+R (Mac) |

---

## 📊 Memahami Data

### Nilai Keramaian (0-20)

```
Setiap lokasi punya nilai 0-20 yang di-random setiap refresh

Contoh pembacaan:
├─ Nilai 2 → Sepi (Hijau)
├─ Nilai 10 → Sedang (Oranye)
└─ Nilai 18 → Ramai (Merah)
```

### Mengapa Simulasi?

Data keramaian adalah **simulasi** karena:
- Aplikasi baru, belum ada GPS sensor asli
- Fleksibel untuk testing dan development
- Stabil dan ringan untuk localhost
- Cocok untuk pembelajaran GIS

### Stabil tapi Realistic

Random logic:
- Setiap lokasi random value berbeda
- Range 0-20 (variasi realistis)
- Bukan 0-100 (terlalu ekstrem)
- Perubahan smooth (tidak tiba-tiba)

---

## 🔍 Mengeksplorasi Lokasi

### 14 Lokasi UNDIP

Coba explore setiap lokasi:

1. **Pusat Kampus**
   - Universitas Diponegoro (pusat)
   - Rektorat UNDIP (administrative)

2. **Fasilitas Utama**
   - Perpustakaan UNDIP (banyak mahasiswa)
   - Muladi Dome (gathering point)

3. **Fakultas**
   - Fakultas Teknik
   - Fakultas Hukum
   - Fakultas Ekonomika & Bisnis
   - FISIP (Ilmu Sosial)
   - Fakultas Psikologi
   - Fakultas Kedokteran
   - FSM (Sains/Teknik)
   - FKM (Kesehatan Masyarakat)
   - FPP (Pascasarjana)
   - FPIK (Teknologi Kelautan)

### Tips Eksplorasi

1. **Click semua marker** untuk lihat variasi keramaian
2. **Zoom in** ke area spesifik untuk detail lebih
3. **Bandingkan warna** antar lokasi
4. **Refresh** untuk lihat perubahan data
5. **Dokumentasikan** pola yang Anda amati

---

## 🛠️ Troubleshooting Dasar

### Peta tidak muncul

**Kemungkinan:**
- Server tidak running
- Port 5000 sudah dipakai
- Browser cache lama

**Solusi:**
```
1. Check terminal: apakah app.py masih running?
2. Cek browser console (F12) untuk error
3. Refresh halaman (Ctrl+Shift+R)
4. Restart server (Ctrl+C, python app.py)
```

### Marker tidak interactive

**Kemungkinan:**
- Peta belum fully loaded
- JavaScript disabled

**Solusi:**
```
1. Tunggu peta fully load (~3 detik)
2. Refresh halaman
3. Check browser JavaScript setting
```

### Browser error/blank

**Kemungkinan:**
- Python error
- Import library gagal

**Solusi:**
```
1. Lihat terminal error message
2. Check console browser (F12)
3. Reinstall: pip install -r requirements.txt
```

---

## 📱 Multi-Device Support

### Desktop (Recommended)
- ✅ Optimal experience
- ✅ Zoom dan pan smooth
- ✅ Popup besar dan readable
- ✅ Legend dan title jelas

### Laptop
- ✅ Good experience
- ⚠️ Zoom dengan trackpad perlu adjustment
- ✅ Responsive design

### Tablet
- ⚠️ Touch controls untuk zoom/pan
- ⚠️ Popup mungkin kecil
- ℹ️ Belum fully optimized

### Mobile Phone
- ❌ Not recommended
- ℹ️ UI terlalu kecil
- ℹ️ Better akses dari desktop

---

## 💡 Tips & Tricks

### 1. Keyboard Shortcuts
```
F5               → Refresh halaman
F12              → Buka developer tools
Ctrl+Shift+R     → Hard refresh (clear cache)
Esc              → Close popup
```

### 2. Inspeksi dengan Developer Tools

**Buka Developer Tools:**
- F12 atau Ctrl+Shift+I

**Lihat:**
- Console: error messages
- Network: loading performance
- Elements: HTML peta structure

### 3. Bookmark untuk Akses Cepat

Bookmark URL aplikasi:
```
http://localhost:5000
```

Akses cepat setelah server running!

### 4. Zoom ke Lokasi Spesifik

Saat peta di-refresh:
1. Identify lokasi yang menarik
2. Zoom in untuk detail
3. Click marker untuk info popup
4. Refresh untuk lihat perubahan data

---

## 🎓 Pembelajaran Geodesi

### Konsep GIS yang Dipelajari

1. **Koordinat Geographic**
   - Latitude/Longitude
   - DMS vs Decimal format
   - Projection systems

2. **Spatial Data Visualization**
   - Marker representation
   - Heatmap interpolation
   - Color gradient mapping

3. **Basemap & Layers**
   - OpenStreetMap basemap
   - HeatMap layer overlay
   - Marker layer

4. **Interactive Mapping**
   - Zoom & pan (navigation)
   - Click popup (interaction)
   - Hover tooltip (feedback)

### Contoh Studi Kasus

**Analisis Keramaian:**
- Lokasi mana yang paling ramai?
- Lokasi mana yang paling sepi?
- Pola keramaian antar area?
- Hubungan dengan fasilitas?

**Improvement Suggestions:**
- Integrasi dengan real GPS data?
- Tambah weather overlay?
- Tambah event calendar?
- Traffic data integration?

---

## 🔗 Resources

### Dokumentasi
- **README.md** - Setup dan overview
- **QUICKSTART.md** - Quick guide
- **ARCHITECTURE.md** - Technical details
- **config.py** - Konfigurasi detail

### External Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Folium Documentation](https://python-visualization.github.io/folium/)
- [Leaflet Documentation](https://leafletjs.com/)
- [OpenStreetMap Wiki](https://wiki.openstreetmap.org/)

### Offline Help
- Buka README.md untuk help
- Check ARCHITECTURE.md untuk technical details
- Lihat app.py comments untuk code explanation

---

## 📧 Feedback & Improvement

Jika ada saran improvement:
1. Check dokumentasi existing
2. Lihat ARCHITECTURE.md untuk extension points
3. Modify config.py untuk customize behavior
4. Extend app.py untuk new features

---

## ✅ Checklist Penggunaan Awal

- [ ] Setup selesai tanpa error
- [ ] Server running (terminal menampilkan "Running on http://localhost:5000")
- [ ] Browser membuka halaman tanpa error
- [ ] Peta muncul dengan 14 marker
- [ ] Legend terlihat di kanan bawah
- [ ] Title terlihat di kiri atas
- [ ] Hover marker → tooltip muncul
- [ ] Click marker → popup muncul
- [ ] Zoom in/out → peta responsive
- [ ] Refresh halaman → data berubah
- [ ] Marker warna berubah sesuai keramaian

Jika semua checklist ✅, selamat! Aplikasi siap digunakan! 🎉

---

**Selamat menjelajahi Activity Mapping UNDIP!** 🗺️

Pertanyaan? Cek dokumentasi atau lihat code comments di app.py

