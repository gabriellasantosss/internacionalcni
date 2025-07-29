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

st.set_page_config(page_title=f"CNI-GAE-BI")

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

    /* >>> ALINHA O CONTEÚDO PRINCIPAL À ESQUERDA <<< */
    .block-container {
        padding-left: 1rem; /* Margem à esquerda para o conteúdo */
        padding-right: 1rem; /* Mantém uma pequena margem à direita para não "colar" */
        max-width: 100%; /* Garante que o container ocupe toda a largura disponível */
    }
    .main .block-container {
        margin: 0; /* Remove a margem automática para centralizar */
    }
    </style>
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

html(
    """
    <script>
        var imgSrc = "https://staticportaldaindustria.azureedge.net/static/img/logos/novas/cni.svg";
        var imgElem = window.parent.document.querySelector(`img[src="${imgSrc}"]`);
        if (imgElem) {
            imgElem.style.width = '100%';
            imgElem.style.marginBottom = '-50px';
        }
    </script>
    """,
    width=0,
    height=0,
)

with st.sidebar:
    add_logo()
    st.write("---")

st.write("# **Inteligência Comercial 🌍**")



# ... o restante do seu código (se houver, adicione aqui abaixo) ...