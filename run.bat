@echo off
REM Start the Cement Dealer Management System

echo.
echo ========================================
echo Cement Dealer Management System
echo ========================================
echo.

if not exist "venv" (
    echo Virtual environment not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting application...
echo.
echo Access the application at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python run.py
