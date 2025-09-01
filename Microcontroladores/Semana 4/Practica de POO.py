class Publicacion:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar_informacion(self):
        print (f"Los datos de la publicacion son:\nTitulo: {self.titulo} \n Autor: {self.autor}\n Año: {self.año}")

class Libro(Publicacion):
    def __init__(self, titulo, autor, año, numeroPaginas, genero):
        super().__init__(titulo, autor, año)
        self.numeroPaginas = numeroPaginas
        self.genero = genero

    def mostrar_informacion(self):
         print(f"Libro: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Páginas: {self.numeroPaginas}, Género: {self.genero}")

class Revista(Publicacion):
    def __init__(self, titulo, autor, año, numeroEdicion, mesPublicacion):
        super().__init__(titulo, autor, año)
        self.numeroEdicion = numeroEdicion
        self.mesPublicacion = mesPublicacion

    def mostrar_informacion(self):
        print(f"Revista: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Edición: {self.numeroEdicion}, Mes: {self.mesPublicacion}")

class Biblioteca:
    def __init__(self):
        self.publicaciones = []

    def agregar_publicacion(self, publicacion):
        self.publicaciones.append(publicacion)

    def mostrar_publicaciones(self):
        for publicacion in self.publicaciones:
            publicacion.mostrar_informacion()

    def buscar_por_titulo(self, titulo):
        for publicacion in self.publicaciones:
            if publicacion.titulo == titulo:
                publicacion.mostrar_informacion()
                return
        print("Publicación no encontrada.")

biblioteca = Biblioteca()

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 471, "Realismo mágico")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, 96, "Fábula")

revista1 = Revista("National Geographic", "Varios", 2023, 150, "Marzo")
revista2 = Revista("Muy Interesante", "Varios", 2022, 98, "Julio")

biblioteca.agregar_publicacion(libro1)
biblioteca.agregar_publicacion(libro2)
biblioteca.agregar_publicacion(revista1)
biblioteca.agregar_publicacion(revista2)

biblioteca.mostrar_publicaciones()

titulo_busqueda = input("Ingrese el título a buscar: ")
biblioteca.buscar_por_titulo(titulo_busqueda)