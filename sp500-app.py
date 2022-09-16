import streamlit as st
from annotated_text import annotated_text
import pandas as pd
import base64
import matplotlib.pyplot as px
import plotly.express as px
import numpy as np
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AEGIS TL Quant Macro Alpha",
    page_icon="https://aegisportfolio.com/wp-content/uploads/2022/06/icon-only.jpg",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('AEGIS TL Quant Macro Alpha - Volatility Research project. ')


st.sidebar.image("https://aegisportfolio.com/wp-content/uploads/2022/09/logo-wide.png", width=250)

st.sidebar.title("AEGIS TL RESEARCH")

st.sidebar.write("AEGIS TL is a mathematically based algorithm that can rank future volatility. TL stands for Top List. There is a 100% correlation between volatility and returns, which is proven mathematically. Since AEGIS is able to rank volatility, you as investor can control 100% the desired volatility in your portfolio compared to the market. This way, you are able to build different portfolio profiles that range from a more cautious pension portfolio to a potent alpha portfolio.")

with st.sidebar:
    components.html("""<hr style="height:5px;border:none;color:#48bc95;background-color:#48bc95;" /> """)


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Key Figures", "Portfolio", "Drawdown", "Probability & Correlation"])

with tab1:
    st.subheader("Overview")
    st.write("AEGIS is a 8-year research project. The main goal is to find new and better ways to protect a portfolio, than the traditional low gain volatility portfolio is able to provide. A part of the research is also to come up with better models for measure results. So we can separate results made randomly and results made from skills. This leads to better optimization and better results.")
    st.write("")
    st.write("A traditionel portfolio is traditionally not protected against a market crash and tall risks like a black swan. We find it more and more important to take the risks into account, when looking to a general global macro economic outlook.")
    st.write("")
    st.write("All results at this website is daily updated. The results are based on running real accounts. For futher information and deep insight in the research results, please write to: anders.hasle@icloud.com.")
    st.write("")
    st.write("")
    
    annotated_text(
        ("AEGIS objective", ":", "#48bc95"),
        " To outperform the benchmark over rolling 1-3 years periods",
    )
    st.write("")
    annotated_text(
        ("AEGIS strategy", ":", "#8097a5"),
        " AEGIS TL Quant Macro Alpha uses the ability to rank volatility to achieve controlled alpha portfolios. The quant of macro data gives a high probability to gain even in a bear market, as long as the volatility in the market is under control.",
    )    
    st.write("")     
    annotated_text(
        ("How many stocks", ":", "#0076b6"),
        " 30 stocks ",
    )   
    st.write("")    
    annotated_text(
        ("Top holdings", ":", "#e6535d"),
        " All 30 stocks in AEGIS TL Quant Macro Alpha are equal weighted ",
    )     
    
    st.write("") 
    st.write("") 
    st.write("") 
    st.subheader("Riskindicator")
    
    st.image("https://aegisportfolio.com/wp-content/uploads/2022/09/riskindicator.jpg")
    
    st.write("")
    
    st.write("")
    
    st.write("Quck disclaimer. I am not - nor is AEGIS - a licensed financial advisor. All information found in this site is purely based on my personal opinion and experience from own research and should not be construed as professional financial advice. Investors should talk to a licensed financial advisor and/or do their own research before makting any investment decisions.")
    
    
    
