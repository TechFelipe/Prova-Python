import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import openpyxl as op

st.set_page_config(
    page_title="Afazeres Domésticos - PNAD",
    page_icon="📊",
    layout="wide"
)

st.title("🚗 Veiculos Minas Gerais")


# =====================================================
# UPLOAD
# =====================================================

arquivo = st.file_uploader("Faça o upload do arquivo CSV:", type=["csv"])

arquivo = r"numero_veiculos.csv"

if arquivo is None:
    st.warning("Erro ao carregar o arquivo. Por favor, faça o upload do arquivo CSV.")
    st.stop()

# =====================================================
# LEITURA DOS DADOS
# =====================================================

bruto = pd.read_csv(
    arquivo
)

print(bruto.columns)  # Debugging step to inspect column names

indicador_1 = bruto.iloc[8:41].copy()

# Adjust the column renaming to match the number of columns
indicador_1.columns = [
    "ano",
    "mes",
    "sigla_uf",
    "id_municipio", 
    "id_municipio_nome",
    "tipo_veiculo",
    "quantidade"
]  # Replace with actual column names if known

indicador_1 = indicador_1.reset_index(drop=True)

for col in indicador_1.columns[1:]:
    indicador_1[col] = pd.to_numeric(
        indicador_1[col],
        errors="coerce"
    )

# Ano manual (altere conforme necessário)
indicador_1["ano"] = 2025


indicador_1 = indicador_1.reset_index(drop=True)

for col in indicador_1.columns[1:]:
    indicador_1[col] = pd.to_numeric(
        indicador_1[col],
        errors="coerce"
    )


# =====================================================
# FILTROS
# =====================================================

st.header("Filtros")



# Ensure default values exist in the options
cidades = indicador_1["id_municipio_nome"].unique()
municipios = [i for i in ["Belo Horizonte", "Contagem", "Betim"] if i in cidades]

cidades = st.multiselect(
    "Municipios / Cidades",
    cidades,
    default=municipios
)

dados = indicador_1[
    indicador_1["id_municipio_nome"].isin(cidades)
]