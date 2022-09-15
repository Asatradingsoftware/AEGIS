import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AEGIST TL Quant Macro Alpha",
    page_icon="https://aegisportfolio.com/wp-content/uploads/2022/06/icon-only.jpg",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('AEGIST TL Quant Macro Alpha')

st.sidebar.image("https://aegisportfolio.com/wp-content/uploads/2022/09/logo-wide.png", width=250)

st.sidebar.title("Welcome to AEGIS")

st.sidebar.subheader("Quant Macro Alpha")

sidebar.components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)

tab1, tab2, tab3, tab4 = st.tabs(["Results", "Portfolio", "Drawdown", "Probability & Correlation"])

with tab1:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")  
    
with tab2:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")  
    
with tab3:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")  
    
with tab4:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")      
