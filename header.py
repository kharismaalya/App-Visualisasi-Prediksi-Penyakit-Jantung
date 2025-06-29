import streamlit as st

def create_header(title, subtitle=None, show_breadcrumb=True):
    """
    Create header with title and optional subtitle
    
    Args:
        title (str): Main title
        subtitle (str, optional): Subtitle text
        show_breadcrumb (bool): Whether to show breadcrumb navigation
    """
    # Breadcrumb navigation
    if show_breadcrumb:
        st.markdown("""
        <div style="margin-bottom: 10px;">
            <span style="color: #666;">🏠 Home</span> 
            <span style="color: #666;">›</span> 
            <span style="color: #ff4b4b;">{}</span>
        </div>
        """.format(title), unsafe_allow_html=True)
    
    # Main header
    if subtitle:
        st.markdown(f"""
        <div class="header">
            <h1>{title}</h1>
            <p style="margin: 0; font-size: 16px; opacity: 0.9;">{subtitle}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="header">
            <h1>{title}</h1>
        </div>
        """, unsafe_allow_html=True)

def create_minimal_header(title):
    """
    Create minimal header without background
    """
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #ff4b4b; margin-bottom: 0;">{title}</h1>
        <hr style="border: 2px solid #ff4b4b; width: 100px; margin: 10px auto;">
    </div>
    """, unsafe_allow_html=True)

def create_dashboard_header():
    """
    Create main dashboard header with stats
    """
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Pasien",
            value="303",
            delta="+12%"
        )
    
    with col2:
        st.metric(
            label="Risiko Tinggi",
            value="165",
            delta="-5%"
        )
    
    with col3:
        st.metric(
            label="Risiko Rendah",
            value="138",
            delta="+8%"
        )
    
    with col4:
        st.metric(
            label="Akurasi Model",
            value="85.2%",
            delta="+2.1%"
        )

def create_feature_header(title, icon="🫀", description=None):
    """
    Create feature-specific header with icon and description
    """
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; 
                border-radius: 10px; 
                margin-bottom: 2rem; 
                text-align: center; 
                color: white;">
        <h1 style="margin: 0; font-size: 2.5rem;">{icon} {title}</h1>
        {f'<p style="margin: 10px 0 0 0; font-size: 1.1rem; opacity: 0.9;">{description}</p>' if description else ''}
    </div>
    """, unsafe_allow_html=True)

def create_alert_header(title, alert_type="info"):
    """
    Create header with alert styling
    
    Args:
        title (str): Header title
        alert_type (str): Type of alert (info, warning, error, success)
    """
    colors = {
        "info": "#3b82f6",
        "warning": "#f59e0b", 
        "error": "#ef4444",
        "success": "#10b981"
    }
    
    icons = {
        "info": "ℹ️",
        "warning": "⚠️",
        "error": "❌",
        "success": "✅"
    }
    
    color = colors.get(alert_type, colors["info"])
    icon = icons.get(alert_type, icons["info"])
    
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, {color}, {color}dd); 
                padding: 1.5rem; 
                border-radius: 8px; 
                margin-bottom: 2rem; 
                border-left: 5px solid {color};">
        <h2 style="margin: 0; color: white; display: flex; align-items: center;">
            <span style="margin-right: 10px; font-size: 1.5rem;">{icon}</span>
            {title}
        </h2>
    </div>
    """, unsafe_allow_html=True)

def create_tabbed_header(tabs_data):
    """
    Create header with tabs
    
    Args:
        tabs_data (list): List of tuples (tab_name, tab_content)
    """
    tab_names = [tab[0] for tab in tabs_data]
    selected_tab = st.tabs(tab_names)
    
    for i, (tab, content) in enumerate(tabs_data):
        with selected_tab[i]:
            st.markdown(f"### {content}")

def create_progress_header(title, progress_value, progress_text=None):
    """
    Create header with progress indicator
    """
    st.markdown(f"""
    <div style="background: #f8f9fa; 
                padding: 1.5rem; 
                border-radius: 8px; 
                margin-bottom: 2rem; 
                border: 1px solid #dee2e6;">
        <h2 style="margin: 0 0 1rem 0; color: #333;">{title}</h2>
        <div style="background: #e9ecef; border-radius: 10px; height: 20px; overflow: hidden;">
            <div style="background: linear-gradient(90deg, #ff4b4b, #ff6b6b); 
                        height: 100%; 
                        width: {progress_value}%; 
                        transition: width 0.3s ease;"></div>
        </div>
        {f'<p style="margin: 0.5rem 0 0 0; text-align: center; color: #666;">{progress_text}</p>' if progress_text else ''}
    </div>
    """, unsafe_allow_html=True) 