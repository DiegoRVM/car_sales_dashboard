import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Dashboard de anúncios de carros')

@st.cache_data
def load_data():
    return pd.read_csv('vehicles.csv')

car_data = load_data()

st.sidebar.header('Opções de gráficos')

hist_checkbox = st.sidebar.checkbox('Criar histograma de quilometragem')
scatter_checkbox = st.sidebar.checkbox('Criar gráfico de dispersão de preço x quilometragem')
bar_chart_checkbox = st.sidebar.checkbox('Criar gráfico de barras de preço por condição')

if hist_checkbox:
    st.subheader('Distribuição de Quilometragem')
    st.write('Criando um histograma para a coluna de quilometragem...')
        
    fig_hist = px.histogram(car_data, x="odometer")
        
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_checkbox:
    st.subheader('Preço vs. Quilometragem')
    st.write('Criando um gráfico de dispersão entre preço e quilometragem...')
    
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
        
    st.plotly_chart(fig_scatter, use_container_width=True)

if bar_chart_checkbox:
    st.subheader('Preço médio por Condição do Veículo')
    st.write('Criando um gráfico de barras de preço por condição...')
        
    avg_price_by_condition = car_data.groupby('condition')['price'].mean().reset_index()
        
    fig_bar = px.bar(avg_price_by_condition, x='condition', y='price', 
                     title='Preço Médio por Condição do Veículo')
        
    st.plotly_chart(fig_bar, use_container_width=True)
