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

st.title('AEGIST TL Quant Macro Alpha')

st.sidebar.image("https://aegisportfolio.com/wp-content/uploads/2022/09/logo-wide.png", width=250)

st.sidebar.title("Welcome to AEGIS")

with st.sidebar:
    components.html("""<hr style="height:5px;border:none;color:#48bc95;background-color:#48bc95;" /> """)

st.sidebar.subheader("AEGIS TL")
st.sidebar.write("AEGIS TL er en matematisk baseret algoritme, der kan rangererer fremtidig volatilitet. TL står for Top List. Der er en korrelation på 100% mellem volatilitet og afkast, hvilket kan bevises matematisk. Eftersom AEGIS kan rangerer volatilitet, kan man kontrollere 100% den ønskede volatilitet i sin portefølje sammenlignet med markedet. Dermed kan man sammensætte alt fra den forsigtige pensions portefølje over til et mere alpha præget portefølje.")



tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Results", "Portfolio", "Drawdown", "Probability & Correlation"])

with tab1:
    st.subheader("Overview")
    
    annotated_text(
        ("AEGIS objective", ":", "#48bc95"),
        " To outperform the Benchmark over rolling 1-3 years periods ",
    )
    components.html("""<hr style="height:1px;border:none;color:#8097a5;background-color:#8097a5;" /> """)   
    annotated_text(
        ("AEGIS strategy", ":", "#8097a5"),
        " To outperform the Benchmark over rolling 1-3 years periods ",
    )    
    components.html("""<hr style="height:1px;border:none;color:#8097a5;background-color:#8097a5;" /> """)      
    annotated_text(
        ("How many stocks", ":", "#02314b"),
        " 30 stocks ",
    )   
    components.html("""<hr style="height:1px;border:none;color:#8097a5;background-color:#8097a5;" /> """)        
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
