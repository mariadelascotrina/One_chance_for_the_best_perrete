import streamlit as st
from PIL import Image

def app():
    st.write("""
    # El proceso de análisis que hemos seguido

    1. Webb Scraping & limpieza
    2. Clusterización
    3. Elección de criterios para la recomendación
    """)

    
    st.write("""
    ### 1. Scraping con calma
    """)
    sc = Image.open("images/scraping.png")
    st.image(sc, use_column_width=True)
    st.write("""
    Nos descargamos las características de cada uno de los perretes y después limpiamos y profundizamos los datos. Creamos categorías como "Comportamiento", "Características físicas" o "Capacidad de adaptación" para segregar la información.
    """)
    


    

    st.write("""
    ### 2. La clusterización no fue fácil
    """)
    cluster = Image.open("images/clusters_2.png")
    st.image(cluster, use_column_width=True)
    st.write("""
    Tras varios intentos, la mejor silueta de la obteníamos con 3 clusters (habiendo hecho PCA).
    """)




    st.write("""
    ### 3. Los criterios finales para hacer nuestro filtro
    """) 
    grafico = Image.open("images/criterios_elegidos.png")
    st.image(grafico, use_column_width=True)
    st.write("""
    Finalmente, detectamos aquellos criterios esenciales para asegurar el éxito de la convivencia con su nueva familia familia.
    """)




    
    