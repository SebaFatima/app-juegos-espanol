import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="Generador de Juegos Español",
    page_icon="🎲",
    layout="wide"
)

# Encabezado principal
st.title("🎯 Generador de Juegos para Clase de Español")

st.markdown(
    """
    Bienvenida maestra 👩‍🏫  
    Esta herramienta te permitirá generar tres tipos de juegos educativos:
    
    - 🁢 Dominó: unir palabra con su dibujo
    - ➰ Unir con línea: conectar palabra e imagen
    - 🃏 Memorama: encuentra las parejas

    Selecciona un juego en el menú lateral para comenzar.
    """
)
