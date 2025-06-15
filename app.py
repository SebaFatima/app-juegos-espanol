import streamlit as st
import pandas as pd
import random


# ===================== FUNCIONES =====================


def mostrar_ficha(imagen, palabra, orientacion):
    if orientacion == "horizontal":
        st.markdown(
            f"""
            <div style='
                border: 3px solid black; 
                border-radius: 10px; 
                width: 300px; 
                height: 150px; 
                background-color: white; 
                display: flex; 
                justify-content: center;
                align-items: center;
                margin: auto;
                overflow: hidden;
            '>
                <div style='width: 50%; height: 100%; display: flex; align-items: center; justify-content: center;'>
                    <img src="{imagen}" style='max-width: 100%; max-height: 90%;'>
                </div>
                <div style='width: 50%; height: 100%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 20px; text-align: center; padding: 10px;'>
                    {palabra.capitalize()}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style='
                border: 3px solid black; 
                border-radius: 10px; 
                width: 150px; 
                height: 300px; 
                background-color: white; 
                display: flex; 
                flex-direction: column; 
                justify-content: center;
                align-items: center;
                margin: auto;
                overflow: hidden;
            '>
                <div style='height: 50%; display: flex; align-items: center; justify-content: center;'>
                    <img src="{imagen}" style='max-height: 90%; max-width: 90%;'>
                </div>
                <div style='height: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 20px; text-align: center; padding: 10px;'>
                    {palabra.capitalize()}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def mostrar_fichas(fichas):
    for i in range(0, len(fichas), 2):
        cols = st.columns(2, gap="large")
        for j in range(2):
            if i + j < len(fichas):
                ficha = fichas[i + j]
                with cols[j]:
                    mostrar_ficha(
                        ficha["imagen"], ficha["palabra"], ficha["orientacion"]
                    )


# ===================== PÁGINA =====================

st.set_page_config(
    page_title="Generador de Juegos Español", page_icon="🎯", layout="wide"
)
st.title("🎯 Generador de Juegos para Clase de Español")


@st.cache_data
def cargar_catalogo():
    return pd.read_csv("data/catalogo.csv")


catalogo = cargar_catalogo()


# ===================== APP =====================

juego = st.sidebar.selectbox(
    "Selecciona el tipo de juego", ["Dominó", "Unir con líneas", "Memorama"]
)

if juego == "Dominó":
    st.header("👢 Generador de Dominó palabra-imagen")

    temas = catalogo["tema"].unique()
    temas_seleccionados = st.multiselect(
        "Elige uno o más temas", options=sorted(temas.tolist()), default=temas[:1]
    )

    numero_fichas = st.slider(
        "Número de fichas a generar", min_value=4, max_value=20, value=6, step=2
    )

    if st.button("Generar dominó"):
        seleccion = catalogo[catalogo["tema"].isin(temas_seleccionados)].copy()

        if len(seleccion["palabra"].unique()) < numero_fichas:
            st.warning("No hay suficientes palabras únicas para generar tantas fichas.")
        else:
            palabras = random.sample(
                list(seleccion["palabra"].unique()), k=numero_fichas
            )

            fichas = []
            for i in range(numero_fichas):
                palabra = palabras[i]
                imagen_path = seleccion[seleccion["palabra"] == palabra][
                    "path_imagen"
                ].values[0]
                orientacion = "horizontal" if i % 2 == 0 else "vertical"
                fichas.append(
                    {
                        "palabra": palabra,
                        "imagen": imagen_path,
                        "orientacion": orientacion,
                    }
                )

            st.subheader("Fichas generadas:")
            mostrar_fichas(fichas)

elif juego == "Unir con líneas":
    st.header("Unir con líneas (pendiente)")

elif juego == "Memorama":
    st.header("Memorama (pendiente)")
