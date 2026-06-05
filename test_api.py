"""
Script untuk testing API endpoint
Jalankan script ini untuk memastikan API /api/locations berfungsi dengan baik
"""

import requests
import json
from datetime import datetime

# URL API
API_URL = "http://localhost:5000/api/locations"

def test_api():
    """Test API endpoint dan display hasilnya"""
    print("=" * 70)
    print("🧪 Testing Activity Mapping UNDIP - API Endpoint")
    print("=" * 70)
    print(f"⏰ Waktu test: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"📍 URL: {API_URL}\n")
    
    try:
        # Send GET request ke API
        response = requests.get(API_URL, timeout=5)
        
        # Check status code
        if response.status_code == 200:
            print("✅ Response Status: 200 OK\n")
            
            # Parse JSON
            data = response.json()
            
            # Display timestamp
            print(f"⏱️  Timestamp: {data['timestamp']}")
            print(f"📊 Total lokasi: {len(data['locations'])}\n")
            
            # Display setiap lokasi
            print("Daftar Lokasi dengan Status Keramaian:")
            print("-" * 70)
            
            for i, location in enumerate(data['locations'], 1):
                crowd_emoji = {
                    'Sepi': '🟢',
                    'Sedang': '🟠',
                    'Ramai': '🔴'
                }
                emoji = crowd_emoji.get(location['crowd_status'], '⚪')
                
                print(f"\n{i}. {location['name']}")
                print(f"   📍 Lat: {location['latitude']:.4f}, Lon: {location['longitude']:.4f}")
                print(f"   👥 Keramaian: {emoji} {location['crowd_status']} (nilai: {location['crowd_value']}/20)")
                print(f"   🎨 Warna: {location['crowd_color'].capitalize()}")
            
            print("\n" + "=" * 70)
            print("✅ API test berhasil!")
            print("=" * 70)
            
        else:
            print(f"❌ Error: Status code {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Tidak bisa connect ke server")
        print(f"   Pastikan Flask server sudah running di {API_URL}")
        print(f"   Jalankan: python app.py")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    # Install requests jika belum
    try:
        import requests
    except ImportError:
        print("Library 'requests' belum terinstall")
        print("Jalankan: pip install requests")
        exit(1)
    
    test_api()
