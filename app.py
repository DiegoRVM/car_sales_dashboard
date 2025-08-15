import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Anúncios de carros')

@st.cache_data
def load_data():
    return pd.read_csv('vehicles.csv')

car_data = load_data()

st.sidebar.header('Configure sua Busca')

filter_options = {
    'Modelo': 'model',
    'Condição': 'condition',
    'Combustível': 'fuel',
    'Tipo': 'type'
}

filter_type_selection = st.sidebar.selectbox(
    'Selecione o filtro',
    list(filter_options.keys())
)

selected_column = filter_options[filter_type_selection]

all_values = sorted(car_data[selected_column].unique())
value_selection = st.sidebar.selectbox(f'Selecione o {filter_type_selection.lower()}', all_values)

min_price, max_price = int(car_data['price'].min()), int(car_data['price'].max())
price_range_selection = st.sidebar.slider(
    'Selecione o intervalo de preço',
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price),
    format='$%d'
)

filtered_data = car_data[
    (car_data[selected_column] == value_selection) &
    (car_data['price'] >= price_range_selection[0]) &
    (car_data['price'] <= price_range_selection[1])
]

st.sidebar.markdown('---')
st.sidebar.header('Selecione os gráficos')

hist_checkbox = st.sidebar.checkbox('Quilometragem')
scatter_checkbox = st.sidebar.checkbox('Gráfico de dispersão de preço x quilometragem')
bar_chart_checkbox = st.sidebar.checkbox('Gráfico de barras de preço por condição')

if hist_checkbox:
    st.subheader(f'Distribuição de Quilometragem para {value_selection}')
    st.write(f'Histograma para quilometragem para {value_selection}...')
    
    fig_hist = px.histogram(filtered_data, x="odometer")
    
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_checkbox:
    st.subheader(f'Preço vs. Quilometragem para {value_selection}')
    st.write(f'Criando um gráfico de dispersão entre preço e quilometragem para {value_selection}...')
    
    fig_scatter = px.scatter(filtered_data, x="odometer", y="price")
    
    st.plotly_chart(fig_scatter, use_container_width=True)

if bar_chart_checkbox:
    st.subheader(f'Preço médio por Condição do Veículo para {value_selection}')
    st.write(f'Criando um gráfico de barras de preço por condição para {value_selection}...')
    
    avg_price_by_condition = filtered_data.groupby('condition')['price'].mean().reset_index()
    
    fig_bar = px.bar(avg_price_by_condition, x='condition', y='price', 
                     title=f'Preço Médio por Condição do Veículo ({value_selection})')
    
    st.plotly_chart(fig_bar, use_container_width=True)