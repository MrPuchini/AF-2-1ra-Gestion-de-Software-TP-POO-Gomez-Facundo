class Estudiante:

    def __init__(self, nombre: str, apellido: str, matricula: str, carrera: str):

        self.__nombre = nombre
        self.__apellido = apellido
        self.__matricula = matricula
        self.__carrera = carrera
        self.cursos_inscriptos = []

    def agregarCurso(self, curso):

        self.cursos_inscriptos.append(curso)

    def quitarCurso(self, curso):

        if curso in self.cursos_inscriptos:
            self.cursos_inscriptos.remove(curso)

    def getMatricula(self):

        return self.__matricula

    def getNombre(self):

        return self.__nombre

    def getApellido(self):

        return self.__apellido

    def getCarrera(self):

        return self.__carrera


class Curso:

    def __init__(self, nombre: str, codigo: str, profesor: str, capacidad: int):

        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad = capacidad
        self.estudiantes_inscriptos = []

    def inscribir_estudiante(self, estudiante):

        if self.estaDisponible():

            self.estudiantes_inscriptos.append(estudiante)
            return True

        else:

            return False

    def estaDisponible(self):

        if len(self.estudiantes_inscriptos) < self.capacidad:
            return True
        else:
            return False

    def dar_baja_estudiante(self, estudiante):

        if estudiante in self.estudiantes_inscriptos:

            self.estudiantes_inscriptos.remove(estudiante)
            return True

        else:

            return False


class Facultad:

    def __init__(self):

        self.estudiantes = []
        self.cursos = []

    def agregarEstudiante(self):

        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        matricula = input("Ingrese el numero de matricula: ")
        carrera = input("Ingrese la carrera del estudiante: ")

        if not matricula.isdigit():

            print("Error: la matricula debe contener solamente numeros.")
            return

        if self.getEstudiante(matricula) != None:

            print("Error: ya existe un estudiante con esa matricula.")
            return

        estudianteobj = Estudiante(nombre, apellido, matricula, carrera)

        self.estudiantes.append(estudianteobj)

        print("Estudiante agregado correctamente.")

    def getEstudiante(self, matricula):

        for estudiante in self.estudiantes:

            if estudiante.getMatricula() == matricula:

                return estudiante

        return None

    def agregarCurso(self):

        nombre = input("Ingrese el nombre del curso: ")
        codigo = input("Ingrese el codigo del curso: ")
        profesor = input("Ingrese el profesor encargado: ")

        if self.getCurso(codigo) != None:

            print("Error: ya existe un curso con ese codigo.")
            return

        capacidad = input("Ingrese la capacidad maxima de estudiantes: ")

        if not capacidad.isdigit():

            print("Error: la capacidad debe ser un numero.")
            return

        capacidad = int(capacidad)

        if capacidad <= 0:

            print("Error: la capacidad debe ser mayor a 0.")
            return

        cursoobj = Curso(nombre, codigo, profesor, capacidad)

        self.cursos.append(cursoobj)

        print("Curso agregado correctamente.")

    def getCurso(self, codigo):

        for curso in self.cursos:

            if curso.codigo == codigo:

                return curso

        return None

    def inscribirEstudiante(self):

        matricula = input("Ingrese la matricula del estudiante: ")

        if not matricula.isdigit():

            print("Error: la matricula debe contener solamente numeros.")
            return

        estudiante = self.getEstudiante(matricula)

        if estudiante == None:

            print("Error: el estudiante no existe.")
            return

        codigo = input("Ingrese el codigo del curso: ")

        curso = self.getCurso(codigo)

        if curso == None:

            print("Error: el curso no existe.")
            return

        if estudiante in curso.estudiantes_inscriptos:

            print("Error: el estudiante ya esta inscripto en este curso.")
            return

        if curso.estaDisponible():

            curso.inscribir_estudiante(estudiante)
            estudiante.agregarCurso(curso)

            print("Estudiante inscripto correctamente.")

        else:

            print("Error: no hay cupos disponibles en este curso.")

    def darBajaCurso(self):

        matricula = input("Ingrese la matricula del estudiante: ")

        if not matricula.isdigit():

            print("Error: la matricula debe contener solamente numeros.")
            return

        estudiante = self.getEstudiante(matricula)

        if estudiante == None:

            print("Error: el estudiante no existe.")
            return

        codigo = input("Ingrese el codigo del curso: ")

        curso = self.getCurso(codigo)

        if curso == None:

            print("Error: el curso no existe.")
            return

        if curso.dar_baja_estudiante(estudiante):

            estudiante.quitarCurso(curso)

            print("El estudiante se dio de baja correctamente.")

        else:

            print("Error: el estudiante no esta inscripto en este curso.")

    def mostrarCursos(self):

        if len(self.cursos) == 0:

            print("No hay cursos registrados.")
            return

        print("\n----- CURSOS DE LA FACULTAD -----")

        for curso in self.cursos:

            inscriptos = len(curso.estudiantes_inscriptos)
            disponibles = curso.capacidad - inscriptos

            print("\nNombre:", curso.nombre)
            print("Codigo:", curso.codigo)
            print("Profesor:", curso.profesor)
            print("Capacidad maxima:", curso.capacidad)
            print("Estudiantes inscriptos:", inscriptos)
            print("Cupos disponibles:", disponibles)

    def mostrarEstudiantes(self):

        if len(self.estudiantes) == 0:

            print("No hay estudiantes registrados.")
            return

        print("\n----- ESTUDIANTES DE LA FACULTAD -----")

        for estudiante in self.estudiantes:

            print("\nNombre:", estudiante.getNombre())
            print("Apellido:", estudiante.getApellido())
            print("Matricula:", estudiante.getMatricula())
            print("Carrera:", estudiante.getCarrera())

            if len(estudiante.cursos_inscriptos) == 0:

                print("Cursos inscriptos: Ninguno")

            else:

                print("Cursos inscriptos:")

                for curso in estudiante.cursos_inscriptos:

                    print("-", curso.nombre, "| Codigo:", curso.codigo)


def main():

    facultad_urquiza = Facultad()

    while True:

        opcion = menu()

        if opcion == "7":

            break

        elif opcion == "1":

            facultad_urquiza.agregarEstudiante()

        elif opcion == "2":

            facultad_urquiza.agregarCurso()

        elif opcion == "3":

            facultad_urquiza.inscribirEstudiante()

        elif opcion == "4":

            facultad_urquiza.darBajaCurso()

        elif opcion == "5":

            facultad_urquiza.mostrarCursos()

        elif opcion == "6":

            facultad_urquiza.mostrarEstudiantes()

        else:

            print("Error: opcion no valida.")

    print("Programa Terminado")


def menu():

    print("\nSistema de Gestion de Facultad:")
    print("1- Agregar Estudiante")
    print("2- Agregar Curso")
    print("3- Inscribir Estudiante a Curso")
    print("4- Dar de Baja Estudiante de Curso")
    print("5- Mostrar Cursos")
    print("6- Mostrar Estudiantes")
    print("7- Salir")

    return input("Seleccione una opcion: ")


main()
