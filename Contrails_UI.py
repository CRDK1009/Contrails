import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import statsmodels.api as sm
from datetime import datetime
import plotly.graph_objects as go
#from meteostat import Hourly, Point, Daily

st.title('REDUCTION IN CONDENSATION TRAILS') 
st.markdown("_~ C R Deepak Kumar_")
st.markdown("_This application is used for the flight path between Moscow and Paris. This application can show the Aviation Industry at which Longitude,Latitude and Altitude a plane will make a Contrail. This will hence help the Aviation Industry reduce 60% of Pollution caused by Contrails._")
st.markdown("_To help in this venture, this application will ask the Aviation users to give the inputs for for a plane's flight path which are the Altitude and the hour of the day over each city of the flight path. With the given information using Appleman chart I can find whether at that particular point Contrail will be formed or not._")
st.markdown("_This application can predict whether a Contrail will form or not, given the inputs requested. It can give a forecast for any number of hours the user chooses before the scheduled departure thereby letting the Aviation officials know beforehand to make anychanges to the flight path if there is a Contrail formation or not._")


Start_title=st.sidebar.title('Choose Altitude in feet')
Moscow_alt=st.sidebar.number_input('Moscow')
Moscow_hour=st.sidebar.selectbox('Hour at Moscow',range(1,24))
Minsk_alt=st.sidebar.number_input('Minsk')
Minsk_hour=st.sidebar.selectbox('Hour at Minsk',range(1,24))
Berlin_alt=st.sidebar.number_input('Berlin')
Berlin_hour=st.sidebar.selectbox('Hour at Berlin',range(1,24))
Colgne_alt=st.sidebar.number_input('Colgne')
Colgne_hour=st.sidebar.selectbox('Hour at Colgne',range(1,24))
Lux_alt=st.sidebar.number_input('Lux')
Lux_hour=st.sidebar.selectbox('Hour at Lux',range(1,24))
Reims_alt=st.sidebar.number_input('Reims')
Reims_hour=st.sidebar.selectbox('Hour at Reims',range(1,24))
Paris_alt=st.sidebar.number_input('Paris')
Paris_hour=st.sidebar.selectbox('Hour at Paris',range(1,24))

