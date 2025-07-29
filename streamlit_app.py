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

# --- INÍCIO DO CÓDIGO CSS ---
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

    /* >>> Adição para personalizar a BARRA SUPERIOR FIXA <<< */
    /* Esta classe pode mudar em futuras versões do Streamlit. */
    /* Ela controla o cabeçalho superior onde estão "Share", ícones, etc. */
    .st-emotion-cache-zt5ig8 {
        background-color: #F0F2F6; /* Um cinza muito claro para o topo (quase branco) */
        color: black; /* Garante que o texto (se houver) no topo seja preto */
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
# --- FIM DO CÓDIGO CSS ---


# Função logo CNI
def add_logo():
    st.image(
        "https://staticportaldaindustria.azureedge.net/static/img/logos/atualizado/cni.svg",
        width=280,
    )

# Este bloco HTML/JavaScript é o que você adicionou.
# Ele tenta manipular uma imagem com um SRC específico.
# Se a logo da CNI (do portal) está aparecendo na barra superior,
# pode ser devido a isso ou a algum outro estilo global que você já tinha.
html(
    """
    <script>
        var imgSrc = "https://staticportaldaindustria.azureedge.net/static/img/logos/novas/cni.svg";
        var imgElem = window.parent.document.querySelector(`img[src="${imgSrc}"]`);
        if (imgElem) { /* Adicionado verificação para garantir que o elemento exista */
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
    # Se você tinha algum outro texto ou elemento na sidebar, adicione aqui.
    # Ex: st.markdown(""" **☝️ Selecione acima um dos dashboards disponíveis para começar!** """)

st.write("# **Inteligência Comercial 📊**")

# ... o restante do seu código (se houver, adicione aqui abaixo) ...