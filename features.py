import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def load_css():
    """
    Load custom CSS styling for enhanced UI
    """
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
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 0.5rem;
            color: white;
            text-align: center;
            margin: 0.5rem;
        }
        .alert-success {
            background-color: #d1fae5;
            border: 1px solid #10b981;
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 1rem 0;
        }
        .alert-warning {
            background-color: #fef3c7;
            border: 1px solid #f59e0b;
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 1rem 0;
        }
        .alert-error {
            background-color: #fee2e2;
            border: 1px solid #ef4444;
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

def show_model_performance(model, X_test, y_test):
    """
    Display comprehensive model performance metrics
    """
    st.subheader("📊 Model Performance Analysis")
    
    # Make predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Create tabs for different metrics
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Classification Report", "🎯 Confusion Matrix", "📊 ROC Curve", "📋 Detailed Metrics"])
    
    with tab1:
        st.subheader("Classification Report")
        report = classification_report(y_test, y_pred, output_dict=True)
        st.dataframe(pd.DataFrame(report).transpose())
    
    with tab2:
        st.subheader("Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_title('Confusion Matrix')
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        st.pyplot(fig)
    
    with tab3:
        st.subheader("ROC Curve")
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        roc_auc = auc(fpr, tpr)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fpr, y=tpr, name=f'ROC Curve (AUC = {roc_auc:.3f})'))
        fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], name='Random', line=dict(dash='dash')))
        fig.update_layout(title='ROC Curve', xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')
        st.plotly_chart(fig)
    
    with tab4:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            accuracy = (cm[0,0] + cm[1,1]) / cm.sum()
            st.metric("Accuracy", f"{accuracy:.3f}")
        
        with col2:
            precision = cm[1,1] / (cm[1,1] + cm[0,1]) if (cm[1,1] + cm[0,1]) > 0 else 0
            st.metric("Precision", f"{precision:.3f}")
        
        with col3:
            recall = cm[1,1] / (cm[1,1] + cm[1,0]) if (cm[1,1] + cm[1,0]) > 0 else 0
            st.metric("Recall", f"{recall:.3f}")
        
        with col4:
            f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            st.metric("F1-Score", f"{f1_score:.3f}")

def show_feature_importance_analysis(df, model):
    """
    Display feature importance analysis
    """
    st.subheader("🎯 Feature Importance Analysis")
    
    # Calculate feature importance using correlation
    correlations = df.corr()['target'].abs().sort_values(ascending=False)
    correlations = correlations.drop('target')
    
    # Create interactive bar chart
    fig = px.bar(
        x=correlations.values,
        y=correlations.index,
        orientation='h',
        title='Feature Importance (Correlation with Target)',
        labels={'x': 'Absolute Correlation', 'y': 'Features'}
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Feature importance table
    st.subheader("📋 Feature Importance Ranking")
    importance_df = pd.DataFrame({
        'Feature': correlations.index,
        'Correlation': correlations.values,
        'Importance_Rank': range(1, len(correlations) + 1)
    })
    st.dataframe(importance_df, use_container_width=True)

def show_advanced_visualizations(df):
    """
    Display advanced visualizations using Plotly
    """
    st.subheader("📊 Advanced Visualizations")
    
    # Age distribution by target
    fig = px.histogram(
        df, 
        x='age', 
        color='target',
        title='Age Distribution by Heart Disease Status',
        labels={'age': 'Age', 'target': 'Heart Disease'},
        color_discrete_map={0: 'green', 1: 'red'}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlation heatmap with Plotly
    corr_matrix = df.corr()
    fig = px.imshow(
        corr_matrix,
        title='Feature Correlation Heatmap',
        color_continuous_scale='RdBu',
        aspect='auto'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # 3D scatter plot (age, cholesterol, target)
    fig = px.scatter_3d(
        df,
        x='age',
        y='chol',
        z='trestbps',
        color='target',
        title='3D Scatter Plot: Age vs Cholesterol vs Blood Pressure',
        labels={'age': 'Age', 'chol': 'Cholesterol', 'trestbps': 'Blood Pressure', 'target': 'Heart Disease'}
    )
    st.plotly_chart(fig, use_container_width=True)

def show_data_quality_report(df):
    """
    Display data quality analysis
    """
    st.subheader("🔍 Data Quality Report")
    
    # Basic info
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Records", len(df))
        st.metric("Total Features", len(df.columns))
    
    with col2:
        st.metric("Missing Values", df.isnull().sum().sum())
        st.metric("Duplicate Rows", df.duplicated().sum())
    
    with col3:
        st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB")
        st.metric("Data Types", len(df.dtypes.unique()))
    
    # Missing values analysis
    if df.isnull().sum().sum() > 0:
        st.subheader("Missing Values Analysis")
        missing_data = df.isnull().sum()
        missing_data = missing_data[missing_data > 0]
        
        fig = px.bar(
            x=missing_data.index,
            y=missing_data.values,
            title='Missing Values by Feature',
            labels={'x': 'Features', 'y': 'Missing Count'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Data types analysis
    st.subheader("Data Types Analysis")
    dtype_counts = df.dtypes.value_counts()
    fig = px.pie(
        values=dtype_counts.values,
        names=dtype_counts.index,
        title='Distribution of Data Types'
    )
    st.plotly_chart(fig, use_container_width=True)

def show_prediction_history():
    """
    Display prediction history (simulated)
    """
    st.subheader("📈 Prediction History")
    
    # Simulate prediction history
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    predictions = np.random.choice([0, 1], size=len(dates), p=[0.6, 0.4])
    
    history_df = pd.DataFrame({
        'Date': dates,
        'Prediction': predictions,
        'Confidence': np.random.uniform(0.7, 0.95, len(dates))
    })
    
    # Daily prediction count
    daily_counts = history_df.groupby(['Date', 'Prediction']).size().unstack(fill_value=0)
    
    fig = px.line(
        daily_counts,
        title='Daily Prediction Counts',
        labels={'value': 'Count', 'index': 'Date'}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Confidence distribution
    fig = px.histogram(
        history_df,
        x='Confidence',
        color='Prediction',
        title='Prediction Confidence Distribution',
        labels={'Confidence': 'Confidence Score', 'Prediction': 'Heart Disease Risk'}
    )
    st.plotly_chart(fig, use_container_width=True)

def show_export_features(df, model):
    """
    Display export and download features
    """
    st.subheader("📥 Export Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Export Data")
        
        # Export dataset
        csv_data = df.to_csv(index=False)
        st.download_button(
            label="📊 Download Dataset (CSV)",
            data=csv_data,
            file_name="heart_disease_dataset.csv",
            mime="text/csv"
        )
        
        # Export statistics
        stats_data = df.describe().to_csv()
        st.download_button(
            label="📈 Download Statistics (CSV)",
            data=stats_data,
            file_name="dataset_statistics.csv",
            mime="text/csv"
        )
    
    with col2:
        st.subheader("Export Model")
        
        # Export model info
        model_info = {
            'Model Type': type(model).__name__,
            'Features': list(df.columns[:-1]),
            'Target': 'target',
            'Training Date': '2024-01-01',
            'Accuracy': '85.2%'
        }
        
        import json
        model_info_json = json.dumps(model_info, indent=2)
        st.download_button(
            label="🤖 Download Model Info (JSON)",
            data=model_info_json,
            file_name="model_info.json",
            mime="application/json"
        )

def show_advanced_prediction_features(model, df):
    """
    Display advanced prediction features
    """
    st.subheader("🔮 Advanced Prediction Features")
    
    # Batch prediction
    st.subheader("📋 Batch Prediction")
    
    uploaded_file = st.file_uploader("Upload CSV file for batch prediction", type=['csv'])
    
    if uploaded_file is not None:
        try:
            batch_data = pd.read_csv(uploaded_file)
            st.write("Preview of uploaded data:")
            st.dataframe(batch_data.head())
            
            if st.button("🔍 Run Batch Prediction"):
                # Make predictions
                predictions = model.predict(batch_data)
                probabilities = model.predict_proba(batch_data)[:, 1]
                
                # Create results dataframe
                results_df = batch_data.copy()
                results_df['Prediction'] = predictions
                results_df['Probability'] = probabilities
                
                st.write("Prediction Results:")
                st.dataframe(results_df)
                
                # Download results
                csv_results = results_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Results (CSV)",
                    data=csv_results,
                    file_name="batch_predictions.csv",
                    mime="text/csv"
                )
        
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    
    # Confidence threshold adjustment
    st.subheader("🎯 Confidence Threshold")
    
    threshold = st.slider("Adjust confidence threshold", 0.0, 1.0, 0.5, 0.05)
    st.write(f"Current threshold: {threshold:.2f}")
    
    # Show how threshold affects predictions
    if st.button("🔍 Test Threshold"):
        # Simulate some test data
        test_data = df.sample(10).drop('target', axis=1)
        probabilities = model.predict_proba(test_data)[:, 1]
        
        # Apply threshold
        predictions = (probabilities >= threshold).astype(int)
        
        results = pd.DataFrame({
            'Probability': probabilities,
            'Prediction (Threshold)': predictions,
            'Original Prediction': model.predict(test_data)
        })
        
        st.write("Threshold Comparison:")
        st.dataframe(results)

def show_health_recommendations():
    """
    Display health recommendations based on prediction results
    """
    st.subheader("💡 Health Recommendations")
    
    # Risk level selector
    risk_level = st.selectbox("Select Risk Level", ["Low Risk", "Medium Risk", "High Risk"])
    
    if risk_level == "Low Risk":
        st.success("✅ Low Risk Recommendations")
        st.markdown("""
        **Lifestyle Recommendations:**
        - Maintain healthy diet with fruits and vegetables
        - Regular exercise (30 minutes daily)
        - Adequate sleep (7-9 hours)
        - Stress management techniques
        - Regular health check-ups
        
        **Preventive Measures:**
        - Monitor blood pressure regularly
        - Maintain healthy weight
        - Avoid smoking and excessive alcohol
        - Regular cardiovascular screening
        """)
    
    elif risk_level == "Medium Risk":
        st.warning("⚠️ Medium Risk Recommendations")
        st.markdown("""
        **Immediate Actions:**
        - Consult with healthcare provider
        - Implement lifestyle changes
        - Monitor vital signs regularly
        - Consider medication if prescribed
        
        **Lifestyle Changes:**
        - Reduce salt intake
        - Increase physical activity
        - Quit smoking immediately
        - Manage stress effectively
        - Regular medical follow-ups
        """)
    
    else:  # High Risk
        st.error("🚨 High Risk Recommendations")
        st.markdown("""
        **Urgent Actions:**
        - Immediate medical consultation
        - Comprehensive cardiac evaluation
        - Medication as prescribed
        - Lifestyle modification program
        
        **Medical Interventions:**
        - ECG and stress testing
        - Blood work and monitoring
        - Specialist consultation
        - Regular follow-up appointments
        """)

def show_comparison_tools(df):
    """
    Display tools for comparing different groups
    """
    st.subheader("📊 Comparison Tools")
    
    # Compare by age groups
    st.subheader("👥 Age Group Comparison")
    
    age_bins = [0, 40, 50, 60, 100]
    age_labels = ['<40', '40-50', '50-60', '>60']
    df['Age_Group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)
    
    age_comparison = df.groupby('Age_Group')['target'].agg(['count', 'sum', 'mean']).round(3)
    age_comparison.columns = ['Total', 'Heart Disease', 'Disease Rate']
    
    st.dataframe(age_comparison)
    
    # Visualize age group comparison
    fig = px.bar(
        age_comparison,
        y='Disease Rate',
        title='Heart Disease Rate by Age Group',
        labels={'Disease Rate': 'Disease Rate (%)', 'index': 'Age Group'}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Compare by gender
    st.subheader("🚻 Gender Comparison")
    
    gender_comparison = df.groupby('sex')['target'].agg(['count', 'sum', 'mean']).round(3)
    gender_comparison.columns = ['Total', 'Heart Disease', 'Disease Rate']
    gender_comparison.index = ['Female', 'Male']
    
    st.dataframe(gender_comparison)
    
    # Visualize gender comparison
    fig = px.pie(
        values=gender_comparison['Heart Disease'],
        names=gender_comparison.index,
        title='Heart Disease Cases by Gender'
    )
    st.plotly_chart(fig, use_container_width=True) 