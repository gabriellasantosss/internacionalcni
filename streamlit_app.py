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

st.set_page_config(page_title=f"cni-internacional")

# --- INÍCIO DO CÓDIGO PARA DEIXAR TUDO BRANCO E TEXTO PRETO ---
st.markdown(
    """
    <style>
    /* Define o fundo de toda a aplicação Streamlit como branco e texto padrão preto */
    .stApp {
        background-color: white;
        color: black; /* Define a cor padrão do texto para preto */
    }

    /* Define o fundo da barra lateral como branco */
    .stSidebar {
        background-color: white;
        color: black; /* Define a cor do texto na barra lateral para preto */
    }

    /* Garante que os títulos (h1-h6) sejam pretos */
    h1, h2, h3, h4, h5, h6 {
        color: black;
    }

    /* Garante que os parágrafos, listas, divs e spans sejam pretos */
    p, li, div, span {
        color: black;
    }

    /* Garante que os links também sejam pretos (opcional, pode querer uma cor diferente para links) */
    a {
        color: black; /* Ou uma cor escura que se destaque, como #0000CC */
    }

    /* Se houver elementos específicos (como botões, expanders) que não fiquem pretos
       no texto, pode ser necessário adicionar regras mais específicas aqui. */
    </style>
    """,
    unsafe_allow_html=True
)
# --- FIM DO CÓDIGO PARA DEIXAR TUDO BRANCO E TEXTO PRETO ---


# Função logo CNI
def add_logo():
    st.image(
        "https://staticportaldaindustria.azureedge.net/static/img/logos/atualizado/cni.svg",
        width=280,
    )

with st.sidebar: # Isso cria um bloco na barra lateral
    add_logo() # CHAMANDO A FUNÇÃO AQUI PARA EXIBIR A LOGO NA BARRA LATERAL
    # Você pode adicionar outros elementos aqui que queira na barra lateral
    st.write("---") # Para adicionar uma linha separadora, por exemplo
    # Se você tinha algum outro texto ou elemento na sidebar, adicione aqui.
    # Ex: st.markdown(""" **☝️ Selecione acima um dos dashboards disponíveis para começar!** """)

st.write("# **Inteligência Comercial 📊**")

# ... o restante do seu código (se houver, adicione aqui abaixo) ...

