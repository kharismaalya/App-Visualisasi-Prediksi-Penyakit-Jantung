import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from header import create_header, create_feature_header, create_alert_header

def show_visualization_page(df, feature_labels, label_to_feature):
    """
    Display data visualization page content
    """
    create_feature_header("Dashboard Visualisasi Dataset Penyakit Jantung", "📊", 
                         "Analisis komprehensif dataset penyakit jantung dengan berbagai visualisasi")
    
    # Overview Section
    with st.expander("📈 Statistik dan Visualisasi Dataset", expanded=True):
        # Summary Statistics
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("📌 Ringkasan Statistik")
            st.dataframe(df.describe(), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Distribution Charts
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

        # Correlation Heatmap
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🔥 Korelasi Antar Fitur")
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
            st.markdown('</div>', unsafe_allow_html=True)

        # Feature Histogram
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("📊 Histogram Fitur Tertentu")
            selected_label = st.selectbox("Pilih fitur:", list(feature_labels.values()))
            selected_feature = label_to_feature[selected_label]
            fig, ax = plt.subplots()
            sns.histplot(df[selected_feature], bins=20, kde=True, ax=ax)
            st.pyplot(fig)
            st.markdown('</div>', unsafe_allow_html=True)

def show_advanced_analysis(df):
    """
    Display advanced analysis features
    """
    create_feature_header("Analisis Lanjutan", "📈", "Analisis mendalam dan insights dari dataset")
    
    # Age Analysis
    with st.expander("👥 Analisis Berdasarkan Usia", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Distribusi Usia")
            fig, ax = plt.subplots()
            sns.histplot(data=df, x='age', hue='target', bins=20, ax=ax)
            ax.set_title('Distribusi Usia berdasarkan Target')
            st.pyplot(fig)
        
        with col2:
            st.subheader("Risiko berdasarkan Usia")
            age_groups = pd.cut(df['age'], bins=[0, 40, 50, 60, 100], labels=['<40', '40-50', '50-60', '>60'])
            risk_by_age = df.groupby(age_groups)['target'].mean()
            st.bar_chart(risk_by_age)
    
    # Gender Analysis
    with st.expander("🚻 Analisis Berdasarkan Gender", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Risiko berdasarkan Gender")
            risk_by_gender = df.groupby('sex')['target'].mean()
            st.bar_chart(risk_by_gender)
        
        with col2:
            st.subheader("Distribusi Gender")
            gender_target = pd.crosstab(df['sex'], df['target'])
            st.dataframe(gender_target)
    
    # Feature Importance Analysis
    with st.expander("🎯 Analisis Kepentingan Fitur", expanded=True):
        # Calculate correlation with target
        correlations = df.corr()['target'].abs().sort_values(ascending=False)
        correlations = correlations.drop('target')
        
        st.subheader("Korelasi dengan Target")
        fig, ax = plt.subplots(figsize=(10, 6))
        correlations.plot(kind='bar', ax=ax)
        ax.set_title('Korelasi Fitur dengan Target')
        ax.set_xlabel('Fitur')
        ax.set_ylabel('Korelasi Absolut')
        plt.xticks(rotation=45)
        st.pyplot(fig)

def show_prediction_page(model):
    """
    Display prediction page content
    """
    create_feature_header("Prediksi Risiko Penyakit Jantung", "🫀", 
                         "Masukkan data pasien untuk memprediksi risiko penyakit jantung")
    
    st.markdown("Masukkan data pasien berikut untuk memprediksi apakah pasien berisiko mengalami penyakit jantung.")

    with st.expander("📝 Formulir Data Pasien", expanded=True):
        with st.form(key='prediction_form'):
            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("📋 Data Demografis")
                age = st.number_input("Umur (age)", 20, 100, 50)
                sex = st.selectbox("Jenis Kelamin (sex)", [0, 1], format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki")
                cp = st.selectbox("Tipe Nyeri Dada (cp)", [0, 1, 2, 3], 
                                format_func=lambda x: {0: "Typical Angina", 1: "Atypical Angina", 2: "Non-anginal Pain", 3: "Asymptomatic"}[x])

            with col2:
                st.subheader("💓 Data Vital")
                trestbps = st.number_input("Tekanan Darah Istirahat (trestbps)", 80, 200, 120)
                chol = st.number_input("Kolesterol (chol)", 100, 600, 250)
                fbs = st.selectbox("Gula Darah Puasa > 120 mg/dl (fbs)", [0, 1], 
                                 format_func=lambda x: "Tidak" if x == 0 else "Ya")
                thalach = st.number_input("Denyut Jantung Maksimum (thalach)", 70, 210, 150)

            with col3:
                st.subheader("🏥 Data Medis")
                restecg = st.selectbox("Hasil EKG Istirahat (restecg)", [0, 1, 2],
                                     format_func=lambda x: {0: "Normal", 1: "ST-T Wave Abnormality", 2: "Left Ventricular Hypertrophy"}[x])
                exang = st.selectbox("Angina Induksi Latihan (exang)", [0, 1],
                                   format_func=lambda x: "Tidak" if x == 0 else "Ya")
                oldpeak = st.number_input("Depresi ST (oldpeak)", 0.0, 6.0, 1.0, step=0.1)
                slope = st.selectbox("Kemiringan ST (slope)", [0, 1, 2],
                                   format_func=lambda x: {0: "Upsloping", 1: "Flat", 2: "Downsloping"}[x])
                ca = st.selectbox("Jumlah Pembuluh Besar (ca)", [0, 1, 2, 3])
                thal = st.selectbox("Thalassemia (thal)", [0, 1, 2],
                                  format_func=lambda x: {0: "Normal", 1: "Fixed Defect", 2: "Reversable Defect"}[x])

            submitted = st.form_submit_button("🔍 Mulai Prediksi")

            if submitted:
                # Show loading
                with st.spinner("Menganalisis data pasien..."):
                    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                            thalach, exang, oldpeak, slope, ca, thal]])
                    prediction = model.predict(input_data)
                    prediction_proba = model.predict_proba(input_data)

                st.markdown("---")
                
                # Display results
                if prediction[0] == 1:
                    create_alert_header("❌ Hasil Prediksi: Risiko Tinggi", "error")
                    st.error("Pasien berisiko terkena penyakit jantung.")
                    
                    # Show probability
                    risk_probability = prediction_proba[0][1] * 100
                    st.metric("Probabilitas Risiko", f"{risk_probability:.1f}%")
                    
                    st.warning("⚠️ Rekomendasi:")
                    st.markdown("- Konsultasi ke dokter spesialis jantung")
                    st.markdown("- Pemeriksaan lanjutan: EKG, treadmill test")
                    st.markdown("- Terapkan pola makan rendah kolesterol")
                    st.markdown("- Rutin olahraga ringan 30 menit/hari")
                    st.markdown("- Hindari rokok dan alkohol")
                    st.markdown("- Kontrol tekanan darah secara rutin")
                else:
                    create_alert_header("✅ Hasil Prediksi: Risiko Rendah", "success")
                    st.success("Pasien tidak berisiko terkena penyakit jantung.")
                    
                    # Show probability
                    risk_probability = prediction_proba[0][1] * 100
                    st.metric("Probabilitas Risiko", f"{risk_probability:.1f}%")
                    
                    st.info("💡 Tips menjaga kesehatan jantung:")
                    st.markdown("- Tetap jaga pola makan sehat")
                    st.markdown("- Hindari stres dan rokok")
                    st.markdown("- Olahraga teratur dan kontrol tekanan darah")
                    st.markdown("- Rutin cek kesehatan jantung")
                    st.markdown("- Istirahat yang cukup")

def show_help_page():
    """
    Display help and documentation page
    """
    create_feature_header("Bantuan & Dokumentasi", "❓", "Panduan penggunaan dashboard")
    
    # Quick Start Guide
    with st.expander("🚀 Panduan Cepat", expanded=True):
        st.markdown("""
        ### Langkah-langkah menggunakan dashboard:
        
        1. **📊 Visualisasi Data**
           - Lihat statistik dataset
           - Analisis distribusi data
           - Korelasi antar fitur
        
        2. **🫀 Prediksi Penyakit Jantung**
           - Masukkan data pasien
           - Dapatkan prediksi risiko
           - Lihat rekomendasi
        
        3. **📈 Analisis Lanjutan**
           - Analisis berdasarkan usia/gender
           - Kepentingan fitur
           - Insights mendalam
        """)
    
    # Feature Documentation
    with st.expander("📚 Dokumentasi Fitur", expanded=True):
        st.markdown("""
        ### Fitur-fitur Dashboard:
        
        **📊 Visualisasi Data:**
        - Ringkasan statistik dataset
        - Distribusi target dan gender
        - Heatmap korelasi
        - Histogram fitur
        
        **🫀 Prediksi:**
        - Form input data pasien
        - Prediksi risiko jantung
        - Probabilitas risiko
        - Rekomendasi kesehatan
        
        **📈 Analisis Lanjutan:**
        - Analisis berdasarkan demografi
        - Kepentingan fitur
        - Insights mendalam
        """)
    
    # FAQ
    with st.expander("❓ FAQ", expanded=True):
        st.markdown("""
        **Q: Bagaimana cara menggunakan fitur prediksi?**
        A: Pilih menu "Prediksi Penyakit Jantung", isi formulir data pasien, lalu klik "Mulai Prediksi".
        
        **Q: Apa arti nilai-nilai dalam dataset?**
        A: Setiap kolom memiliki arti medis tertentu. Lihat dokumentasi untuk penjelasan lengkap.
        
        **Q: Seberapa akurat model prediksi?**
        A: Model memiliki akurasi 85.2% berdasarkan testing data.
        
        **Q: Bagaimana cara menginterpretasi hasil prediksi?**
        A: Hasil 1 = berisiko, 0 = tidak berisiko. Probabilitas menunjukkan tingkat kepercayaan.
        """) 