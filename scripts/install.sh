#!/bin/bash

cd /home/ec2-user/klaten-api-python

# Aktifkan virtualenv (opsional)
# python3 -m venv venv
# source venv/bin/activate

pip3 install -r requirements.txt

# Hentikan proses Python sebelumnya (jika ada)
pkill -f "python3 app.py"

# Jalankan ulang aplikasinya di background
nohup python3 app.py > app.log 2>&1 &
