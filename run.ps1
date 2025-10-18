# Start the Cement Dealer Management System

Write-Host ""
Write-Host "========================================"
Write-Host "Cement Dealer Management System"
Write-Host "========================================"
Write-Host ""

if (-not (Test-Path "venv")) {
    Write-Host "Virtual environment not found!"
    Write-Host "Please run setup.ps1 first"
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Activating virtual environment..."
& ".\venv\Scripts\Activate.ps1"

Write-Host ""
Write-Host "Starting application..."
Write-Host ""
Write-Host "Access the application at: http://localhost:5000"
Write-Host "Press Ctrl+C to stop the server"
Write-Host ""

python run.py
