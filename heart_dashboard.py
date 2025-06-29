import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import numpy as np

# Splash screen logic
if "show_dashboard" not in st.session_state:
    st.session_state.show_dashboard = False
    st.markdown("<h1 style='text-align: center; margin-top: 150px;'>TUGAS CASE BASED LEARNING<br>DESAIN APLIKASI SAINS DATA</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Kharisma Alya Septiana<br>2211501004</h2>", unsafe_allow_html=True)
    time.sleep(0.05)
    st.session_state.show_dashboard = True
    st.rerun()  # ✅ ganti dari st.experimental_rerun()

# ==== Dashboard Start ====
if st.session_state.show_dashboard:

    # Konfigurasi halaman
    st.set_page_config(
        page_title="Heart Disease Dashboard",
        page_icon="🫀",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Styling kotak visualisasi/card
    st.markdown("""
        <style>
        .card {
            background-color: #111827;
            padding: 1.5rem;
            border-radius: 0.5rem;
            border: 1px solid #374151;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar Navigasi
    menu = st.sidebar.radio("Navigasi", ["📊 Visualisasi Data", "🫀 Prediksi Penyakit Jantung"])

    # Load dataset dan model
    df = pd.read_csv('heart.csv')
    model = joblib.load("logreg_model.pkl")

    # Dictionary label untuk fitur
    feature_labels = {
        'age': 'age (Usia)',
        'sex': 'sex (Jenis Kelamin)',
        'cp': 'cp (Tipe Nyeri Dada)',
        'trestbps': 'trestbps (Tekanan Darah)',
        'chol': 'chol (Kolesterol)',
        'fbs': 'fbs (Gula Darah Puasa)',
        'restecg': 'restecg (EKG Istirahat)',
        'thalach': 'thalach (Denyut Jantung Maksimum)',
        'exang': 'exang (Angina Induksi Latihan)',
        'oldpeak': 'oldpeak (Depresi ST)',
        'slope': 'slope (Kemiringan ST)',
        'ca': 'ca (Jumlah Pembuluh Besar)',
        'thal': 'thal (Thalassemia)',
        'target': 'target (Risiko Jantung)'
    }
    label_to_feature = {v: k for k, v in feature_labels.items()}

    # ================================
    # 📊 Halaman 1: Visualisasi Data
    # ================================
    if menu == "📊 Visualisasi Data":
        st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🫀 Dashboard Visualisasi Dataset Penyakit Jantung</h1>", unsafe_allow_html=True)
        st.markdown("---")

        with st.expander("📈 Statistik dan Visualisasi Dataset", expanded=True):

            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("📌 Ringkasan Statistik")
                st.dataframe(df.describe(), use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                with st.container():
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.subheader("🔢 Distribusi Target (Penyakit Jantung)")
                    st.bar_chart(df['target'].value_counts())
                    st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                with st.container():
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.subheader("🚻 Distribusi Jenis Kelamin")
                    gender_labels = ['Laki-laki', 'Perempuan']
                    gender_counts = df['sex'].value_counts()
                    st.write("0 = Perempuan, 1 = Laki-laki")
                    fig, ax = plt.subplots()
                    ax.pie(gender_counts, labels=gender_labels, autopct='%1.1f%%', startangle=90)
                    ax.axis('equal')
                    st.pyplot(fig)
                    st.markdown('</div>', unsafe_allow_html=True)

            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("🔥 Korelasi Antar Fitur")
                fig, ax = plt.subplots(figsize=(12, 6))
                sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
                st.pyplot(fig)
                st.markdown('</div>', unsafe_allow_html=True)

            with st.container():
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader("📊 Histogram Fitur Tertentu")
                selected_label = st.selectbox("Pilih fitur:", list(feature_labels.values()))
                selected_feature = label_to_feature[selected_label]
                fig, ax = plt.subplots()
                sns.histplot(df[selected_feature], bins=20, kde=True, ax=ax)
                st.pyplot(fig)
                st.markdown('</div>', unsafe_allow_html=True)

    # ================================
    # 🫀 Halaman 2: Prediksi Penyakit Jantung
    # ================================
    elif menu == "🫀 Prediksi Penyakit Jantung":
        st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🫀 Prediksi Risiko Penyakit Jantung</h1>", unsafe_allow_html=True)
        st.markdown("Masukkan data pasien berikut untuk memprediksi apakah pasien berisiko mengalami penyakit jantung.")

        with st.expander("📝 Formulir Data Pasien", expanded=True):
            with st.form(key='prediction_form'):
                col1, col2, col3 = st.columns(3)

                with col1:
                    age = st.number_input("Umur (age)", 20, 100, 50)
                    cp = st.selectbox("Tipe Nyeri Dada (cp)", [0, 1, 2, 3])
                    fbs = st.selectbox("Gula Darah Puasa > 120 mg/dl (fbs)", [0, 1])
                    thalach = st.number_input("Denyut Jantung Maksimum (thalach)", 70, 210, 150)
                    ca = st.selectbox("Jumlah Pembuluh Besar (ca)", [0, 1, 2, 3])

                with col2:
                    sex = st.selectbox("Jenis Kelamin (sex)", [0, 1])
                    trestbps = st.number_input("Tekanan Darah Istirahat (trestbps)", 80, 200, 120)
                    restecg = st.selectbox("Hasil EKG Istirahat (restecg)", [0, 1, 2])
                    exang = st.selectbox("Angina Induksi Latihan (exang)", [0, 1])
                    thal = st.selectbox("Thalassemia (thal)", [0, 1, 2])

                with col3:
                    chol = st.number_input("Kolesterol (chol)", 100, 600, 250)
                    oldpeak = st.number_input("Depresi ST (oldpeak)", 0.0, 6.0, 1.0, step=0.1)
                    slope = st.selectbox("Kemiringan ST (slope)", [0, 1, 2])

                submitted = st.form_submit_button("🔍 Mulai Prediksi")

                if submitted:
                    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                            thalach, exang, oldpeak, slope, ca, thal]])
                    prediction = model.predict(input_data)

                    st.markdown("---")
                    if prediction[0] == 1:
                        st.error("❌ Hasil Prediksi: Pasien berisiko terkena penyakit jantung.")
                        st.warning("⚠️ Rekomendasi:")
                        st.markdown("- Konsultasi ke dokter spesialis jantung")
                        st.markdown("- Pemeriksaan lanjutan: EKG, treadmill test")
                        st.markdown("- Terapkan pola makan rendah kolesterol")
                        st.markdown("- Rutin olahraga ringan 30 menit/hari")

                    else:
                        st.success("✅ Hasil Prediksi: Pasien tidak berisiko terkena penyakit jantung.")
                        st.info("💡 Tips menjaga kesehatan jantung:")
                        st.markdown("- Tetap jaga pola makan sehat")
                        st.markdown("- Hindari stres dan rokok")
                        st.markdown("- Olahraga teratur dan kontrol tekanan darah")

