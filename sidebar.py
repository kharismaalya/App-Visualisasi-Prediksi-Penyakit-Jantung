import streamlit as st

def create_sidebar():
    """
    Create and return sidebar navigation with dashboard information
    """
    with st.sidebar:
        # Dashboard Title
        st.markdown("## 🫀 Heart Disease Dashboard")
        st.markdown("---")
        
        # Navigation Menu
        menu = st.radio(
            "Navigasi",
            [
                "📊 Visualisasi Data",
                "🫀 Prediksi Penyakit Jantung",
                "📈 Analisis Lanjutan",
                "❓ Bantuan"
            ]
        )
        st.markdown("---")
        
        # Information Section
        st.markdown("### 📋 Informasi Dashboard")
        st.markdown("- **Dataset**: Heart Disease")
        st.markdown("- **Model**: Logistic Regression")
        st.markdown("- **Author**: Kharisma Alya Septiana")
        st.markdown("- **NIM**: 2211501004")
        
        st.markdown("---")
        
        # Dataset Info
        st.markdown("### 📊 Dataset Info")
        if 'df' in st.session_state:
            df = st.session_state.df
            st.markdown(f"- **Total Records**: {len(df)}")
            st.markdown(f"- **Features**: {len(df.columns) - 1}")
            st.markdown(f"- **Target**: Binary (0/1)")
        else:
            st.markdown("- **Total Records**: -")
            st.markdown("- **Features**: -")
            st.markdown("- **Target**: Binary (0/1)")
        
        st.markdown("---")
        
        # Quick Stats
        st.markdown("### 📈 Quick Stats")
        if 'df' in st.session_state:
            df = st.session_state.df
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Cases", len(df))
                st.metric("Heart Disease", df['target'].sum())
            with col2:
                st.metric("Healthy", len(df) - df['target'].sum())
                st.metric("Disease Rate", f"{(df['target'].sum()/len(df)*100):.1f}%")
        
        st.markdown("---")
        
        # Help Section
        with st.expander("❓ Bantuan"):
            st.markdown("""
            **Cara menggunakan dashboard:**
            1. Pilih menu navigasi di atas
            2. **Visualisasi Data**: Lihat grafik dan statistik dataset
            3. **Prediksi**: Masukkan data pasien untuk prediksi
            4. **Analisis Lanjutan**: Analisis demografi dan fitur
            """)
    
    return menu

def create_advanced_sidebar():
    """
    Create advanced sidebar with additional features
    """
    with st.sidebar:
        # Dashboard Title with logo
        st.markdown("""
        <div style="text-align: center; padding: 10px;">
            <h2>🫀 Heart Disease Dashboard</h2>
            <p style="font-size: 12px; color: #666;">Case Based Learning</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        
        # Navigation with icons
        menu = st.radio("📱 Navigasi", [
            "📊 Visualisasi Data", 
            "🫀 Prediksi Penyakit Jantung",
            "📈 Analisis Lanjutan",
            "⚙️ Pengaturan"
        ])
        st.markdown("---")
        
        # User Profile Section
        st.markdown("### 👤 Profil")
        st.markdown("**Nama**: Kharisma Alya Septiana")
        st.markdown("**NIM**: 2211501004")
        st.markdown("**Mata Kuliah**: Desain Aplikasi Sains Data")
        
        st.markdown("---")
        
        # Model Information
        st.markdown("### 🤖 Model Info")
        st.markdown("**Algoritma**: Logistic Regression")
        st.markdown("**Akurasi**: 85.2%")
        st.markdown("**Precision**: 83.1%")
        st.markdown("**Recall**: 87.3%")
        
        st.markdown("---")
        
        # Quick Actions
        st.markdown("### ⚡ Quick Actions")
        if st.button("🔄 Refresh Data"):
            st.rerun()
        
        if st.button("📥 Download Report"):
            st.info("Fitur download report akan segera tersedia!")
        
        st.markdown("---")
        
        # Theme Selector
        st.markdown("### 🎨 Tema")
        theme = st.selectbox("Pilih tema", ["Dark", "Light", "Auto"])
        if theme != "Auto":
            st.info(f"Tema {theme} dipilih")
        
        st.markdown("---")
        
        # Footer in sidebar
        st.markdown("""
        <div style="text-align: center; font-size: 10px; color: #666;">
            © 2025 Heart Disease Dashboard<br>
            Powered by Streamlit
        </div>
        """, unsafe_allow_html=True)
    
    return menu 