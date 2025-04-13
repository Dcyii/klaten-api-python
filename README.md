# api-klaten
---------------------------------------------------------
Berikut ini adalah isi file dan struktur folder proyek `klaten-api-python` yang di upload ke GitHub:

---

### 📁 Struktur Folder

```
klaten-api-python/
│
├── app.py
├── requirements.txt
├── appspec.yml
├── scripts/
│   └── install.sh
```

---

### ✅ **1. `app.py`**
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Selamat datang di API Klaten"})

@app.route('/kecamatan')
def kecamatan():
    data = [
        "Bayat", "Cawas", "Ceper", "Delanggu", "Gantiwarno",
        "Jatinom", "Jogonalan", "Karanganom", "Karangdowo", "Karangnongko",
        "Kebonarum", "Kemalang", "Klaten Selatan", "Klaten Tengah", "Klaten Utara"
    ]
    return jsonify({"kecamatan": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

### ✅ **2. `requirements.txt`**
```
flask
```

---

### ✅ **3. `appspec.yml`**
```yaml
version: 0.0
os: linux
files:
  - source: /
    destination: /home/ec2-user/klaten-api-python
hooks:
  AfterInstall:
    - location: scripts/install.sh
      timeout: 300
      runas: ec2-user
```

---

### ✅ **4. `scripts/install.sh`**
```bash
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
```
