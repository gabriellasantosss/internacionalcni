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
st.write("# **Inteligência Comercial 📊**")

# Função logo CNI
def add_logo():

    st.image(
        "https://staticportaldaindustria.azureedge.net/static/img/logos/atualizado/cni.svg",
        width=280,
    )



