from re import T
import streamlit as st
from multipage import MultiPage
from pages import home
from pages import analysis
from pages import perrinder

app = MultiPage()

app.add_page("¿Por qué?", home.app)
app.add_page("¿Cómo?", analysis.app)
app.add_page("¿Qué?", perrinder.app)

app.run()