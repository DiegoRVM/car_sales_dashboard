import streamlit as st
import pandas as pd
import plotly.express as px

# Título do dashboard
st.header('Dashboard de anúncios de carros')

# Carregar os dados
car_data = pd.read_csv('vehicles.csv')

# Criar a caixa de seleção
hist_button = st.button('Criar histograma de quilometragem')

# Lógica para o botão
if hist_button:
    # Escrever uma mensagem de sucesso
    st.write('Criando um histograma para a coluna de quilometragem')
    
    # Criar o histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Exibir o gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)

# Adicionar uma caixa de seleção
scatter_button = st.button('Criar gráfico de dispersão de preço x quilometragem')

# Lógica para o segundo botão
if scatter_button:
    # Escrever uma mensagem de sucesso
    st.write('Criando um gráfico de dispersão entre preço e quilometragem')
    
    # Criar o gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Exibir o gráfico Plotly
    st.plotly_chart(fig_scatter, use_container_width=True)