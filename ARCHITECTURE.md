# 🏗️ Architecture & Technical Documentation

Dokumentasi teknis lengkap untuk Activity Mapping UNDIP.

## 📐 Arsitektur Sistem

```
┌─────────────────────────────────────────────────────────────┐
│                      CLIENT SIDE (Browser)                  │
│                                                              │
│  HTML (index.html) + CSS + JavaScript                      │
│  └─ Leaflet Map (rendered by Folium)                       │
│  └─ Interactive layers (markers, heatmap)                  │
└────────────────────────────────────────────────────────────┘
                          ↑
                          │ HTTP Request/Response
                          │
┌────────────────────────────────────────────────────────────┐
│                    SERVER SIDE (Flask)                      │
│                                                             │
│  app.py                                                    │
│  ├─ Route: / (GET) → render index.html with map           │
│  ├─ Route: /api/locations (GET) → return JSON             │
│  └─ Helper functions:                                     │
│     ├─ create_map() → generate Folium map object         │
│     ├─ get_crowd_level() → random simulation             │
│     └─ get_crowd_status() → determine color/status       │
│                                                             │
│  config.py (opsional)                                      │
│  └─ Centralized configuration                             │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

## 🔄 Request-Response Flow

### Ketika User Pertama Kali Buka Aplikasi

```
1. User ketik: http://localhost:5000 di browser
   ↓
2. Browser send: GET / request ke Flask server
   ↓
3. Flask receive request di route @app.route('/')
   ↓
4. Function index() dipanggil
   ↓
5. create_map() dijalankan:
   - Create folium.Map object dengan center di UNDIP
   - Loop semua 14 lokasi:
     * Generate random crowd_value (0-20)
     * Tentukan status & color via get_crowd_status()
     * Add CircleMarker ke peta
     * Add data ke heatmap_data list
   - Add HeatMap layer ke peta
   - Add legend, title, annotations
   - Render peta ke HTML string via _repr_html_()
   ↓
6. render_template('index.html', map_html=map_html)
   - Pass HTML peta ke template
   ↓
7. Flask return HTML response ke browser
   ↓
8. Browser display halaman dengan peta interaktif
```

### Ketika User Refresh Halaman

```
User tekan F5 (refresh)
   ↓
Sama seperti step 1-8, tapi dengan random value baru
   ↓
Heatmap dan marker berubah warna sesuai keramaian baru
```

## 📦 Code Structure Breakdown

### app.py Structure

```python
# 1. IMPORTS
from flask import Flask, render_template, jsonify
import folium, random, json

# 2. FLASK INITIALIZATION
app = Flask(__name__)

# 3. CONSTANTS (Data Lokasi)
LOCATIONS = {...}

# 4. UTILITY FUNCTIONS
get_crowd_level()           # Generate random 0-20
get_crowd_status()          # Map value → status/color
get_color_code()            # Map color name → hex code

# 5. CREATE MAP FUNCTION
create_map()                # Main function untuk generate peta
  ├─ Create folium.Map
  ├─ Loop lokasi & generate data
  ├─ Add markers ke peta
  ├─ Add heatmap layer
  ├─ Add legend & title
  └─ Return HTML string

# 6. FLASK ROUTES
@app.route('/')             # Homepage dengan peta
@app.route('/api/locations') # JSON API endpoint

# 7. MAIN
if __name__ == '__main__'
    app.run()
```

## 🗺️ Folium Map Components

### 1. Base Map
```python
folium.Map(
    location=[center_lat, center_lon],
    zoom_start=16,
    tiles='OpenStreetMap'  # Basemap provider
)
```
- Tiles: Using OpenStreetMap (free, no API key needed)
- Zoom: 16 (perfect untuk area UNDIP ~500m²)

### 2. Markers (Circle Markers)
```python
folium.CircleMarker(
    location=[lat, lon],
    radius=8,
    popup=folium.Popup(html_content),
    tooltip=location_name,
    color=border_color,
    fill=True,
    fillColor=fill_color,
    fillOpacity=0.8,
    weight=2
)
```
- Setiap lokasi: 1 CircleMarker
- Warna circle: sesuai keramaian
- Popup: muncul saat diklik
- Tooltip: muncul saat hover

### 3. HeatMap Layer
```python
plugins.HeatMap(
    [[lat, lon, intensity], ...],
    min_opacity=0.4,
    radius=25,
    blur=15,
    gradient={0.2: 'green', 0.5: 'orange', 1.0: 'red'}
)
```
- Input: list [latitude, longitude, intensity (0-1)]
- Intensity: normalized dari crowd_value / 20
- Gradient: smooth color transition
- Radius: 25px spreading
- Blur: 15px untuk smooth edges

### 4. Legend (HTML Element)
```python
# HTML div positioned di bottom-right
# Contain color squares + status text
```

### 5. Title (HTML Element)
```python
# HTML div positioned di top-left
# Contain app name + description
```

## 📊 Data Flow Diagram

```
┌──────────────────────────────┐
│   Crowd Value Generation     │
│  (get_crowd_level)           │
│  random.randint(0, 20)       │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│   Status Determination       │
│  (get_crowd_status)          │
│  0-5: Sepi (Hijau)          │
│  6-15: Sedang (Oranye)      │
│  >15: Ramai (Merah)         │
└──────────────┬───────────────┘
               │
               ├─────────────────┬──────────────────┐
               ↓                 ↓                  ↓
        ┌────────────┐   ┌──────────────┐   ┌───────────────┐
        │   Marker   │   │   Heatmap    │   │   Popup Info  │
        │   (Visual) │   │   (Intensity)│   │   (Metadata)  │
        └────────────┘   └──────────────┘   └───────────────┘
               │                 │                  │
               └─────────────────┴──────────────────┘
                         ↓
                 ┌──────────────────┐
                 │   Folium Map     │
                 │   (Leaflet)      │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │  HTML String     │
                 │  (_repr_html_)   │
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │   Browser        │
                 │   Visualization  │
                 └──────────────────┘
