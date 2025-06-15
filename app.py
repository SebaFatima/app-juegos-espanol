import streamlit as st
import pandas as pd
from generadores import generar_domino

st.set_page_config(
    page_title="Generador de Juegos Español",
    page_icon="🎲",
    layout="wide"
)

st.title("🎯 Generador de Juegos para Clase de Español")

# Cargar catálogo
@st.cache_data
def cargar_catalogo():
    return pd.read_csv("data/catalogo.csv")

catalogo = cargar_catalogo()

# Menú lateral
juego = st.sidebar.selectbox(
    "Selecciona el tipo de juego",
    ["Dominó", "Unir con líneas", "Memorama"]
)

if juego == "Dominó":
    st.header("🁢 Generador de Dominó palabra-imagen")

    temas = catalogo['tema'].unique()
    temas_seleccionados = st.multiselect(
        "Elige uno o más temas",
        opciones := sorted(temas.tolist()),
        default=opciones[0:1]
    )

    numero_fichas = st.slider(
        "Número de fichas a generar",
        min_value=4,
        max_value=20,
        value=6,
        step=2
    )

    if st.button("Generar dominó"):
        fichas = generar_domino(catalogo, temas_seleccionados, numero_fichas)

        if fichas:
            st.subheader("Fichas generadas:")
            cols = st.columns(len(fichas))
            for i, ficha in enumerate(fichas):
                with cols[i]:
                    st.markdown(f"**{ficha['palabra'].capitalize()}**")
                    st.image(ficha["imagen"], use_column_width=True)

elif juego == "Unir con líneas":
    st.header("➰ Generador de juego: Unir con líneas (pendiente)")

elif juego == "Memorama":
    st.header("🃏 Generador de Memorama (pendiente)")
