# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import locale
import altair as alt
from streamlit.components.v1 import html
import json

st.set_page_config(page_title=f"CNI-INTERNACIONAL")

# --- INÍCIO DO CÓDIGO CSS CORRIGIDO E COMPLETO ---
st.markdown(
    """
    <style>
    /* Define o fundo da área principal da aplicação como branco e texto padrão preto */
    .stApp {
        background-color: white;
        color: black;
    }

    /* Define o fundo da barra lateral como CINZA e texto preto */
    .stSidebar {
        background-color: #DDDDDD; /* Cor cinza para a barra lateral */
        color: black;
    }

    /* Personaliza a BARRA SUPERIOR FIXA para ser CINZA, igual à sidebar */
    header {
        background-color: #DDDDDD !important; /* Cor cinza para o cabeçalho, igual à sidebar */
        color: black !important;
    }
    header * {
        color: black !important;
    }

    /* Garante que os títulos (h1-h6) sejam pretos */
    h1, h2, h3, h4, h5, h6 {
        color: black;
    }

    /* Garante que os parágrafos, listas, divs e spans sejam pretos */
    p, li, div, span {
        color: black;
    }

    /* Garante que os links também sejam pretos */
    a {
        color: black;
    }

   """,
    unsafe_allow_html=True # Apenas um unsafe_allow_html=True para todo o bloco
)
# --- FIM DO CÓDIGO CSS CORRIGIDO E COMPLETO ---


# Função logo CNI
def add_logo():
    st.image(
        "https://staticportaldaindustria.azureedge.net/static/img/logos/atualizado/cni.svg",
        width=280,
    )

with st.sidebar:
    add_logo()
    st.write("---")

st.write("# **Inteligência Comercial 🌍**")
# ... o restante do seu código (se houver, adicione aqui abaixo) ...