with tab2:
    st.subheader("Performance AEGIS vs benchmark S&P 500")  
    
    btstats = pd.DataFrame(pd.read_csv('KeyFigures.csv'))

    col1, col2, col3, col4 =  st.columns(4)
    col1.metric("Sharpe Ratio", round(btstats['Sharpe ratio'][0],2), str(round(btstats['Sharpe ratio'][1],2)) + " (S&P 500) ")
    col2.metric("Sortino Ratio", round(btstats['Sortino ratio'][0],2), str(round(btstats['Sortino ratio'][1],2)) + " (S&P 500) ")
    col3.metric("Calmar Ratio", round(btstats['Calmar ratio'][0],2), str(round(btstats['Calmar ratio'][1],2)) + " (S&P 500) ")         
    col4.metric("Max Drawdown", round(btstats['Max Drawdown'][0]*100,1), str(round(btstats['Max Drawdown'][1]*100,1)) + "% (S&P 500) ") 
    
    df = pd.DataFrame(pd.read_csv('datachart.csv'))

    df1 = pd.DataFrame(df)
    fig = px.line(df1, title='AEGIS TL Quant Macro Alpha vs S&P 500')

    fig['data'][0]['line']['color']='#48bc95'
    fig['data'][0]['line']['width']=2
    fig['data'][1]['line']['color']='#e6535d'
    fig['data'][1]['line']['width']=2    
    
    st.write(fig)
    
with tab3:
    st.subheader("30 stocks equally weighted")  
    
    PortfolioList = pd.DataFrame(pd.read_csv('PortfolioList.csv'))
    st.write(PortfolioList)
    
    col1, col2 = st.columns(2)
    
    with col1:
        New_porfolio = pd.DataFrame(pd.read_csv('All30Stocks.csv'))

        New_porfolio["NumberStocks"] = 1/30

        fig = px.pie(New_porfolio, values='NumberStocks', names='0', title='AEGIS TL Quant Macro Alpha')
        st.write(fig)  
    
    with col2:
        df = pd.DataFrame(pd.read_csv('CatAll30Stocks.csv'))

        fig = px.pie(df, values='Frequency', names='cat', title='AEGIS TL Quant Macro Alpha')
        st.write(fig)    
    
with tab4:
    st.subheader("Drawdown analysis")      
    st.write("Based on a 60 days rolling average.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        df = pd.DataFrame(pd.read_csv('DrawDownAEGIS.csv'))

        df1 = pd.DataFrame(df)
        fig = px.line(df1, title='AEGIS TL Quant Macro Alpha')

        fig['data'][0]['line']['color']='#48bc95'
        fig['data'][0]['line']['width']=2
        fig['data'][1]['line']['color']='#e6535d'
        fig['data'][1]['line']['width']=2    

        st.write(fig)   
        
    with col2:
        df = pd.DataFrame(pd.read_csv('DrawDownSPX.csv'))

        df1 = pd.DataFrame(df)
        fig = px.line(df1, title='S&P 500')

        fig['data'][0]['line']['color']='#8097a5'
        fig['data'][0]['line']['width']=2
        fig['data'][1]['line']['color']='#e6535d'
        fig['data'][1]['line']['width']=2    

        st.write(fig)     
    
with tab5:
    st.subheader("Probability & Correlation")     
    st.write("The only mathematically correct way to validate a given result is to use the binomial probability distribution")
    st.write("")
    st.write("The period needed to ensure the validity of a result has nothing to do with the length of the track period, but has to do with how consistently we outperform in the chosen time interval.")
    
 
    Sumorize = pd.DataFrame(pd.read_csv('Sumorize.csv'))
    Sumorize.columns = ['AEGIS', 'SPX']
    Sumorize['Description'] = pd.DataFrame(["Sum of minus days","Sum of plus days"])
    Sumorize = Sumorize.set_index('Description')    
    
    st.write(Sumorize)
    
    col1, col2 = st.columns(2)
    
    with col1:
        df = pd.DataFrame(pd.read_csv('ProbabilityAEGISdays.csv'))
        
        fig = px.line(df, title="Probability: 94.9% - Won 111 out of 198 days")

        fig['data'][0]['line']['color']='#48bc95'
        fig['data'][0]['line']['width']=5        

        st.write(fig)   
        
    with col2:
        df = pd.DataFrame(pd.read_csv('ProbabilityAEGISmonth.csv'))

        fig = px.line(df, title="Probability: 98.07% - Won 10 out of 12 month")

        fig['data'][0]['line']['color']='#48bc95'
        fig['data'][0]['line']['width']=5            

        st.write(fig)       
    
