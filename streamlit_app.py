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

st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.set_page_config(page_title=f"cni-internacional")

# Função logo CNI
def add_logo():
    st.image(
        "https://staticportaldaindustria.azureedge.net/static/img/logos/atualizado/cni.svg",
        width=280,
    )

with st.sidebar: # Isso cria um bloco na barra lateral
    add_logo() # >>> CHAMANDO A FUNÇÃO AQUI PARA EXIBIR A LOGO NA BARRA LATERAL <<<
    # Você pode adicionar outros elementos aqui que queira na barra lateral
    st.write("---") # Para adicionar uma linha separadora, por exemplo

st.write("# **Inteligência Comercial 📊**")

# ... o restante do seu código ...



