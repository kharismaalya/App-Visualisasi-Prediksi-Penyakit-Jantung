import time
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Import modular components
from sidebar import create_sidebar, create_advanced_sidebar
from header import create_header, create_dashboard_header, create_feature_header
from content import (
    show_visualization_page, 
    show_prediction_page, 
    show_advanced_analysis,
    show_help_page
)

# ================================
# 🎯 SPLASH SCREEN LOGIC
# ================================
def show_splash_screen():
    """Display splash screen with title and author information"""
    if "show_dashboard" not in st.session_state:
        st.session_state.show_dashboard = False
        st.markdown("<h1 style='text-align: center; margin-top: 150px;'>TUGAS CASE BASED LEARNING<br>DESAIN APLIKASI SAINS DATA</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Kharisma Alya Septiana<br>2211501004</h2>", unsafe_allow_html=True)
        time.sleep(0.05)
        st.session_state.show_dashboard = True
        st.rerun()

# ================================
# 🚀 MAIN APPLICATION
# ================================
def main():
    """Main application function"""
    # Show splash screen if needed
    show_splash_screen()
    
    # Only proceed if dashboard should be shown
    if st.session_state.show_dashboard:
        # Page configuration
        st.set_page_config(
            page_title="Heart Disease Dashboard",
            page_icon="🫀",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        # Add CSS directly here
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
            .header {
                background: linear-gradient(90deg, #ff4b4b, #ff6b6b);
                padding: 1rem;
                border-radius: 0.5rem;
                margin-bottom: 2rem;
                text-align: center;
                color: white;
            }
            .footer {
                background-color: #1f2937;
                padding: 1rem;
                border-radius: 0.5rem;
                margin-top: 2rem;
                text-align: center;
                color: #9ca3af;
                border-top: 2px solid #374151;
            }
            </style>
        """, unsafe_allow_html=True)
        # Load data and model
        df = pd.read_csv('heartclean.csv')
        model = joblib.load("logreg_model.pkl")
        # Store data in session state for sidebar access
        st.session_state.df = df
        # Feature labels dictionary
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
        # Create sidebar and get navigation
        menu = create_sidebar()
        # Main content area based on navigation
        if menu == "📊 Visualisasi Data":
            show_visualization_page(df, feature_labels, label_to_feature)
        elif menu == "🫀 Prediksi Penyakit Jantung":
            show_prediction_page(model)
        elif menu == "📈 Analisis Lanjutan":
            show_advanced_analysis(df)
        elif menu == "❓ Bantuan":
            show_help_page()
        # Simple footer
        st.markdown("""
            <div class='footer'>
                <p>© 2025 Heart Disease Dashboard | Kharisma Alya Septiana (2211501004)</p>
                <p>Case Based Learning - Desain Aplikasi Sains Data</p>
            </div>
        """, unsafe_allow_html=True)

# ================================
# 🔧 ADVANCED FEATURES SECTION
# ================================
def show_advanced_features_section(df, model):
    """Display advanced features in a separate section"""
    st.markdown("---")
    st.markdown("## 🔧 Advanced Features")
    
    # Create tabs for different advanced features
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Model Performance", 
        "🎯 Feature Analysis", 
        "📈 Advanced Viz", 
        "🔍 Data Quality", 
        "📥 Export Tools"
    ])
    
    with tab1:
        # Note: This would need X_test and y_test data
        st.info("Model performance analysis requires test data. This is a demonstration.")
        # show_model_performance(model, X_test, y_test)
    
    with tab2:
        show_feature_importance_analysis(df, model)
    
    with tab3:
        show_advanced_visualizations(df)
    
    with tab4:
        show_data_quality_report(df)
    
    with tab5:
        show_export_features(df, model)

# ================================
# 🎨 THEME AND STYLING
# ================================
def apply_theme(theme_name):
    """Apply different themes to the dashboard"""
    if theme_name == "Dark":
        st.markdown("""
            <style>
            .stApp {
                background-color: #1a1a1a;
                color: #ffffff;
            }
            </style>
        """, unsafe_allow_html=True)
    elif theme_name == "Light":
        st.markdown("""
            <style>
            .stApp {
                background-color: #ffffff;
                color: #000000;
            }
            </style>
        """, unsafe_allow_html=True)

# ================================
# 📱 RESPONSIVE DESIGN
# ================================
def make_responsive():
    """Add responsive design elements"""
    st.markdown("""
        <style>
        @media (max-width: 768px) {
            .stApp {
                padding: 1rem;
            }
            .card {
                margin: 0.5rem 0;
                padding: 1rem;
            }
        }
        </style>
    """, unsafe_allow_html=True)

# Run the application
if __name__ == "__main__":
    main()

