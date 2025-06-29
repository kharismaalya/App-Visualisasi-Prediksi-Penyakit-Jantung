import requests
import json

# URL API Flask lokal
API_URL = "http://127.0.0.1:5000/predict"

# Data uji: ganti dengan 13 nilai fitur sesuai dataset heart.csv
# Contoh nilai berdasarkan urutan umum dataset Heart Disease UCI:
# [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
test_data = {
    "features": [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]  # ganti jika kamu punya contoh lain
}

# Tampilkan data yang dikirim
print("Mengirim data berikut ke API:")
print(json.dumps(test_data, indent=4))

# Kirim request POST ke API
response = requests.post(API_URL, json=test_data)

# Tampilkan respons dari API
print("\nRespons dari API:")
print("Status Code:", response.status_code)
try:
    print(response.json())
except Exception as e:
    print("Gagal menguraikan JSON:", str(e))
    