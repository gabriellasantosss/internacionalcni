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

# --- INÍCIO DO CÓDIGO CSS MAIS ABRANGENTE ---
st.markdown(
    """
    <style>
    /* Define o fundo da área principal da aplicação como branco e texto padrão preto */
    .stApp {
        background-color: white;
        color: black; /* Define a cor padrão do texto para preto */
    }

    /* Define o fundo da barra lateral como CINZA e texto preto */
    .stSidebar {
        background-color: #DDDDDD; /* Cor cinza para a barra lateral */
        color: black; /* Define a cor do texto na barra lateral para preto */
    }

    /* >>> NOVO: Personaliza a BARRA SUPERIOR FIXA para ser BRANCA <<< */
    /* Tentativa de sobrescrever o fundo do cabeçalho */
    header {
        background-color: #DDDDDD !important; /* Força o fundo branco para o elemento <header> */
    }

    /* Pode ser necessário forçar o texto no cabeçalho também, se houver */
    header * { /* Aplica a todos os elementos dentro do cabeçalho */
        color: black !important; /* Força a cor do texto para preto */
    }

    /* Se a logo do Streamlit na barra superior ainda aparecer escura, podemos tentar esconder */
    /* .st-emotion-cache-l9b3z5 { /* Exemplo de classe para o logo Streamlit */
    /* visibility: hidden; */
    /* } */


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
    </style>
    """,
    unsafe_allow_html=True
)
# --- FIM DO CÓDIGO CSS MAIS ABRANGENTE ---


# Função logo CNI
def add_logo():
    st.image(
        "https://staticportaldaindustria.azureedge.net/static/img/logos/atualizado/cni.svg",
        width=280,
    )

# Este bloco HTML/JavaScript que você adicionou.
# Se a logo da CNI (do portal) está aparecendo na barra superior e você não quer,
# é possível que este script ou outro elemento a esteja colocando lá.
# O script abaixo tenta ajustar o estilo de uma imagem específica.
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

with st.sidebar: # Isso cria um bloco na barra lateral
    add_logo() # CHAMANDO A FUNÇÃO AQUI PARA EXIBIR A LOGO NA BARRA LATERAL
    # Você pode adicionar outros elementos aqui que queira na barra lateral
    st.write("---") # Para adicionar uma linha separadora, por exemplo
    # Ex: st.markdown(""" **☝️ Selecione acima um dos dashboards disponíveis para começar!** """)

st.write("# **Inteligência Comercial 📊**")

# ... o restante do seu código (se houver, adicione aqui abaixo) ...