'''class Persona:
    def _init_(self, nombre,apellido,telefono,correo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo

    def mostrarDatos(self):
        print (f"Los datos de la persona seleccionada son:\nNombre: {self.nombre} \n apellido: {self.apellido}\n telefono: {self.telefono}\n correo: {self.correo}")

    def mostrarTelefono(self):
        print (f"El telefono es: {self.telefono}")

class Empleado(Persona):
    def _init_(self, codigoEmpleado):
        self.codigoEmpleado = codigoEmpleado

    def ingresarDatosEmpleado(self):
        print("ingrese nombre del empleado")
        self.nombre =input("Nombre")  

    def mostrarEmpleado(self):
        print(f"codigo: {self.codigoEmpleado}, nombre {self.nombre}")

primeraPersona = Persona("Cesar", "Perez","3188896098","cesaraperezt@gmail.com")
segundaPersona = Persona("Andres","Parra","3155432323","andresP@mail.com")

primeraPersona.mostrarDatos()
segundaPersona.mostrarDatos()

primeraPersona.mostrarTelefono()

primerEmpleado = Empleado("1231")
primerEmpleado.ingresarDatosEmpleado()
primerEmpleado.mostrarEmpleado()
'''

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

# Agrega 2 libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 471, "Realismo mágico")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, 96, "Fábula")

# Agrega 2 revistas
revista1 = Revista("National Geographic", "Varios", 2023, 150, "Marzo")
revista2 = Revista("Muy Interesante", "Varios", 2022, 98, "Julio")

biblioteca.agregar_publicacion(libro1)
biblioteca.agregar_publicacion(libro2)
biblioteca.agregar_publicacion(revista1)
biblioteca.agregar_publicacion(revista2)

biblioteca.mostrar_publicaciones()

biblioteca.buscar_por_titulo("El Principito")