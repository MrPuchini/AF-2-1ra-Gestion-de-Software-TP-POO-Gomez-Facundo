class Miembro:

    def __init__(self, dni: str, nombre: str):

        self.setDni(dni)
        self.__nombre = nombre
        self.libros_prestados = []

    def agregarLibroPrestado(self, libro):

        self.libros_prestados.append(libro)

    def quitarLibroPrestado(self, libro):

        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def getDni(self):

        return self.__dni

    def setDni(self, dni):

        if dni.isdigit() and len(dni) >= 6:
            self.__dni = dni
        else:
            print("Error: el DNI debe contener solamente numeros y tener al menos 6 digitos.")
            self.__dni = ""

    def getNombre(self):

        return self.__nombre


class Libro:

    def __init__(self, titulo: str, autor: str, isbn: str, ejemplar: int):

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ejemplar = ejemplar
        self.prestado_a = []

    def prestar_libro(self, miembro: Miembro):

        if self.estaDisponible():
            self.prestado_a.append(miembro)
            return True
        else:
            return False

    def estaDisponible(self):

        if len(self.prestado_a) < self.ejemplar:
            return True
        else:
            return False

    def devolver_libro(self, miembro):

        if miembro in self.prestado_a:
            self.prestado_a.remove(miembro)
            return True
        else:
            return False


class Biblioteca:

    def __init__(self):

        self.libros = []
        self.miembros = []

    def agregarLibro(self):

        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")

        if not isbn.isdigit():
            print("Error: el ISBN debe contener solamente numeros.")
            return

        libro = self.getLibro(isbn)

        if libro:

            print("El libro ya existe.")

            agregarejemplar = input("Cuantos ejemplares desea agregar: ")

            if not agregarejemplar.isdigit():
                print("Error: debe ingresar un numero.")
                return

            agregarejemplar = int(agregarejemplar)

            if agregarejemplar <= 0:
                print("Error: debe ingresar una cantidad mayor a 0.")
                return

            libro.ejemplar += agregarejemplar

            print("Ejemplares agregados correctamente.")

        else:

            agregarejemplar = input("Cuantos ejemplares desea agregar: ")

            if not agregarejemplar.isdigit():
                print("Error: debe ingresar un numero.")
                return

            agregarejemplar = int(agregarejemplar)

            if agregarejemplar <= 0:
                print("Error: debe ingresar una cantidad mayor a 0.")
                return

            libro = Libro(titulo, autor, isbn, agregarejemplar)

            self.libros.append(libro)

            print("Libro agregado correctamente.")

    def getLibro(self, isbn):

        for libro in self.libros:

            if libro.isbn == isbn:
                return libro

        return None

    def getMiembro(self, dni):

        for miembro in self.miembros:

            if miembro.getDni() == dni:
                return miembro

        return None

    def quitarLibro(self):

        isbn = input("Ingrese el ISBN del libro a quitar: ")

        libroaBorrar = self.getLibro(isbn)

        if libroaBorrar == None:
            print("Error: el libro no existe.")
            return

        ejemplaresaquitar = input(
            "Cuantos ejemplares desea quitar? (Hay "
            + str(libroaBorrar.ejemplar)
            + " ejemplares): "
        )

        if not ejemplaresaquitar.isdigit():
            print("Error: debe ingresar un numero.")
            return

        ejemplaresaquitar = int(ejemplaresaquitar)

        if ejemplaresaquitar <= 0:
            print("Error: debe ingresar una cantidad mayor a 0.")
            return

        disponibles = libroaBorrar.ejemplar - len(libroaBorrar.prestado_a)

        if ejemplaresaquitar > disponibles:
            print("Error: no puede quitar tantos ejemplares.")
            print("Ejemplares disponibles para quitar:", disponibles)
            return

        if ejemplaresaquitar == libroaBorrar.ejemplar:

            self.libros.remove(libroaBorrar)

            print("Libro eliminado correctamente.")

        else:

            libroaBorrar.ejemplar -= ejemplaresaquitar

            print("Ejemplares eliminados correctamente.")
            print("Quedan", libroaBorrar.ejemplar, "ejemplares.")

    def agregarMiembro(self):

        nombre = input("Ingrese el nombre del socio: ")
        dni = input("Ingrese el DNI del socio: ")

        if not dni.isdigit() or len(dni) < 6:
            print("Error: el DNI debe contener solamente numeros y tener al menos 6 digitos.")
            return

        if self.getMiembro(dni) != None:
            print("Error: ya existe un miembro con ese DNI.")
            return

        miembroobj = Miembro(dni, nombre)

        self.miembros.append(miembroobj)

        print("Miembro agregado correctamente.")

    def quitarMiembro(self):

        dni = input("Ingrese el DNI de la persona a borrar: ")

        personaaborrar = self.getMiembro(dni)

        if personaaborrar == None:
            print("Error: el miembro no existe.")
            return

        if len(personaaborrar.libros_prestados) > 0:
            print("Error: no se puede borrar un miembro que tiene libros prestados.")
            return

        self.miembros.remove(personaaborrar)

        print("Miembro eliminado correctamente.")

    def prestar_libro(self):

        dni = input("Ingrese el DNI de la persona a la que se le prestara: ")

        if not dni.isdigit():
            print("Error: el DNI debe contener solamente numeros.")
            return

        isbn = input("Ingrese el ISBN del libro a prestar: ")

        if not isbn.isdigit():
            print("Error: el ISBN debe contener solamente numeros.")
            return

        libroaprestar = self.getLibro(isbn)

        if libroaprestar == None:
            print("Libro no existe.")
            return

        miembroaprestar = self.getMiembro(dni)

        if miembroaprestar == None:
            print("Miembro no existe.")
            return

        if libroaprestar.estaDisponible():

            libroaprestar.prestar_libro(miembroaprestar)
            miembroaprestar.agregarLibroPrestado(libroaprestar)

            print("Libro prestado correctamente.")

        else:

            print("No hay ejemplares disponibles de este libro.")

    def devolver_libro(self):

        dni = input("Ingrese el DNI de la persona que devuelve el libro: ")

        if not dni.isdigit():
            print("Error: el DNI debe contener solamente numeros.")
            return

        isbn = input("Ingrese el ISBN del libro a devolver: ")

        if not isbn.isdigit():
            print("Error: el ISBN debe contener solamente numeros.")
            return

        libroaDevolver = self.getLibro(isbn)

        if libroaDevolver == None:
            print("Libro no existe.")
            return

        miembro = self.getMiembro(dni)

        if miembro == None:
            print("Miembro no existe.")
            return

        if libroaDevolver.devolver_libro(miembro):

            miembro.quitarLibroPrestado(libroaDevolver)

            print("Libro devuelto correctamente.")

        else:

            print("Error: este miembro no tiene prestado ese libro.")

    def mostrarLibros(self):

        if len(self.libros) == 0:
            print("No hay libros registrados.")
            return

        print("\n----- LIBROS DE LA BIBLIOTECA -----")

        for libro in self.libros:

            disponibles = libro.ejemplar - len(libro.prestado_a)

            print("\nTitulo:", libro.titulo)
            print("Autor:", libro.autor)
            print("ISBN:", libro.isbn)
            print("Cantidad de ejemplares:", libro.ejemplar)
            print("Ejemplares disponibles:", disponibles)

            if len(libro.prestado_a) == 0:

                print("Estado: Disponible")

            else:

                print("Estado: Hay ejemplares prestados.")

                for miembro in libro.prestado_a:

                    print(
                        "Prestado a:",
                        miembro.getNombre(),
                        "- DNI:",
                        miembro.getDni()
                    )

    def mostrarMiembros(self):

        if len(self.miembros) == 0:
            print("No hay miembros registrados.")
            return

        print("\n----- MIEMBROS DE LA BIBLIOTECA -----")

        for miembro in self.miembros:

            print("\nNombre:", miembro.getNombre())
            print("DNI:", miembro.getDni())

            if len(miembro.libros_prestados) == 0:

                print("Libros prestados: Ninguno")

            else:

                print("Libros prestados:")

                for libro in miembro.libros_prestados:

                    print("-", libro.titulo, "| ISBN:", libro.isbn)

    def mostrarLibrosPrestadosAMiembro(self):

        dni = input("Ingrese el DNI del miembro: ")

        if not dni.isdigit():
            print("Error: el DNI debe contener solamente numeros.")
            return

        miembro = self.getMiembro(dni)

        if miembro == None:
            print("Error: el miembro no existe.")
            return

        print("\n----- LIBROS PRESTADOS -----")
        print("Miembro:", miembro.getNombre())
        print("DNI:", miembro.getDni())

        if len(miembro.libros_prestados) == 0:

            print("Este miembro no tiene libros prestados.")

        else:

            for libro in miembro.libros_prestados:

                print("-", libro.titulo, "| ISBN:", libro.isbn)


