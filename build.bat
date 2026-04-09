@echo off
chcp 65001 >nul 2>&1
title GrimVault Chinese Edition - Build

echo.
echo ==========================================
echo   GrimVault Chinese Edition - Full Build
echo ==========================================
echo.

REM ===== Step 1: Check tools =====
echo [1/5] Checking required tools...

node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js not found. Install from https://nodejs.org
    pause
    exit /b 1
)

set SKIP_PYTHON=0
python --version >nul 2>&1
if errorlevel 1 (
    echo [WARN] Python not found. Skipping OCR exe build.
    set SKIP_PYTHON=1
)

echo [OK] Tools checked.
echo.

REM ===== Step 2: Install npm dependencies =====
echo [2/5] Installing npm dependencies...
call npm install
if errorlevel 1 (
    echo [ERROR] npm install failed.
    pause
    exit /b 1
)
echo [OK] Dependencies installed.
echo.

REM ===== Step 3: Build Vue UI =====
echo [3/5] Building Vue overlay UI...
call npx vite build
if errorlevel 1 (
    echo [ERROR] Vite build failed.
    pause
    exit /b 1
)
echo [OK] UI built.
echo.

REM ===== Step 4: Build Python OCR exe =====
if "%SKIP_PYTHON%"=="0" (
    echo [4/5] Building OCR service executable...
    echo       This may take several minutes on first run...
    pip install pyinstaller paddleocr paddlepaddle flask mss opencv-python-headless onnxruntime pywin32 numpy --quiet 2>nul
    python chinese\build_exe.py
    if errorlevel 1 (
        echo [WARN] OCR exe build failed. Users will need Python.
    ) else (
        echo [OK] OCR service built.
    )
) else (
    echo [4/5] Skipping OCR exe build - no Python.
)
echo.

REM ===== Step 5: Package with electron-builder =====
echo [5/5] Packaging installer...
call npx electron-builder --win
if errorlevel 1 (
    echo [ERROR] Packaging failed.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo   Build Complete!
echo   Output: dist\
echo ==========================================
echo.
pause
