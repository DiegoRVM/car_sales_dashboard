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

# Opções de filtro para o selectbox
filter_options = {
    'Modelo': 'model',
    'Condição': 'condition',
    'Combustível': 'fuel',
    'Tipo': 'type'
}

# Primeira caixa de seleção para escolher o tipo de filtro (ex: 'Modelo')
filter_type_selection = st.sidebar.selectbox(
    'Selecione o tipo de filtro',
    list(filter_options.keys())
)

# Obter o nome da coluna do DataFrame com base na escolha do usuário
selected_column = filter_options[filter_type_selection]

# Segunda caixa de seleção, preenchida com os valores únicos da coluna selecionada
all_values = sorted(car_data[selected_column].unique())
value_selection = st.sidebar.selectbox(f'Selecione o {filter_type_selection.lower()}', all_values)

# Filtrar os dados com base na seleção do usuário
filtered_data = car_data[car_data[selected_column] == value_selection]

# Adicionar as caixas de seleção para os gráficos na barra lateral
st.sidebar.markdown('---')
st.sidebar.header('Selecione os gráficos')

hist_checkbox = st.sidebar.checkbox('Criar histograma de quilometragem')
scatter_checkbox = st.sidebar.checkbox('Criar gráfico de dispersão de preço x quilometragem')
bar_chart_checkbox = st.sidebar.checkbox('Criar gráfico de barras de preço por condição')

# Lógica para as caixas de seleção
if hist_checkbox:
    st.subheader(f'Distribuição de Quilometragem para {value_selection}')
    st.write(f'Criando um histograma para a coluna de quilometragem para {value_selection}...')
    
    # Criar o histograma com os dados filtrados
    fig_hist = px.histogram(filtered_data, x="odometer")
    
    # Exibir o gráfico Plotly
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_checkbox:
    st.subheader(f'Preço vs. Quilometragem para {value_selection}')
    st.write(f'Criando um gráfico de dispersão entre preço e quilometragem para {value_selection}...')
    
    # Criar o gráfico de dispersão com os dados filtrados
    fig_scatter = px.scatter(filtered_data, x="odometer", y="price")
    
    # Exibir o gráfico Plotly
    st.plotly_chart(fig_scatter, use_container_width=True)

if bar_chart_checkbox:
    st.subheader(f'Preço médio por Condição do Veículo para {value_selection}')
    st.write(f'Criando um gráfico de barras de preço por condição para {value_selection}...')
    
    # Agrupar os dados filtrados por condição e calcular o preço médio
    avg_price_by_condition = filtered_data.groupby('condition')['price'].mean().reset_index()
    
    # Criar o gráfico de barras
    fig_bar = px.bar(avg_price_by_condition, x='condition', y='price', 
                     title=f'Preço Médio por Condição do Veículo ({value_selection})')
    
    # Exibir o gráfico Plotly
    st.plotly_chart(fig_bar, use_container_width=True)