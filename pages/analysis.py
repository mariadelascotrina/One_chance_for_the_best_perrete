import streamlit as st
from PIL import Image

def app():
    perri = Image.open("images/analisis.jpg")
    st.image(perri, use_column_width=True)

    st.sidebar.image("images/Therojo.png", use_column_width=True)
    st.write("""
    # ¿Cómo?
    ## El proceso de análisis que hemos seguido

    1. Webb Scraping & limpieza
    2. Clusterización
    3. Elección de criterios para la recomendación
    




    
    """)

    ra = Image.open("images/ra.png")
    st.image(ra, use_column_width=True)

    
    st.write("""
    ### 1. Webb Scraping & limpieza
    """)
    sc = Image.open("images/scraping.png")
    st.image(sc, use_column_width=True)
    st.write("""
    Nos descargamos las características de cada uno de los perretes, limpiamos y profundizamos. Creamos categorías como "Características físicas", "Comportamiento", o "Capacidad de adaptación" para segregar la información. 
    Algunas observaciones:
    - Sociabilidad: 
        Están relacionadas altas puntuaciones en: Cariñoso con la familia, Apto para niños, Amigable con los perros, Amigable con los extraños, Potencial para el juego
    - Dos tipos de variables:
        Las que ordenan los datos (Por ejemplo la variable comportamiento, para ordenar nuestros perretes siendo los mejores los que aparecen primero)
        Las que te permiten filtrar los fatos (Perrinder)    """)
    
    ra = Image.open("images/ra.png")
    st.image(ra, use_column_width=True)


    st.write("""
    ### 2. Clusterización     """)
    cluster = Image.open("images/clusters_2.png")
    st.image(cluster, use_column_width=True)
    st.write("""
    Tras varios intentos, la mejor silueta de la obteníamos con 3 clusters (habiendo hecho PCA).
    """)

    ra = Image.open("images/ra.png")
    st.image(ra, use_column_width=True)





    st.write("""
    ### 3. Los criterios finales 
    """) 
    grafico = Image.open("images/criterios_elegidos.png")
    st.image(grafico, use_column_width=True)
    st.write("""
    Finalmente, detectamos aquellos criterios esenciales para asegurar el éxito de la convivencia con su nueva familia familia.
    Los criterios elegidos son aquellas características más diferenciales dentro de cada grupo de características 

    """)




    
    