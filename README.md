# 🫀 Heart Disease Dashboard

A comprehensive Streamlit dashboard for heart disease prediction and analysis, built with a modular architecture.

## 📋 Project Information

- **Author**: Kharisma Alya Septiana
- **NIM**: 2211501004
- **Course**: Case Based Learning - Desain Aplikasi Sains Data
- **University**: Universitas Indonesia

## 🏗️ Project Structure

```
dasd/
├── heart_dashboard.py      # Main application file
├── sidebar.py             # Sidebar components
├── header.py              # Header components
├── content.py             # Main content pages
├── footer.py              # Footer components
├── features.py            # Advanced features and utilities
├── heart.csv              # Heart disease dataset
├── logreg_model.pkl       # Trained logistic regression model
├── rf_model.pkl           # Random forest model (backup)
├── app.py                 # Original app file
├── test_client.py         # Test client
└── README.md              # This file
```

## 🚀 Features

### 📊 Core Features
- **Data Visualization**: Comprehensive dataset analysis with charts and statistics
- **Heart Disease Prediction**: Interactive form for patient data input and risk prediction
- **Advanced Analysis**: Deep insights into age, gender, and feature importance
- **Settings Management**: Customizable dashboard preferences
- **Help & Documentation**: User guide and FAQ

### 🎨 UI Components

#### Sidebar (`sidebar.py`)
- **Basic Sidebar**: Navigation and essential information
- **Advanced Sidebar**: Extended features with user profile, model info, and quick actions
- **Real-time Statistics**: Live dataset metrics
- **Help Section**: User guidance and feature documentation

#### Header (`header.py`)
- **Standard Header**: Clean title display
- **Dashboard Header**: Metrics overview with key statistics
- **Feature Header**: Icon-based headers with descriptions
- **Alert Header**: Color-coded alert messages
- **Progress Header**: Progress indicators
- **Tabbed Header**: Multi-tab navigation

#### Content (`content.py`)
- **Visualization Page**: Data exploration and charts
- **Prediction Page**: Patient data input and risk assessment
- **Advanced Analysis**: Demographic and feature analysis
- **Settings Page**: Dashboard configuration
- **Help Page**: Documentation and guides

#### Footer (`footer.py`)
- **Basic Footer**: Simple copyright information
- **Detailed Footer**: Comprehensive project information
- **Minimal Footer**: Essential information only
- **Stats Footer**: Dataset statistics display
- **Interactive Footer**: Contact information and feedback
- **Progress Footer**: Project completion status

#### Advanced Features (`features.py`)
- **Model Performance**: Comprehensive model evaluation metrics
- **Feature Importance**: Correlation and importance analysis
- **Advanced Visualizations**: Interactive Plotly charts
- **Data Quality Report**: Dataset health assessment
- **Export Tools**: Data and model export functionality
- **Batch Prediction**: Multiple patient predictions
- **Health Recommendations**: Personalized health advice
- **Comparison Tools**: Demographic comparisons

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Model Storage**: Joblib

## 📈 Model Information

- **Algorithm**: Logistic Regression
- **Accuracy**: 85.2%
- **Precision**: 83.1%
- **Recall**: 87.3%
- **Dataset**: 303 records, 13 features

## 🚀 Installation & Usage

### Prerequisites
```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn joblib plotly
```

### Running the Dashboard
```bash
streamlit run heart_dashboard.py
```

### Access the Dashboard
Open your browser and navigate to `http://localhost:8501`

## 📱 Dashboard Navigation

### Main Pages
1. **📊 Visualisasi Data**: Dataset exploration and visualization
2. **🫀 Prediksi Penyakit Jantung**: Heart disease risk prediction
3. **📈 Analisis Lanjutan**: Advanced demographic analysis
4. **⚙️ Pengaturan**: Dashboard configuration
5. **❓ Bantuan**: Help and documentation

### Sidebar Options
- **Use Advanced Sidebar**: Toggle between basic and advanced sidebar
- **Footer Style**: Choose from 6 different footer styles
- **Real-time Stats**: Live dataset metrics
- **Quick Actions**: Refresh data and download reports

## 🎨 Customization

### Themes
- **Dark Theme**: Professional dark interface
- **Light Theme**: Clean light interface
- **Auto Theme**: System-based theme selection

### Footer Styles
1. **Basic**: Simple copyright information
2. **Detailed**: Comprehensive project details
3. **Minimal**: Essential information only
4. **Stats**: Dataset statistics
5. **Interactive**: Contact and feedback
6. **Progress**: Project completion status

## 📊 Dataset Features

| Feature | Description | Range |
|---------|-------------|-------|
| age | Patient age | 20-100 |
| sex | Gender (0=Female, 1=Male) | 0-1 |
| cp | Chest pain type | 0-3 |
| trestbps | Resting blood pressure | 80-200 |
| chol | Cholesterol level | 100-600 |
| fbs | Fasting blood sugar | 0-1 |
| restecg | ECG results | 0-2 |
| thalach | Max heart rate | 70-210 |
| exang | Exercise angina | 0-1 |
| oldpeak | ST depression | 0.0-6.0 |
| slope | ST slope | 0-2 |
| ca | Number of vessels | 0-3 |
| thal | Thalassemia | 0-2 |
| target | Heart disease (0=No, 1=Yes) | 0-1 |

## 🔧 Advanced Features

### Model Performance Analysis
- Classification report
- Confusion matrix
- ROC curve analysis
- Detailed metrics (Accuracy, Precision, Recall, F1-Score)

### Feature Importance
- Correlation analysis
- Feature ranking
- Interactive importance charts

### Data Export
- Dataset download (CSV)
- Statistics export
- Model information export
- Batch prediction results

### Health Recommendations
- Risk-based recommendations
- Lifestyle advice
- Medical intervention guidance

## 📈 Performance Metrics

- **Total Records**: 303
- **Heart Disease Cases**: 165 (54.5%)
- **Healthy Cases**: 138 (45.5%)
- **Model Accuracy**: 85.2%
- **Processing Time**: < 2 seconds

## 🤝 Contributing

This is a course project for Case Based Learning. For questions or feedback, contact:
- **Email**: kharisma.alya@ui.ac.id
- **Course**: Desain Aplikasi Sains Data
- **University**: Universitas Indonesia

## 📄 License

This project is created for educational purposes as part of the Case Based Learning course at Universitas Indonesia.

## 🎯 Future Enhancements

- [ ] Real-time data updates
- [ ] Multiple model comparison
- [ ] Mobile app version
- [ ] API integration
- [ ] User authentication
- [ ] Prediction history tracking
- [ ] Advanced ML algorithms
- [ ] Multi-language support

---

**Built with ❤️ for Data Science Education**
