import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# URL da API de ataques
API_URL = "http://localhost/blog_guardiao/public/api/logs_ataques?token=meuTokenSegur0"

# Título
st.set_page_config(page_title="Painel de Ataques - Guardião", layout="wide")
st.title("🛡️ Painel de Monitoramento de Ataques - Guardião")

# Função para buscar os dados
@st.cache_data(ttl=60)
def carregar_dados():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        dados = response.json()
        df = pd.DataFrame(dados)
        df['data'] = pd.to_datetime(df['data'])
        return df
    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
        return pd.DataFrame()

# Carregar os dados
df = carregar_dados()

if df.empty:
    st.warning("Nenhum ataque registrado.")
else:
    col1, col2 = st.columns(2)

    # Gráfico de tipos de ataques
    with col1:
        st.subheader("📊 Tipos de Ataques Detectados")
        tipo_counts = df['tipo'].value_counts()
        st.bar_chart(tipo_counts)

    # Gráfico de IPs mais ativos
    with col2:
        st.subheader("🌐 IPs com mais tentativas")
        ip_counts = df['ip'].value_counts().head(10)
        st.bar_chart(ip_counts)

    # Linha do tempo
    st.subheader("🕒 Linha do Tempo de Ataques")
    timeline = df.set_index('data').resample('H').size()
    st.line_chart(timeline)

    # Tabela de últimos ataques
    st.subheader("📄 Últimos 10 ataques registrados")
    st.dataframe(df.sort_values(by="data", ascending=False).head(10))
