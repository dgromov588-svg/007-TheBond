#!/bin/bash

# Check if venv folder already exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the script
cd scripts
python3 007-TheBond.py
