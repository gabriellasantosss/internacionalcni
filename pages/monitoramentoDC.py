import streamlit as st

# Define o título da página no navegador
st.set_page_config(page_title="Meu Primeiro Dashboard")

# Opcional: Reaplicar o CSS da sua página principal se quiser que esta nova página
# tenha o mesmo estilo de fundo e cores de texto. Se não incluir,
# ela usará o tema padrão do Streamlit ou o configurado em .streamlit/config.toml.
st.markdown(
    """
    <style>
    .stApp { background-color: white; color: black; }
    .stSidebar { background-color: #DDDDDD; color: black; }
    header { background-color: #DDDDDD !important; color: black !important; }
    header * { color: black !important; }
    h1, h2, h3, h4, h5, h6 { color: black; }
    p, li, div, span { color: black; }
    a { color: black; }
    /* Se você removeu o alinhamento à esquerda, não inclua as regras block-container aqui */
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Meu Primeiro Dashboard")
st.write("Bem-vindo à sua nova página de dashboard!")
st.write("Aqui você pode adicionar gráficos, tabelas, e outros elementos do Streamlit.")

# Exemplo:
st.line_chart([1, 5, 2, 6, 3])
