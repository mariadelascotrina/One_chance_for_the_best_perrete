from re import T
import streamlit as st
from multipage import MultiPage
from pages import home
from pages import analysis
from pages import perrinder

app = MultiPage()

app.add_page("Index", home.app)
app.add_page("Análisis", analysis.app)
app.add_page("Perrinder", perrinder.app)

app.run()