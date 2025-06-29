from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model Logistic Regression yang sudah disimpan
model = joblib.load('logreg_model.pkl')

@app.route('/')
def index():
    return "✅ API Prediksi Penyakit Jantung Aktif!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil data input JSON dari client
        data = request.get_json()
        features = data['features']  # Harus berupa list dengan 13 elemen

        # Validasi jumlah fitur
        if len(features) != 13:
            return jsonify({'error': 'Input harus terdiri dari 13 nilai fitur.'}), 400

        # Ubah ke array numpy dan reshape ke 2 dimensi
        input_data = np.array(features).reshape(1, -1)

        # Lakukan prediksi
        prediction = model.predict(input_data)

        # Kembalikan hasil prediksi (0 = tidak sakit, 1 = sakit)
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
