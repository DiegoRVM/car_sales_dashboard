import streamlit as st
import pandas as pd
import plotly.express as px

# Título do dashboard
st.header('Dashboard de anúncios de carros')

# Carregar os dados
# O Streamlit recomenda o uso de st.cache para carregar dados pesados apenas uma vez.
@st.cache_data
def load_data():
    return pd.read_csv('vehicles.csv')

car_data = load_data()

# Adicionar a barra lateral para opções de gráficos
st.sidebar.header('Opções de gráficos')

# Criar as caixas de seleção na barra lateral
hist_checkbox = st.sidebar.checkbox('Criar histograma de quilometragem')
scatter_checkbox = st.sidebar.checkbox('Criar gráfico de dispersão de preço x quilometragem')

# Lógica para as caixas de seleção
if hist_checkbox:
    st.subheader('Distribuição de Quilometragem')
    st.write('Criando um histograma para a coluna de quilometragem...')
    
    # Criar o histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Exibir o gráfico Plotly
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_checkbox:
    st.subheader('Preço vs. Quilometragem')
    st.write('Criando um gráfico de dispersão entre preço e quilometragem...')
    
    # Criar o gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Exibir o gráfico Plotly
    st.plotly_chart(fig_scatter, use_container_width=True)
