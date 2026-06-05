# Activity Mapping UNDIP - Quick Start Guide

## ⚡ Quick Setup (5 Menit)

### 1. Open Terminal di VS Code
Ctrl + ` (backtick)

### 2. Create Virtual Environment
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run Application
```
python app.py
```

### 5. Open Browser
```
http://localhost:5000
```

---

## 🔍 Testing API

Untuk test API endpoint:

```bash
python test_api.py
```

Atau buka di browser:
```
http://localhost:5000/api/locations
```

---

## 📝 File Structure

```
activity-mapping-undip/
├── app.py                 ← Main Flask application
├── requirements.txt       ← Python dependencies
├── README.md             ← Full documentation
├── QUICKSTART.md         ← File ini (quick guide)
├── test_api.py           ← API testing script
├── .gitignore           ← Git ignore rules
├── templates/
│   └── index.html       ← HTML template
└── static/              ← Static files folder
```

---

## 🎯 Fitur Utama

✅ Peta interaktif dengan OpenStreetMap
✅ Heatmap keramaian real-time (refresh dependent)
✅ 14 lokasi UNDIP dengan marker
✅ 3 kategori keramaian (Hijau/Oranye/Merah)
✅ Data simulasi stabil dan realistis
✅ Legend dan title pada peta
✅ API endpoint JSON
✅ UI modern dan responsive

---

## 🐛 Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 5000 used | Change port in app.py |
| Module not found | Run: `pip install -r requirements.txt` |
| Peta tidak muncul | F5 refresh, cek console F12 |
| Server tidak start | Cek antivirus, port conflicts |

---

## 📖 Documentation

Lihat `README.md` untuk dokumentasi lengkap!

---

Happy mapping! 🗺️

