import streamlit as st
import pandas as pd

# Configuração inicial da interface
st.title("Modelo Hipotético-Dedutivo no Xadrez")
st.write("Preencha as etapas do método para organizar suas jogadas e estratégias.")

# Inicialização da tabela de dados
if "mhd_data" not in st.session_state:
    st.session_state.mhd_data = pd.DataFrame(columns=["Etapa", "Descrição"])

# Perguntas norteadoras para cada etapa
perguntas = {
    "Base Teórica": "Qual é a base de conhecimento ou estratégia que será usada como referência?",
    "Hipótese": "O que você espera alcançar com uma jogada ou sequência de jogadas?",
    "Consequências": "Quais reações ou respostas você espera do adversário?",
    "Experimento": "Qual jogada ou sequência será aplicada para testar sua hipótese?",
    "Observações": "O que aconteceu após a jogada? O resultado foi o esperado?",
    "Avaliação": "A hipótese inicial foi confirmada, ajustada ou refutada? Por quê?"
}

# Formulário para entrada dos dados
with st.form("mhd_form"):
    etapa = st.selectbox("Selecione a Etapa", list(perguntas.keys()))
    descricao = st.text_area("Responda:", perguntas[etapa], height=100)
    submitted = st.form_submit_button("Adicionar Etapa")

    if submitted:
        nova_entrada = pd.DataFrame({"Etapa": [etapa], "Descrição": [descricao]})
        st.session_state.mhd_data = pd.concat([st.session_state.mhd_data, nova_entrada], ignore_index=True)
        st.success(f"Etapa '{etapa}' adicionada com sucesso!")

# Exibição da tabela dinâmica
st.subheader("Tabela do Modelo Hipotético-Dedutivo")
st.table(st.session_state.mhd_data)

# Opção para limpar a tabela
if st.button("Limpar Tabela"):
    st.session_state.mhd_data = pd.DataFrame(columns=["Etapa", "Descrição"])
    st.success("Tabela limpa com sucesso!")

# Exportar a tabela para CSV
st.download_button(
    label="Baixar Tabela como CSV",
    data=st.session_state.mhd_data.to_csv(index=False),
    file_name="mhd_xadrez.csv",
    mime="text/csv"
)
