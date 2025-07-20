#!/bin/bash

echo "========================================"
echo "   AI Text Analysis & Comparison App"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "Python version:"
python3 --version
echo

# Check if requirements are installed
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "Installing requirements..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install requirements"
        exit 1
    fi
fi

echo
echo "Starting the application..."
echo "The app will open in your default browser"
echo "If it doesn't open automatically, go to: http://localhost:8501"
echo
echo "Press Ctrl+C to stop the application"
echo

streamlit run app.py 