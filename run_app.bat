@echo off
echo ========================================
echo    AI Text Analysis & Comparison App
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo Checking if requirements are installed...
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Installing requirements...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install requirements
        pause
        exit /b 1
    )
)

echo.
echo Starting the application...
echo The app will open in your default browser
echo If it doesn't open automatically, go to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

streamlit run app.py

pause 