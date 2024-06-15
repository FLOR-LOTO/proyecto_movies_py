import os

class Movie:
    def __init__(self, nombre):
        self.__nombre = nombre #guardo el nombre de la pelicula
        
    @property   #accedo al nombre ya que esta en modo privado y lo transformo en propiedad
    def nombre(self):
        return self.__nombre 

class CatalogoMovies:
    def __init__(self, nombre_catalogo):
        self.nombre = nombre_catalogo
        self.ruta_archivo = f'{nombre_catalogo}.txt'
        
        
    def agregar_pelicula(self, pelicula):
        
        
    def mostrar_peliculas(self):
        
    
    def eliminar_pelicula(self):
        
        