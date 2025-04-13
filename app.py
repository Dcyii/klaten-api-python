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
