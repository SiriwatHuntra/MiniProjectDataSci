#!/bin/bash
# chmod +x script.sh
# Update the package list
sudo apt update

# Install Python3 and virtual environment
sudo apt install -y python3-venv git

# Clone your repository
git clone https://github.com/SiriwatHuntra/MiniProjectDataSci.git

# Navigate to the project directory
cd MiniProjectDataSci

# Set up the virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install required packages
pip install -r requirements.txt

# Optionally, run a script like `streamlit` or another task
streamlit run Streamlit.py & python3 Gradio.py

