# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st

st.set_page_config(page_title=f"cni-internacional")

from utils import style_fragment

with st.sidebar:
    style_fragment()

from func import check_password


st.write("# **Inteligência Comercial 📊**")




