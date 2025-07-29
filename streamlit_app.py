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

# --- INÍCIO DO CÓDIGO CSS ---
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

    /* >>> COR DO TEXTO DOS LINKS DA BARRA LATERAL PARA PRETO <<< */
    /* Este seletor visa os links de navegação gerados pelo Streamlit na sidebar */
    .st-emotion-cache-10o4u2c a { /* Esta classe pode variar entre versões do Streamlit */
        color: black !important;
    }
    /* Se o seletor acima não funcionar, tente também: */
    .st-emotion-cache-1l00yvg a { /* Outra classe comum para links na sidebar */
        color: black !important;
    }

    /* Regra para a linha horizontal (HR) na sidebar */
    .stSidebar hr { /* Seleciona a tag <hr> dentro da sidebar */
        border-top: 1px solid black; /* Define a cor da borda superior para preto */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# --- FIM DO CÓDIGO CSS ---


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
    add_logo() # Sua logo aparece aqui
    st.write("---") # Linha separadora abaixo da logo (agora com CSS para ser preta)
# Conteúdo da sua página inicial (Home)
st.write("# **Plataforma CNI-Internacional!**")
st.write("Use a barra lateral para navegar entre os painéis.")

# ... o restante do seu código da página inicial, se houver ...