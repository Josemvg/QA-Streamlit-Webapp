import streamlit as st
 
class MultiPage: 
    """
    Clase que gestiona multiples paginas en una misma aplicacion de streamlit.
    """
    def __init__(self) -> None:
        """
        Constructor de la clase MultiPage
        """
        #Atributo pages, diccionario con las subpaginas de nuestra interfaz
        self.pages = {}
    
    def add_page(self, title, func) -> None: 
        """
        Metodo que agrega una pagina a nuestro proyecto. Argumentos:
        - title: Titulo de la pagina, sera el que aparezca en el selector
        - func: Funcion de Python que ejecutara nuestra interfaz para correr la pagina en cuestion
        """
        self.pages.update({title: func})

    def run(self, db):
        """
        Funcion que ejecuta el codigo de la aplicacion
        """
        #Selector   
        page = st.sidebar.radio(
            "App Navigation", 
            self.pages.keys()
        )

        #Ejecutar funcion de la pagina seleccionada
        self.pages[page](db)