```

## 🎨 Color System

### Mapping Logic
```
Crowd Value  → Status  → Color (Name)  → Hex Code    → Folium Name
0-5          → Sepi    → Hijau         → #2ecc71     → 'green'
6-15         → Sedang  → Oranye        → #e67e22     → 'orange'
16-20        → Ramai   → Merah         → #e74c3c     → 'red'
```

### Implementasi
```python
# Color di CircleMarker
color='#2ecc71'        # Border color
fillColor='#2ecc71'    # Fill color

# Color di HeatMap gradient
gradient={
    0.2: 'green',      # Value 0-5 → green
    0.5: 'orange',     # Value 6-15 → orange
    1.0: 'red'         # Value 16-20 → red
}
```

## 🔐 Security Considerations

1. **No Authentication** - Aplikasi publik, tidak perlu login
2. **No Database** - Hanya dalam-memory simulation
3. **CORS** - Tidak ada, single origin
4. **Input Validation** - Tidak perlu, hardcoded data
5. **SQL Injection** - N/A (no database)

## ⚡ Performance Optimization

### Current Implementation
- **Sync rendering**: Peta di-render setiap request
- **No caching**: Setiap refresh = peta baru
- **Small payload**: HTML ~50-100KB (termasuk peta)

### Potential Improvements
1. **Cache map tiles** - Browser caching via OpenStreetMap
2. **Async rendering** - Untuk dataset besar
3. **WebSocket updates** - Real-time updates tanpa refresh
4. **GeoJSON overlay** - Untuk area-based data
5. **TileLayer clustering** - Untuk banyak markers

## 🧪 Testing Strategy

### Unit Testing (app.py functions)
```python
# Test get_crowd_level()
assert 0 <= get_crowd_level() <= 20

# Test get_crowd_status()
status = get_crowd_status(3)
assert status['status'] == 'Sepi'
assert status['color'] == 'green'
```

### Integration Testing
```python
# Test Flask routes
with app.test_client() as client:
    response = client.get('/')
    assert response.status_code == 200
    assert 'Activity Mapping' in response.data.decode()
```

### Manual Testing
```
1. Load halaman → Check peta tampil
2. Hover marker → Check tooltip
3. Klik marker → Check popup
4. Refresh → Check data berubah
5. Zoom in/out → Check interactivity
6. API endpoint → Check JSON valid
```

## 📚 File Dependencies

```
index.html
├─ Depends on: Folium HTML output from Flask
├─ Uses: Leaflet JS (included in Folium HTML)
├─ Uses: CSS (inline styling)
└─ Uses: JavaScript (timestamp display)

app.py
├─ Imports: Flask, folium, folium.plugins, random, json
├─ Reads: LOCATIONS constant data
├─ Generates: HTML peta via Folium
└─ Serves: HTML ke index.html template

requirements.txt
├─ Flask 2.3.3
├─ Folium 0.14.0
├─ Jinja2 3.1.2
└─ Werkzeug 2.3.7
```

## 🔄 Extension Points

### Untuk menambah feature:

1. **Real GPS Data**
   - Replace `get_crowd_level()` dengan:
   - Query API GPS tracking
   - Query IoT sensor data
   - Query database real

2. **Historical Data**
   - Simpan data ke CSV/database
   - Display chart historical trends
   - Predict future crowd

3. **Filtering**
   - Add dropdown untuk filter lokasi
   - Add date range picker
   - Add status filter

4. **Notifications**
   - Alert jika lokasi terlalu ramai
   - Email notification
   - SMS alert

5. **Integrasi**
   - Weather data overlay
   - Event calendar integration
   - Traffic data integration
   - Social media sentiment

## 📋 Development Checklist

- [x] Flask setup & configuration
- [x] Folium map generation
- [x] Marker implementation
- [x] Heatmap layer
- [x] Legend & title
- [x] Color system
- [x] Data simulation
- [x] Popup functionality
- [x] HTML template
- [x] CSS styling
- [x] API endpoint
- [x] Documentation
- [x] Testing script
- [ ] Database integration
- [ ] Real GPS data
- [ ] User authentication
- [ ] Advanced analytics

---

**Technical Stack Summary:**
- **Backend**: Python Flask
- **Mapping**: Folium (wrapper around Leaflet JS)
- **Basemap**: OpenStreetMap (via Leaflet)
- **Frontend**: HTML5, CSS3, JavaScript
- **Data**: In-memory simulation (random)
- **Deployment**: localhost:5000

---

Dibuat untuk dokumentasi teknis Teknik Geodesi UNDIP 🎓

