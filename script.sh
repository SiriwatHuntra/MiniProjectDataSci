#!/bin/bash

# Clone the GitHub repository
git clone https://github.com/SiriwatHuntra/MiniProjectDataSci.git

# Navigate into the project directory
cd MiniProjectDataSci

# Update the package list
sudo apt update

# Install the Python virtual environment package
sudo apt install -y python3-venv

# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install required Python packages
pip install -r requirements.txt


# Run the Streamlit application
streamlit run Streamlit.py
