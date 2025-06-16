import random
import os


def generar_domino(catalogo, temas, cantidad):
    # Filtra el catálogo por los temas seleccionados
    seleccion = catalogo[catalogo["tema"].isin(temas)]

    # Elige al azar palabras únicas suficientes para generar la secuencia
    palabras = seleccion["palabra"].unique().tolist()
    random.shuffle(palabras)

    if len(palabras) < cantidad:
        return None  # No hay suficientes palabras

    palabras = palabras[:cantidad]

    fichas = []
    for i in range(cantidad - 1):
        ficha = {}
        ficha["palabra_a"] = palabras[i]
        ficha["palabra_b"] = palabras[i + 1]

        ficha["imagen_a"] = seleccion[seleccion["palabra"] == ficha["palabra_a"]][
            "imagen"
        ].values[0]
        ficha["orientacion"] = "horizontal" if i % 2 == 0 else "vertical"

        fichas.append(ficha)

    return fichas
