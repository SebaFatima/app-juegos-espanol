import streamlit as st
import pandas as pd
import random
import base64  # Necesario para convertir imágenes a base64

# ===================== FUNCIONES =====================


# Convierte una imagen local en una cadena base64 para insertar en HTML
def imagen_a_base64(path_imagen):
    with open(path_imagen, "rb") as img_file:
        data = img_file.read()
    return base64.b64encode(data).decode()


# Dibuja una ficha individual con imagen + texto incrustados dentro del borde
def mostrar_ficha_dominio(imagen_path, texto, orientacion):
    imagen_base64 = imagen_a_base64(imagen_path)
    img_tag = f"<img src='data:image/png;base64,{imagen_base64}' style='max-height: 90%; max-width: 90%;'/>"

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
                flex-direction: row;
                overflow: hidden;
                margin: auto;
            '>
                <div style='width: 50%; display: flex; align-items: center; justify-content: center;'>
                    {img_tag}
                </div>
                <div style='width: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: bold;'>
                    {texto.capitalize()}
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
                overflow: hidden;
                margin: auto;
            '>
                <div style='height: 50%; display: flex; align-items: center; justify-content: center;'>
                    {img_tag}
                </div>
                <div style='height: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: bold;'>
                    {texto.capitalize()}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# Muestra las fichas de 2 en 2 en pantalla
def mostrar_fichas_encadenadas(fichas):
    for i in range(0, len(fichas), 2):
        cols = st.columns(2, gap="large")
        for j in range(2):
            if i + j < len(fichas):
                ficha = fichas[i + j]
                with cols[j]:
                    mostrar_ficha_dominio(
                        ficha["imagen"], ficha["texto"], ficha["orientacion"]
                    )


# ===================== CONFIGURACIÓN =====================

st.set_page_config(
    page_title="Generador de Juegos Español", page_icon="🎯", layout="wide"
)
st.title("🎯 Generador de Juegos para Clase de Español")

# ===================== CARGA DE DATOS =====================


@st.cache_data
def cargar_catalogo():
    return pd.read_csv("data/catalogo.csv")


catalogo = cargar_catalogo()

# ===================== UI PRINCIPAL =====================

juego = st.sidebar.selectbox(
    "Selecciona el tipo de juego", ["Dominó", "Unir con líneas", "Memorama"]
)

if juego == "Dominó":
    st.header("👢 Generador de Dominó palabra-imagen")

    # Selección de temas
    temas = catalogo["tema"].unique()
    temas_seleccionados = st.multiselect(
        "Elige uno o más temas", options=sorted(temas.tolist()), default=temas[:1]
    )

    # Selector de cantidad de fichas
    numero_fichas = st.slider(
        "Número de fichas a generar", min_value=4, max_value=20, value=6, step=2
    )

    if st.button("Generar dominó"):
        seleccion = catalogo[catalogo["tema"].isin(temas_seleccionados)].copy()

        if len(seleccion["palabra"].unique()) < numero_fichas:
            st.warning("No hay suficientes palabras únicas para generar tantas fichas.")
        else:
            # Elegir palabras únicas al azar
            palabras = random.sample(
                list(seleccion["palabra"].unique()), k=numero_fichas
            )

            # Crear fichas encadenadas: imagen actual → texto siguiente
            fichas = []
            for i in range(numero_fichas - 1):
                palabra_a = palabras[i]
                palabra_b = palabras[i + 1]
                imagen_path = seleccion[seleccion["palabra"] == palabra_a][
                    "path_imagen"
                ].values[0]
                orientacion = "horizontal" if i % 2 == 0 else "vertical"
                fichas.append(
                    {
                        "imagen": imagen_path,
                        "texto": palabra_b,
                        "orientacion": orientacion,
                    }
                )

            # Mostrar fichas
            st.subheader("Fichas generadas:")
            mostrar_fichas_encadenadas(fichas)

elif juego == "Unir con líneas":
    st.header("Unir con líneas (pendiente)")

elif juego == "Memorama":
    st.header("Memorama (pendiente)")
