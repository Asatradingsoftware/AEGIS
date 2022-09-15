import streamlit as st
from annotated_text import annotated_text
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

st.title('AEGIS TL Quant Macro Alpha')

st.sidebar.image("https://aegisportfolio.com/wp-content/uploads/2022/09/logo-wide.png", width=250)

st.sidebar.title("Welcome to AEGIS TL")

st.sidebar.write("AEGIS TL is a mathematically based algorithm that can rank future volatility. TL stands for Top List. There is a 100% correlation between volatility and returns, which can be proven mathematically. Since AEGIS can rank volatility, you can control 100% the desired volatility in your portfolio compared to the market. In this way, you can put together everything from the prudent pension portfolio to a more alpha portfolio.")

with st.sidebar:
    components.html("""<hr style="height:5px;border:none;color:#48bc95;background-color:#48bc95;" /> """)


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Results", "Portfolio", "Drawdown", "Probability & Correlation"])

with tab1:
    st.subheader("Overview")
    
    annotated_text(
        ("AEGIS objective", ":", "#48bc95"),
        " To outperform the Benchmark over rolling 1-3 years periods ",
    )
    st.write("")
    annotated_text(
        ("AEGIS strategy", ":", "#8097a5"),
        " AEGIS TL Quant Macro Alpha use the ability to rank volatility to achieve controlled alpha. The quant of macro data give a high probability to gain even in a bear market, as long the volatility in the market is under control.",
    )    
    st.write("")     
    annotated_text(
        ("How many stocks", ":", "#02314b"),
        " 30 stocks ",
    )   
    st.write("")    
    annotated_text(
        ("Top holdings", ":", "#e6535d"),
        " Alle 30 stocks in AEGIS TL Quant Macro Alpha are equal weighted ",
    )     
    
with tab2:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")  
    
with tab3:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")  
    
with tab4:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")      
    
with tab5:
    st.subheader("Results for AEGIS TL Quant Macro Alpha")        
