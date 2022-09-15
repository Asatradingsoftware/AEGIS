import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('AEGIST TL Quant Macro Alpha')

st.sidebar.header('User Input Features')

tab1, tab2, tab3, tab4 = st.tabs(["Results", "Portfolio", "Drawdown", "Probability & Correlation"])

with tab1:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")  
    
with tab2:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")  
    
with tab3:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")  
    
with tab4:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")      
