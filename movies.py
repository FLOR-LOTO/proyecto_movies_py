import os

class Movie:
    def __init__(self, name, director, year_premiere):
        self.__name = name
        self.director = director
        self.year_premiere = year_premiere
        
    @property
    def name(self):
        return self.__name 

class CatalogMovies:
    def __init__(self, name_catalog):
        self.name = name_catalog
        self.rute_file = f'{self.name}.txt'
      
        if not os.path.exists(self.rute_file):
            with open(self.rute_file, 'w') as file:
                pass  
        
    def add_movie_catalog(self, movie):
        with open(self.rute_file, 'a') as file:
            file.write(f'Pelicula: {movie.name}\n'
                       f'  Director: {movie.director}\n'
                       f'  Estreno: {movie.year_premiere}\n' + '\n') 
        
    def all_movies(self):
        with open(self.rute_file, 'r') as file:
            movies = file.readlines()
            
        if movies:
            print(f"\nLISTA DE PELÍCULAS EN EL CATÁLOGO {self.name.upper()}:\n")
            for movie in movies:
                print(movie)
        else:
            print(f"\nAÚN NO HAY PELÍCULAS EN EL CATÁLOGO {self.name.upper()}\n")
    
    def delete_catalog(self):
        if os.path.exists(self.rute_file):
            os.remove(self.rute_file)
            print(f"\nEL CATÁLOGO {self.name.upper()} HA SIDO ELIMINADO CORRECTAMENTE\n")
        
        
def show_menu(): print(
    "\nMenú de opciones:\n"
    "1. Agregar Película\n"
    "2. Listar Películas\n"
    "3. Eliminar catálogo de películas\n"
    "4. Volver al menú principal\n"
    "5. Salir"
)

def main():
    while True:
        name_catalog = input('Ingrese el nombre del catálogo: ').lower()
        catalog = CatalogMovies(name_catalog)
        
        while True:
            show_menu()
            option = input('Seleccione una opción: ')
            
            if option == '1':
                name_movie = input('Ingrese el nombre de la pelicula: ')
                name_director = input('Ingrese el director de la pelicula: ')
                year_premiere = input('Ingrese el año de estreno: ')
                movie = Movie(name_movie, name_director, year_premiere)
                catalog.add_movie_catalog(movie)
                print(f"La película '{name_movie}' ha sido agregada al catálogo.")
                
            elif option == '2':
                catalog.all_movies()
                
            elif option == '3':
                confirmacion = input('Esta seguro que desea eliminar el catálogo? (s/n): ')
                if confirmacion.lower() == 's':
                    catalog.delete_catalog()
                    
            elif option == '4':
                break
                
            elif option == '5':
                print("Fin del programa. Vuelve pronto!!")
                return
            
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
                

main()