import streamlit as st
from datetime import datetime

def create_footer():
    """
    Create basic footer with copyright and course information
    """
    st.markdown("""
        <div class="footer">
            <p>© 2025 Heart Disease Dashboard | Kharisma Alya Septiana (2211501004)</p>
            <p>Case Based Learning - Desain Aplikasi Sains Data</p>
        </div>
    """, unsafe_allow_html=True)

def create_detailed_footer():
    """
    Create detailed footer with additional information and links
    """
    st.markdown("""
        <div style="background-color: #1f2937; 
                    padding: 2rem; 
                    border-radius: 0.5rem; 
                    margin-top: 2rem; 
                    color: #9ca3af; 
                    border-top: 2px solid #374151;">
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                
                <!-- Project Info -->
                <div>
                    <h4 style="color: #f9fafb; margin-bottom: 1rem;">📊 Heart Disease Dashboard</h4>
                    <p style="margin: 0.5rem 0;">Case Based Learning Project</p>
                    <p style="margin: 0.5rem 0;">Desain Aplikasi Sains Data</p>
                    <p style="margin: 0.5rem 0;">Universitas Indonesia</p>
                </div>
                
                <!-- Author Info -->
                <div>
                    <h4 style="color: #f9fafb; margin-bottom: 1rem;">👤 Developer</h4>
                    <p style="margin: 0.5rem 0;"><strong>Nama:</strong> Kharisma Alya Septiana</p>
                    <p style="margin: 0.5rem 0;"><strong>NIM:</strong> 2211501004</p>
                    <p style="margin: 0.5rem 0;"><strong>Email:</strong> kharisma.alya@ui.ac.id</p>
                </div>
                
                <!-- Technology Stack -->
                <div>
                    <h4 style="color: #f9fafb; margin-bottom: 1rem;">🛠️ Technology</h4>
                    <p style="margin: 0.5rem 0;">• Streamlit</p>
                    <p style="margin: 0.5rem 0;">• Python</p>
                    <p style="margin: 0.5rem 0;">• Scikit-learn</p>
                    <p style="margin: 0.5rem 0;">• Pandas & NumPy</p>
                </div>
                
                <!-- Quick Links -->
                <div>
                    <h4 style="color: #f9fafb; margin-bottom: 1rem;">🔗 Quick Links</h4>
                    <p style="margin: 0.5rem 0;">• <a href="#" style="color: #60a5fa;">Documentation</a></p>
                    <p style="margin: 0.5rem 0;">• <a href="#" style="color: #60a5fa;">GitHub Repository</a></p>
                    <p style="margin: 0.5rem 0;">• <a href="#" style="color: #60a5fa;">Report</a></p>
                    <p style="margin: 0.5rem 0;">• <a href="#" style="color: #60a5fa;">Contact</a></p>
                </div>
            </div>
            
            <hr style="border: 1px solid #374151; margin: 2rem 0;">
            
            <div style="text-align: center;">
                <p style="margin: 0.5rem 0;">© 2025 Heart Disease Dashboard. All rights reserved.</p>
                <p style="margin: 0.5rem 0; font-size: 0.9rem;">Built with ❤️ for Data Science Education</p>
                <p style="margin: 0.5rem 0; font-size: 0.8rem;">Last updated: """ + datetime.now().strftime("%B %d, %Y") + """</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

def create_minimal_footer():
    """
    Create minimal footer with just essential information
    """
    st.markdown("""
        <div style="text-align: center; 
                    padding: 1rem; 
                    margin-top: 2rem; 
                    color: #666; 
                    font-size: 0.9rem; 
                    border-top: 1px solid #eee;">
            <p>© 2025 Heart Disease Dashboard | Kharisma Alya Septiana (2211501004)</p>
        </div>
    """, unsafe_allow_html=True)

def create_stats_footer(df):
    """
    Create footer with dataset statistics
    """
    if df is not None:
        total_records = len(df)
        heart_disease_cases = df['target'].sum()
        healthy_cases = total_records - heart_disease_cases
        disease_rate = (heart_disease_cases / total_records) * 100
        
        st.markdown(f"""
            <div style="background-color: #f8f9fa; 
                        padding: 1.5rem; 
                        border-radius: 0.5rem; 
                        margin-top: 2rem; 
                        border: 1px solid #dee2e6;">
                
                <h4 style="text-align: center; margin-bottom: 1rem; color: #333;">📊 Dataset Statistics</h4>
                
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; text-align: center;">
                    <div>
                        <h5 style="margin: 0; color: #666;">Total Records</h5>
                        <p style="margin: 0; font-size: 1.5rem; font-weight: bold; color: #333;">{total_records}</p>
                    </div>
                    <div>
                        <h5 style="margin: 0; color: #666;">Heart Disease</h5>
                        <p style="margin: 0; font-size: 1.5rem; font-weight: bold; color: #dc3545;">{heart_disease_cases}</p>
                    </div>
                    <div>
                        <h5 style="margin: 0; color: #666;">Healthy</h5>
                        <p style="margin: 0; font-size: 1.5rem; font-weight: bold; color: #28a745;">{healthy_cases}</p>
                    </div>
                    <div>
                        <h5 style="margin: 0; color: #666;">Disease Rate</h5>
                        <p style="margin: 0; font-size: 1.5rem; font-weight: bold; color: #ffc107;">{disease_rate:.1f}%</p>
                    </div>
                </div>
                
                <div style="text-align: center; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #dee2e6;">
                    <p style="margin: 0; color: #666; font-size: 0.9rem;">
                        © 2025 Heart Disease Dashboard | Kharisma Alya Septiana (2211501004)
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)

