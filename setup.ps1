# Cement Dealer Management System - Setup Script for PowerShell

Write-Host ""
Write-Host "========================================"
Write-Host "Cement Dealer Management System Setup"
Write-Host "========================================"
Write-Host ""

# Check if Python is installed
try {
    python --version | Out-Null
} catch {
    Write-Host "Error: Python is not installed or not in PATH"
    Write-Host "Please install Python from https://www.python.org/"
    Read-Host "Press Enter to exit"
    exit 1
}

# Create virtual environment
Write-Host "[1/4] Creating virtual environment..."
if (-not (Test-Path "venv")) {
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Failed to create virtual environment"
        Read-Host "Press Enter to exit"
        exit 1
    }
} else {
    Write-Host "Virtual environment already exists"
}

# Activate virtual environment
Write-Host "[2/4] Activating virtual environment..."
& ".\venv\Scripts\Activate.ps1"

# Install packages
Write-Host "[3/4] Installing required packages..."
python -m pip install --upgrade pip
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to install packages"
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[4/4] Ready to run!"
Write-Host ""
Write-Host "========================================"
Write-Host "Setup Complete!"
Write-Host "========================================"
Write-Host ""
Write-Host "To start the application, run:"
Write-Host "  .\run.ps1"
Write-Host ""
Write-Host "Or manually run:"
Write-Host "  .\venv\Scripts\Activate.ps1"
Write-Host "  python run.py"
Write-Host ""
Write-Host "Then open http://localhost:5000 in your browser"
Write-Host ""
Read-Host "Press Enter to exit"
