import streamlit as st
from PIL import Image
import pandas as pd


def app():
    

    portada = Image.open("images/pepa3.jpg")
    st.sidebar.image("images/themain.png", use_column_width=True)

    st.image(portada, use_column_width=True)

    st.write("""
    # ¿Por qué?
    ## * Perrinder, * dale una chance al perrete 
    Son muchos los perros que sufren abandono a lo largo del año, por eso, para garantizar el éxito de la relación con su nueva familia, hemos desarrollado el  * Perrinder *

 


    """)