if st.sidebar.button('Predict'):
    Moscow_temp=pd.read_csv('moscow_temp.csv')
    Minsk_temp=pd.read_csv('Minsk_temp.csv')
    Berlin_temp=pd.read_csv('Berlin_temp.csv')
    Colgne_temp=pd.read_csv('Colgne_temp.csv')
    Lux_temp=pd.read_csv('lux_temp.csv')
    Reims_temp=pd.read_csv('reims_temp.csv')
    Paris_temp=pd.read_csv('Paris_temp.csv')
    Moscow_pres=pd.read_csv('moscow_pres.csv')
    Minsk_pres=pd.read_csv('Minsk_pres.csv')
    Berlin_pres=pd.read_csv('Berlin_pres.csv')
    Colgne_pres=pd.read_csv('Colgne_pres.csv')
    Lux_pres=pd.read_csv('Lux_pres.csv')
    Reims_pres=pd.read_csv('reims_pres.csv')
    Paris_pres=pd.read_csv('Paris_pres.csv')
    Moscow_temp=Moscow_temp.drop(['time'],axis=1)
    Minsk_temp=Minsk_temp.drop(['time'],axis=1)
    Berlin_temp=Berlin_temp.drop(['time'],axis=1)
    Colgne_temp=Colgne_temp.drop(['time'],axis=1)
    Lux_temp=Lux_temp.drop(['time'],axis=1)
    Reims_temp=Reims_temp.drop(['time'],axis=1)
    Paris_temp=Paris_temp.drop(['time'],axis=1)
    Moscow_pres=Moscow_pres.drop(['time'],axis=1)
    Minsk_pres=Minsk_pres.drop(['time'],axis=1)
    Berlin_pres=Berlin_pres.drop(['time'],axis=1)
    Colgne_pres=Colgne_pres.drop(['time'],axis=1)
    Lux_pres=Lux_pres.drop(['time'],axis=1)
    Reims_pres=Reims_pres.drop(['time'],axis=1)
    Paris_pres=Paris_pres.drop(['time'],axis=1)
    
    a=Moscow_pres.iloc[[Moscow_hour]].to_numpy()
    
    Moscow_temp_fahr = (Moscow_temp.iloc[[Moscow_hour]] * 9.0/5.0) + 32.0
    Moscow_temp_alt=Moscow_alt*0.00356
    Moscow_temp_fahr = Moscow_temp_fahr - Moscow_temp_alt
    Moscow_temp_final= (Moscow_temp_fahr - 32.0) * 5.0/9.0
    Moscow_alt_meter = Moscow_alt / 3.281
    Moscow_temp_Kelvin = Moscow_temp_final + 273.15
    b = Moscow_temp_Kelvin[["temp"]].apply(pd.to_numeric)
    Moscow_pres_final=a*np.exp((-9.80665*0.0289644*Moscow_alt_meter)/(8.31432*b))
    
    c=Minsk_pres.iloc[[Minsk_hour]].to_numpy()
    
    Minsk_temp_fahr = (Minsk_temp.iloc[[Minsk_hour]] * 9.0/5.0) + 32.0
    Minsk_temp_alt=Minsk_alt*0.00356
    Minsk_temp_fahr = Minsk_temp_fahr - Minsk_temp_alt
    Minsk_temp_final= (Minsk_temp_fahr - 32.0) * 5.0/9.0
    Minsk_alt_meter = Minsk_alt / 3.281
    Minsk_temp_Kelvin = Minsk_temp_final + 273.15
    d = Minsk_temp_Kelvin[["temp"]].apply(pd.to_numeric)
    Minsk_pres_final=c*np.exp((-9.80665*0.0289644*Minsk_alt_meter)/(8.31432*d))
    
    e=Berlin_pres.iloc[[Berlin_hour]].to_numpy()
    
    Berlin_temp_fahr = (Berlin_temp.iloc[[Berlin_hour]] * 9.0/5.0) + 32.0
    Berlin_temp_alt=Berlin_alt*0.00356
    Berlin_temp_fahr = Berlin_temp_fahr - Berlin_temp_alt
    Berlin_temp_final= (Berlin_temp_fahr - 32.0) * 5.0/9.0
    Berlin_alt_meter = Berlin_alt / 3.281
    Berlin_temp_Kelvin = Berlin_temp_final + 273.15
    f = Berlin_temp_Kelvin[["temp"]].apply(pd.to_numeric)
    Berlin_pres_final=e*np.exp((-9.80665*0.0289644*Berlin_alt_meter)/(8.31432*f))
    
    g=Colgne_pres.iloc[[Colgne_hour]].to_numpy()
    
    Colgne_temp_fahr = (Colgne_temp.iloc[[Colgne_hour]] * 9.0/5.0) + 32.0
    Colgne_temp_alt=Colgne_alt*0.00356
    Colgne_temp_fahr = Colgne_temp_fahr - Colgne_temp_alt
    Colgne_temp_final= (Colgne_temp_fahr - 32.0) * 5.0/9.0
    Colgne_alt_meter = Colgne_alt / 3.281
    Colgne_temp_Kelvin = Colgne_temp_final + 273.15
    h = Colgne_temp_Kelvin[["temp"]].apply(pd.to_numeric)
    Colgne_pres_final=g*np.exp((-9.80665*0.0289644*Colgne_alt_meter)/(8.31432*h))
    
    i=Lux_pres.iloc[[Lux_hour]].to_numpy()
    
    Lux_temp_fahr = (Lux_temp.iloc[[Lux_hour]] * 9.0/5.0) + 32.0
    Lux_temp_alt=Lux_alt*0.00356
    Lux_temp_fahr = Lux_temp_fahr - Lux_temp_alt
    Lux_temp_final= (Lux_temp_fahr - 32.0) * 5.0/9.0
    Lux_alt_meter = Lux_alt / 3.281
    Lux_temp_Kelvin = Lux_temp_final + 273.15
    j = Lux_temp_Kelvin[["temp"]].apply(pd.to_numeric)
    Lux_pres_final=i*np.exp((-9.80665*0.0289644*Lux_alt_meter)/(8.31432*j))
    
    k=Reims_pres.iloc[[Reims_hour]].to_numpy()
    
    Reims_temp_fahr = (Reims_temp.iloc[[Reims_hour]] * 9.0/5.0) + 32.0
    Reims_temp_alt=Reims_alt*0.00356
    Reims_temp_fahr = Reims_temp_fahr - Reims_temp_alt
    Reims_temp_final= (Reims_temp_fahr - 32.0) * 5.0/9.0
    Reims_alt_meter = Reims_alt / 3.281
    Reims_temp_Kelvin = Reims_temp_final + 273.15
    l = Reims_temp_Kelvin[["temp"]].apply(pd.to_numeric)
    Reims_pres_final=k*np.exp((-9.80665*0.0289644*Reims_alt_meter)/(8.31432*l))
    
    m=Paris_pres.iloc[[Paris_hour]].to_numpy()
    
    Paris_temp_fahr = (Paris_temp.iloc[[Paris_hour]] * 9.0/5.0) + 32.0
    Paris_temp_alt=Paris_alt*0.00356
    Paris_temp_fahr = Paris_temp_fahr - Moscow_temp_alt
    Paris_temp_final= (Paris_temp_fahr - 32.0) * 5.0/9.0
    Paris_alt_meter = Paris_alt / 3.281
    Paris_temp_Kelvin = Paris_temp_final + 273.15
    n = Paris_temp_Kelvin[["temp"]].apply(pd.to_numeric)
    Paris_pres_final=m*np.exp((-9.80665*0.0289644*Paris_alt_meter)/(8.31432*n))
    
    
    st.header('Appleman Chart')
    df=pd.read_csv('appleman.csv')
    #, ax = plt.subplots(1)
    fig_bol = go.Figure()
    fig_bol.add_trace(go.Scatter(x=df['RH (percent) 0'], y=df['Pressure (hPa)'],
                    mode='lines+markers',
                    name='RH (percent) 0'))
    fig_bol.add_trace(go.Scatter(x=df['RH (percent) 30'], y=df['Pressure (hPa)'],
                    mode='lines',
                    name='RH (percent) 30'))
    fig_bol.add_trace(go.Scatter(x=df['RH (percent) 60'], y=df['Pressure (hPa)'],
                    mode='lines+markers',
                    name='RH (percent) 60',marker=dict(symbol='triangle-up')))
    fig_bol.add_trace(go.Scatter(x=df['RH (percent) 90'], y=df['Pressure (hPa)'],
                    mode='lines',
                    name='RH (percent) 90'))
    fig_bol.add_trace(go.Scatter(x=df['RH (percent) 100'], y=df['Pressure (hPa)'],
                    mode='lines+markers',
                    name='RH (percent) 100'))
    fig_bol.add_trace(go.Scatter(x=Moscow_temp_final['temp'], y=Moscow_pres_final['temp'],
                    mode='markers',
                    name='Moscow_Contrail',marker=dict(size=15))) 
    fig_bol.add_trace(go.Scatter(x=Minsk_temp_final['temp'], y=Minsk_pres_final['temp'],
                    mode='markers',
                    name='Minsk_Contrail',marker=dict(size=15))) 
    fig_bol.add_trace(go.Scatter(x=Berlin_temp_final['temp'], y=Berlin_pres_final['temp'],
                    mode='markers',
                    name='Berlin_Contrail',marker=dict(size=15))) 
    fig_bol.add_trace(go.Scatter(x=Colgne_temp_final['temp'], y=Colgne_pres_final['temp'],
                    mode='markers',
                    name='Colgne_Contrail',marker=dict(size=15))) 
    fig_bol.add_trace(go.Scatter(x=Lux_temp_final['temp'], y=Lux_pres_final['temp'],
                    mode='markers',
                    name='Lux_Contrail',marker=dict(size=15))) 
    fig_bol.add_trace(go.Scatter(x=Reims_temp_final['temp'], y=Reims_pres_final['temp'],
                    mode='markers',
                    name='Reims_Contrail',marker=dict(size=15))) 
    fig_bol.add_trace(go.Scatter(x=Paris_temp_final['temp'], y=Paris_pres_final['temp'],
                    mode='markers',
                    name='Paris_Contrail',marker=dict(size=15))) 
    fig_bol.update_xaxes(title_text = "Temperature(*C)",title_font = {"size": 20},title_standoff = 25)
    fig_bol.update_yaxes(title_text = "Pressure(hPa)",title_font = {"size": 20},title_standoff = 25)
    fig_bol.update_layout(height=500,width=1500,yaxis_range=[1000,0])
    st.plotly_chart(fig_bol)
    