def main():

    biblioteca_urquiza = Biblioteca()

    while True:

        opcion = menu()

        if opcion == "10":

            break

        elif opcion == "1":

            biblioteca_urquiza.agregarLibro()

        elif opcion == "2":

            biblioteca_urquiza.quitarLibro()

        elif opcion == "3":

            biblioteca_urquiza.agregarMiembro()

        elif opcion == "4":

            biblioteca_urquiza.quitarMiembro()

        elif opcion == "5":

            biblioteca_urquiza.prestar_libro()

        elif opcion == "6":

            biblioteca_urquiza.devolver_libro()

        elif opcion == "7":

            biblioteca_urquiza.mostrarLibros()

        elif opcion == "8":

            biblioteca_urquiza.mostrarMiembros()

        elif opcion == "9":

            biblioteca_urquiza.mostrarLibrosPrestadosAMiembro()

        else:

            print("Error: opcion no valida.")


    print("Programa Terminado")


def menu():

    print("\nSistema de Gestion de Biblioteca:")
    print("1- Agregar Libro")
    print("2- Quitar Libro")
    print("3- Agregar Miembro")
    print("4- Borrar Miembro")
    print("5- Prestar Libro")
    print("6- Devolver Libro")
    print("7- Mostrar Libros")
    print("8- Mostrar Miembros")
    print("9- Mostrar Libros Prestados a Miembro")
    print("10- Salir")

    return input("Seleccione una opcion: ")


main()

