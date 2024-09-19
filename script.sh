#!/bin/bash

sudo apt update -y
sudo apt upgrade -y
git clone https://github.com/SiriwatHuntra/MiniProjectDataSci.git
cd MiniProjectDataSci/

sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install gradio
pip install scikit-learn
python3 Gradio.py