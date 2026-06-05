"""
config.py - Konfigurasi Application
File ini berisi semua konfigurasi yang bisa disesuaikan
"""

# ============================================
# KONFIGURASI FLASK
# ============================================
FLASK_ENV = 'development'
FLASK_DEBUG = True
FLASK_HOST = '127.0.0.1'
FLASK_PORT = 5000

# ============================================
# KONFIGURASI PETA
# ============================================
# Default zoom level untuk peta
MAP_ZOOM_START = 16

# Default center peta (UNDIP Tembalang)
MAP_CENTER_LAT = -7.0515
MAP_CENTER_LON = 110.4390

# Basemap tile provider
MAP_TILES = 'OpenStreetMap'

# ============================================
# KONFIGURASI KERAMAIAN
# ============================================
# Range nilai keramaian (0-MAX_CROWD_VALUE)
MAX_CROWD_VALUE = 20

# Threshold kategori keramaian
CROWD_THRESHOLDS = {
    'sepi': (0, 5),          # 0-5: Sepi (Hijau)
    'sedang': (6, 15),       # 6-15: Sedang (Oranye)
    'ramai': (16, 20)        # >15: Ramai (Merah)
}

# Warna untuk setiap kategori
CROWD_COLORS = {
    'sepi': {
        'name': 'Hijau',
        'hex': '#2ecc71',
        'rgb': (46, 204, 113),
        'folium': 'green'
    },
    'sedang': {
        'name': 'Oranye',
        'hex': '#e67e22',
        'rgb': (230, 126, 34),
        'folium': 'orange'
    },
    'ramai': {
        'name': 'Merah',
        'hex': '#e74c3c',
        'rgb': (231, 76, 60),
        'folium': 'red'
    }
}

# ============================================
# KONFIGURASI HEATMAP
# ============================================
HEATMAP_MIN_OPACITY = 0.4
HEATMAP_RADIUS = 25
HEATMAP_BLUR = 15
HEATMAP_MAX_ZOOM = 18
HEATMAP_GRADIENT = {
    0.2: 'green',      # Sepi
    0.5: 'orange',     # Sedang
    1.0: 'red'         # Ramai
}

# ============================================
# KONFIGURASI MARKER
# ============================================
MARKER_RADIUS = 8
MARKER_WEIGHT = 2
MARKER_FILL_OPACITY = 0.8

# ============================================
# DAFTAR LOKASI UNIVERSITAS DIPONEGORO
# ============================================
# Format: 'Nama Lokasi': {'lat': latitude, 'lon': longitude}
LOCATIONS = {
    'Universitas Diponegoro': {'lat': -7.0507, 'lon': 110.4399},
    'Perpustakaan UNDIP': {'lat': -7.0516, 'lon': 110.4381},
    'Muladi Dome': {'lat': -7.0510, 'lon': 110.4406},
    'Rektorat UNDIP': {'lat': -7.0516, 'lon': 110.4395},
    'Fakultas Teknik': {'lat': -7.0507, 'lon': 110.4409},
    'Fakultas Hukum': {'lat': -7.0535, 'lon': 110.4387},
    'Fakultas Ekonomika dan Bisnis': {'lat': -7.0547, 'lon': 110.4377},
    'FISIP': {'lat': -7.0530, 'lon': 110.4369},
    'Fakultas Psikologi': {'lat': -7.0540, 'lon': 110.4401},
    'Fakultas Kedokteran': {'lat': -7.0488, 'lon': 110.4426},
    'FSM': {'lat': -7.0498, 'lon': 110.4384},
    'FKM': {'lat': -7.0519, 'lon': 110.4360},
    'FPP': {'lat': -7.0475, 'lon': 110.4392},
    'FPIK': {'lat': -7.0482, 'lon': 110.4413},
}

# ============================================
# KONFIGURASI UI
# ============================================
# Judul aplikasi
APP_TITLE = '🗺️ Activity Mapping UNDIP'
APP_SUBTITLE = 'Peta Keramaian Universitas Diponegoro Tembalang'

# Info banner
INFO_BANNER = 'ℹ️ Data keramaian berubah setiap halaman di-refresh. Gunakan simulasi stabil dengan variasi realistis.'

# Refresh info
REFRESH_INFO = '💡 Refresh halaman untuk memperbarui data keramaian (F5 atau Ctrl+R)'

# ============================================
# KONFIGURASI API
# ============================================
API_RESPONSE_FORMAT = 'json'  # or 'xml', 'csv', dll

# ============================================
# LOGGING
# ============================================
LOG_LEVEL = 'INFO'
LOG_FILE = 'activity_mapping.log'

# ============================================
# KONFIGURASI PENGEMBANGAN
# ============================================
# Aktifkan fitur testing/debugging
ENABLE_TESTING = True
ENABLE_API_DOCS = True

# Simpan peta sebagai file HTML (untuk development)
SAVE_MAP_HTML = False
SAVED_MAP_PATH = 'static/map.html'
