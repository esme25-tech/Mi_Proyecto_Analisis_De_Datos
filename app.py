import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt

ruta = os.path.join(os.path.dirname(__file__), "YARDAS_PASOS_DATOS_TICS.xlsx")
df = pd.read_excel(ruta, index_col=0)

st.header("Primeras 5 columnas")
st.dataframe(df.head())

st.header("Estadistica Descriptiva")
st.dataframe(df.describe())

df.columns = [c.lower().replace(' ', '_') for c in df.columns]

col1, col2 =st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.boxplot(df['pases_completos'])
    st.header("Diagrama de caja y bigote\n de pases completos")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.boxplot(df['yardas_totales'])
    st.header("Diagrama de caja y bigote\n de yardas totales")
    st.pyplot(fig)      