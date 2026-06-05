#!/bin/bash
# ============================================
# Activity Mapping UNDIP - Linux/Mac Setup Script
# ============================================

echo ""
echo "============================================================"
echo "  Activity Mapping UNDIP - Automated Setup"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python3 belum terinstall"
    echo ""
    echo "Solusi:"
    echo "  macOS:  brew install python3"
    echo "  Ubuntu: sudo apt-get install python3 python3-pip"
    echo ""
    exit 1
fi

# Display Python version
PYTHON_VERSION=$(python3 --version)
echo "✅ $PYTHON_VERSION found"
echo ""

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ ERROR: pip3 tidak tersedia"
    exit 1
fi

echo "✅ pip3 tersedia"
echo ""

# Create virtual environment
echo ""
echo "============================================================"
echo "  Step 1: Creating Virtual Environment"
echo "============================================================"
echo ""

if [ -d "venv" ]; then
    echo "⚠️  Virtual environment sudah ada (venv folder)"
    echo ""
else
    echo "📦 Creating venv folder..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ ERROR: Gagal membuat virtual environment"
        exit 1
    fi
    echo "✅ Virtual environment created!"
fi

echo ""

# Activate virtual environment
echo "============================================================"
echo "  Step 2: Activating Virtual Environment"
echo "============================================================"
echo ""

source venv/bin/activate
echo "✅ Virtual environment activated!"
echo ""

# Upgrade pip
echo "============================================================"
echo "  Step 3: Upgrading pip"
echo "============================================================"
echo ""

python3 -m pip install --upgrade pip > /dev/null 2>&1
echo "✅ pip upgraded!"
echo ""

# Install dependencies
echo "============================================================"
echo "  Step 4: Installing Dependencies"
echo "============================================================"
echo ""

if [ -f "requirements.txt" ]; then
    echo "📥 Installing packages dari requirements.txt..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ ERROR: Gagal install packages"
        exit 1
    fi
    echo "✅ All packages installed successfully!"
else
    echo "❌ ERROR: requirements.txt tidak ditemukan"
    exit 1
fi

echo ""

# Display completion message
echo "============================================================"
echo "  ✅ SETUP COMPLETE!"
echo "============================================================"
echo ""
echo "🎉 Sekarang siap menjalankan aplikasi!"
echo ""
echo "Langkah selanjutnya:"
echo "  1. Pastikan terminal dalam virtual environment (venv)"
echo "  2. Jalankan: python app.py"
echo "  3. Buka browser: http://localhost:5000"
echo ""
echo "Untuk menjalankan aplikasi di lain waktu:"
echo "  1. Buka terminal di folder project"
echo "  2. Jalankan: source venv/bin/activate"
echo "  3. Jalankan: python app.py"
echo ""
echo "Info lebih lanjut: Baca README.md"
echo ""
