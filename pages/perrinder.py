import streamlit as st
import pandas as pd
import src.manage_data as dat
from PIL import Image
import requests
from bs4 import BeautifulSoup


def app():

    perri = Image.open("images/perrinder2.png")
    st.image(perri, use_column_width=True)

    st.write("""
   ## Haz *match* con tu perrete
    """)

    data = dat.cargadata()
    data = data.sort_values('Behaviour', ascending = False)

    

    input_size = ["Elige" , "Grande", "Mediano", "Pequeño"]

    size = st.selectbox("¿De qué tamaño te gustaría adoptar tu perro?", input_size)
    if size == "Elige":
        st.stop()
    

    input_alergia = ["Elige", "Sí", "No"]
    alergia  = st.selectbox("¿Eres alérgicx al pelo de perro?", input_alergia)
    if alergia == "Elige":
        st.stop()
    
    input_tiempo  = ["Elige", "Mucho", "Intermedio", "Poco"]
    tiempo = st.selectbox("¿Cuánto tiempo tienes para pasear?", input_tiempo)
    if tiempo == "Elige":
        st.stop()
    
    input_ninos  = ["Elige", "Sí", "No"]
    ninos = st.selectbox("¿Tienes hijos pequeños?", input_ninos)
    if ninos == "Elige":
        st.stop()

    input_perros_otro  = ["Elige", "Sí", "No"]
    perros_otro = st.selectbox("¿Tienes ya otro perro? ", input_perros_otro)
    if perros_otro == "Elige":
            st.stop()

    #formula

    if size == "Grande":
        tamano = [4,5]
    elif size == "Mediano":
        tamano = [3]
    else:
        tamano = [1,2]
    volumen = data[data.Size.isin(tamano)]
    

    if alergia == "Sí":
        pelo = [1,2]
    else: 
        pelo = [1,2,3,4,5]    
    pelete = volumen[volumen['Amount Of Shedding'].isin(pelo)]


    if tiempo == "Mucho":
        horas = [1,2,3,4,5]
    elif tiempo == "Intermedio":
        horas = [1,2,3]
    else:
        horas = [1,2]        
    paseo = pelete[pelete['Exercise Needs'].isin(horas)]
    

    if ninos == "Sí":
        hijo = [4,5]
    else:
        hijo = [1,2,3,4,5]        
    nino = paseo[paseo['Kid-Friendly'].isin(hijo)]
    

    if perros_otro == "Sí":
        otro = [4,5]
    else:
        otro = [1,2,3,4,5]        
    perro = nino[nino['Dog Friendly'].isin(otro)]

    st.write("""
    ## Primeras sugerencias:
    """)
    if len(perro.Name) == 0:
        st.write("""
        No hemos podido encontrar perretes con estas características
        """)
    else:
        
        st.write(f"""
        ###  {str(perro.head(1).Name.unique())[2:-2]}  


          
        """) 

        st.dataframe(perro.head(4).Name)
        
        

        st.write(f"""
        Tu match especial, el {str(perro.head(1).Name.unique())[2:-2]} se define por estas características: 
        """) 

        #formular perro
        nombre = str(perro.head(1).Name.unique())[2:-2]
        url = f"https://www.google.com/search?q={nombre}+dog+*.jpg&tbm=isch&ved=2ahUKEwi2kIjl0uX0AhXG0YUKHVPECi8Q2-cCegQIABAA&oq={nombre}+*.jpg&gs_lcp=CgNpbWcQAzIECAAQHjoHCAAQsQMQQzoECAAQQzoICAAQgAQQsQM6BQgAEIAEUNYCWIUeYIkgaABwAHgAgAFOiAHPA5IBATeYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=I8q5YfbyFcajlwTTiKv4Ag&bih=475&biw=1098&rlz=1C1VDKB_esES970ES970"
        #= "https://www.google.com/search?q=chihuahua+*.jpg&tbm=isch&ved=2ahUKEwif6e3BwOX0AhWE8IUKHTMnDaIQ2-cCegQIABAA&oq=husky+*.jpg&gs_lcp=CgNpbWcQAzIECAAQHjoHCCMQ7wMQJzoHCAAQsQMQQzoECAAQQzoICAAQgAQQsQNQoQVYgCNg4yZoAHAAeACAAXeIAe0EkgEDNi4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=-ba5Yd-IKoThlwSzzrSQCg&bih=475&biw=1098&rlz=1C1VDKB_esES970ES970"
        html = requests.get(url)
        soup = BeautifulSoup(html.content,"html.parser")
        tags = soup.find_all("img")

        hola = [tag["src"] for tag in tags]

        

        st.image(
            hola[1],
            width=400, # Manually Adjust the width of the image as per requirement
        )

        st.write("""
        ##### Tamaño:
         """)   

        

        numero_estrellas_tamano = (list(perro.head(1)["Size"])[0])

        if numero_estrellas_tamano == 1:
            unaestrella = Image.open("images/1_estrella.jpg")
            st.image(unaestrella)

        elif numero_estrellas_tamano == 2:
            dosestrellas = Image.open("images/2_estrellas.jpg")
            st.image(dosestrellas)

        elif numero_estrellas_tamano == 3:
            trestrellas = Image.open("images/3_estrellas.jpg")
            st.image(trestrellas)
            
        elif numero_estrellas_tamano == 4:
            cuatroestrellas = Image.open("images/4_estrellas.jpg")
            st.image(cuatroestrellas)

        else: 
            cincoestrellas = Image.open("images/5_estrellas.jpg")
            st.image(cincoestrellas)
        
        st.write(f"""     
        ##### Cantidad de pelo:  
        """) 
        numero_estrellas_pelo = (list(perro.head(1)["Amount Of Shedding"])[0])

        if numero_estrellas_pelo == 1:
            unaestrella = Image.open("images/1_estrella.jpg")
            st.image(unaestrella)

        elif numero_estrellas_pelo == 2:
            dosestrellas = Image.open("images/2_estrellas.jpg")
            st.image(dosestrellas)

        elif numero_estrellas_pelo == 3:
            trestrellas = Image.open("images/3_estrellas.jpg")
            st.image(trestrellas)
            
        elif numero_estrellas_pelo == 4:
            cuatroestrellas = Image.open("images/4_estrellas.jpg")
            st.image(cuatroestrellas)

        else: 
            cincoestrellas = Image.open("images/5_estrellas.jpg")
            st.image(cincoestrellas)


        st.write(f"""     
        ##### Ejercicio necesario:  
        """) 
        numero_estrellas_ejercicio = (list(perro.head(1)['Exercise Needs'])[0])

        if numero_estrellas_ejercicio == 1:
            unaestrella = Image.open("images/1_estrella.jpg")
            st.image(unaestrella)

        elif numero_estrellas_ejercicio == 2:
            dosestrellas = Image.open("images/2_estrellas.jpg")
            st.image(dosestrellas)

        elif numero_estrellas_ejercicio == 3:
            trestrellas = Image.open("images/3_estrellas.jpg")
            st.image(trestrellas)
            
        elif numero_estrellas_ejercicio == 4:
            cuatroestrellas = Image.open("images/4_estrellas.jpg")
            st.image(cuatroestrellas)

        else: 
            cincoestrellas = Image.open("images/5_estrellas.jpg")
            st.image(cincoestrellas)

    
    




    
    st.write("""




    ### Por si quieres valorar otros perretes con características parecidas
    """)

    try:
        lista = perro.head(4).Name.unique()
        c = len(lista)
        cluster = int(perro[perro["Name"]== lista[0]].Groups)
        eleccion2 = data.loc[(data.Groups == cluster)]
        for i in range(0,c):
            eleccion2 = eleccion2[eleccion2.Name != lista[i]]

        eleccion2 = eleccion2.head(4).Name
        st.dataframe(eleccion2)    
    except:
        st.write("""
        No hemos podido encontrar perretes con estas características
        """)

    finada = Image.open("images/pepa8.jpg")
    st.image(finada, use_column_width=True)

