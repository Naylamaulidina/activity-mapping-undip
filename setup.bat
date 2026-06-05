@echo off
REM ============================================
REM Activity Mapping UNDIP - Windows Setup Script
REM ============================================

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo   Activity Mapping UNDIP - Automated Setup
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python belum terinstall atau tidak dalam PATH
    echo.
    echo Solusi:
    echo 1. Download Python dari: https://www.python.org/downloads/
    echo 2. Pastikan check box "Add Python to PATH" saat instalasi
    echo 3. Restart Command Prompt atau PowerShell
    echo 4. Jalankan script ini lagi
    echo.
    pause
    exit /b 1
)

REM Display Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python found: version !PYTHON_VERSION!
echo.

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: pip tidak tersedia
    echo Jalankan: python -m pip install --upgrade pip
    pause
    exit /b 1
)

echo ✅ pip tersedia
echo.

REM Create virtual environment
echo.
echo ============================================================
echo   Step 1: Creating Virtual Environment
echo ============================================================
echo.

if exist venv (
    echo ⚠️  Virtual environment sudah ada (venv folder)
    echo.
) else (
    echo 📦 Creating venv folder...
    python -m venv venv
    if errorlevel 1 (
        echo ❌ ERROR: Gagal membuat virtual environment
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created!
)

echo.

REM Activate virtual environment
echo ============================================================
echo   Step 2: Activating Virtual Environment
echo ============================================================
echo.

call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ ERROR: Gagal mengaktifkan virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment activated!
echo.

REM Upgrade pip
echo ============================================================
echo   Step 3: Upgrading pip
echo ============================================================
echo.

python -m pip install --upgrade pip >nul 2>&1
echo ✅ pip upgraded!
echo.

REM Install dependencies
echo ============================================================
echo   Step 4: Installing Dependencies
echo ============================================================
echo.

if exist requirements.txt (
    echo 📥 Installing packages dari requirements.txt...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ ERROR: Gagal install packages
        echo Coba jalankan manual:
        echo   pip install -r requirements.txt
        pause
        exit /b 1
    )
    echo ✅ All packages installed successfully!
) else (
    echo ❌ ERROR: requirements.txt tidak ditemukan
    echo Pastikan script dijalankan dari folder project
    pause
    exit /b 1
)

echo.

REM Display completion message
echo ============================================================
echo   ✅ SETUP COMPLETE!
echo ============================================================
echo.
echo 🎉 Sekarang siap menjalankan aplikasi!
echo.
echo Langkah selanjutnya:
echo   1. Pastikan terminal masih dalam virtual environment (venv)
echo   2. Jalankan: python app.py
echo   3. Buka browser: http://localhost:5000
echo.
echo Untuk menjalankan aplikasi di lain waktu:
echo   1. Buka PowerShell di folder project
echo   2. Jalankan: .\venv\Scripts\Activate.ps1
echo   3. Jalankan: python app.py
echo.
echo Info lebih lanjut: Baca README.md
echo.
pause
