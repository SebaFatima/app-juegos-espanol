import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Generador de Juegos Español",
    page_icon="🎲",
    layout="wide"
)

st.title("🎯 Generador de Juegos para Clase de Español")

# Cargar datos
@st.cache_data
def cargar_catalogo():
    return pd.read_csv("data/catalogo.csv")

catalogo = cargar_catalogo()

# Menú de navegación
juego = st.sidebar.selectbox(
    "Selecciona el tipo de juego",
    ["Dominó", "Unir con líneas", "Memorama"]
)

if juego == "Dominó":
    st.header("🁢 Generador de Dominó palabra-imagen")
    st.markdown("Configura las opciones del juego y genera las fichas.")

    # Opciones
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
        step=2  # par para que se pueda encadenar bien
    )

    if st.button("Generar dominó"):
        st.info("Aquí va a aparecer el layout de las fichas (todavía no está implementado).")

elif juego == "Unir con líneas":
    st.header("➰ Generador de juego: Unir con líneas (pendiente)")
elif juego == "Memorama":
    st.header("🃏 Generador de Memorama (pendiente)")
