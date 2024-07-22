import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

st.title("Laptop Price Predictor")
pipe = pickle.load(open('pipe2.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))
df = pd.DataFrame(df)

Company = st.selectbox('Company', df['Company'].unique())
Type = st.selectbox('Type', df['TypeName'].unique())
Ram = st.selectbox('Ram(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
Weight = st.number_input('Weight')
Touchscreen = st.selectbox('Touchscreen', ['Yes', 'No'])
Ips = st.selectbox('IPS Display', ['Yes', 'No'])
screen_size = st.number_input('Screen Size(Inches)')
Resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
CPU = st.selectbox('CPU', df['Cpu_name'].unique())
hdd = st.number_input('HDD(in GB)')
ssd = st.number_input('SSD(in GB)')
gpu = st.selectbox('GPU', df['Gpu'].unique())
OS = st.selectbox('Operating System', df['OpSys'].unique())

if st.button('Predict Price'):
    X_Res = int(Resolution.split('x')[0])
    Y_Res = int(Resolution.split('x')[1])
    ppi = (((X_Res**2)+(Y_Res**2))**0.5)/screen_size
    if Touchscreen == 'Yes':
        Touchscreen = 1
    else:
        Touchscreen = 0

    if Ips == 'Yes':
        Ips = 1
    else:
        Ips = 0

    query = [[Company, Type, Ram, gpu, OS, Weight, Touchscreen, Ips, ppi, CPU, hdd, ssd]]
    st.subheader("The price of this configuration is predicted to be around:")
    st.subheader(f"INR :red[{str(round(int(np.exp(pipe.predict(query)[0])), -3))}]")