def create_interactive_footer():
    """
    Create interactive footer with feedback and social links
    """
    st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; 
                    border-radius: 0.5rem; 
                    margin-top: 2rem; 
                    color: white;">
            
            <div style="text-align: center; margin-bottom: 2rem;">
                <h3 style="margin-bottom: 1rem;">💬 Feedback & Support</h3>
                <p>Bantu kami meningkatkan dashboard ini dengan memberikan feedback!</p>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
                <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 0.5rem;">
                    <h5>📧 Email</h5>
                    <p>kharisma.alya@ui.ac.id</p>
                </div>
                <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 0.5rem;">
                    <h5>📱 WhatsApp</h5>
                    <p>+62 812-3456-7890</p>
                </div>
                <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 0.5rem;">
                    <h5>🌐 Website</h5>
                    <p>ui.ac.id</p>
                </div>
            </div>
            
            <div style="text-align: center; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.2);">
                <p style="margin: 0; opacity: 0.9;">© 2025 Heart Disease Dashboard | Kharisma Alya Septiana (2211501004)</p>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.8;">
                    Case Based Learning - Desain Aplikasi Sains Data
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

def create_progress_footer():
    """
    Create footer with project progress information
    """
    st.markdown("""
        <div style="background-color: #1f2937; 
                    padding: 1.5rem; 
                    border-radius: 0.5rem; 
                    margin-top: 2rem; 
                    color: #9ca3af;">
            
            <h4 style="text-align: center; margin-bottom: 1rem; color: #f9fafb;">📈 Project Progress</h4>
            
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>Data Collection</span>
                    <span>100%</span>
                </div>
                <div style="background: #374151; border-radius: 10px; height: 8px;">
                    <div style="background: #10b981; height: 100%; width: 100%; border-radius: 10px;"></div>
                </div>
            </div>
            
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>Model Development</span>
                    <span>100%</span>
                </div>
                <div style="background: #374151; border-radius: 10px; height: 8px;">
                    <div style="background: #10b981; height: 100%; width: 100%; border-radius: 10px;"></div>
                </div>
            </div>
            
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>Dashboard Development</span>
                    <span>95%</span>
                </div>
                <div style="background: #374151; border-radius: 10px; height: 8px;">
                    <div style="background: #f59e0b; height: 100%; width: 95%; border-radius: 10px;"></div>
                </div>
            </div>
            
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span>Testing & Documentation</span>
                    <span>80%</span>
                </div>
                <div style="background: #374151; border-radius: 10px; height: 8px;">
                    <div style="background: #f59e0b; height: 100%; width: 80%; border-radius: 10px;"></div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid #374151;">
                <p style="margin: 0; font-size: 0.9rem;">© 2025 Heart Disease Dashboard | Kharisma Alya Septiana (2211501004)</p>
            </div>
        </div>
    """, unsafe_allow_html=True) 