@echo off
REM Cement Dealer Management System - Setup Script for Windows

echo.
echo ========================================
echo Cement Dealer Management System Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
) else (
    echo Virtual environment already exists
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing required packages...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install packages
    pause
    exit /b 1
)

echo [4/4] Ready to run!
echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the application, run:
echo   run.bat
echo.
echo Or manually run:
echo   .\venv\Scripts\activate.ps1
echo   python run.py
echo.
echo Then open http://localhost:5000 in your browser
echo.
pause
