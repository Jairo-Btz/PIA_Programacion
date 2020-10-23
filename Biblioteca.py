
#importamos la clase sys para salir del sistema
#importamos la clase datetime para que nos ayude con el formato de las fechas
import sys
from datetime import datetime
#definimos clase libro para poder registrar nuevos libros
class Libro:
    #constructor para obtener los atributos de la clase
    def __init__(self, isbn,titulo, autor, año_publicacion, precio):
        #atributos de la clase privados
        self.__isbn=isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion
        self.__precio = precio
    #metodo para imprimir los atributos de la clase
    def mostrarDatos(self):
        print(f"ISBN: {self.__isbn}\nTitulo: {self.__titulo}\nAutor: {self.__autor}\nAño Publicación: {self.__año_publicacion}\nPrecio: {self.__precio}")
    #metodo getters para obtener los atributos de la clase, ya que son privados
    def get_isbn(self):
        return self.__isbn
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_año(self):
        return self.__año_publicacion
    def get_precio(self):
        return self.__precio
    #metodos setters para actualizar los atributos de la clase
    def set_isbn(self,isbn):
        self.__isbn=isbn
    def set_titulo(self,titulo):
        self.__titulo=titulo
    def set_autor(self,autor):
        self.__autor=autor
    def set_año(self,año):
        self.__año_publicacion=año
    def set_precio(self,precio):
        self.__precio=precio


#definimos la clase Estanteria que servira como almacenamiento de los libros
class Estanteria:
    #constructor de la clase
    def __init__(self):
        #se define la lista donde se añadiran los libros
        self.__libros=list()
    #metodo para registra/almacenar un libro
    def registrarLibro(self):
        #variable que sirve de interruptor
        continuar = True
        #iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta
        while continuar:
            # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta

            while True:
                #definimos un bloque de excepciones
                try:
                    _opcion = int(input("Ha elegido 'Añadir Libro', desea continuar? (1 Continuar,0 Volver al menu)"))
                except:
                    print("Opcion no valida, intente de nuevo")
                else:
                #avanzamos
                    break
            #si elige la opcion 1 procedemos a actualizar el libro
            if _opcion == 1:
                # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta
                isbn_go = True
                while isbn_go:
                    # definimos un bloque de excepciones

                    try:
                        isbn = int(input("ISBN:\n"))
                    except:
                        print("Valor no valido, solo enteros")
                    else:
                        #variable para ver el largo del isbn
                        len_isbn = len(str(isbn))
                        #si el isbn es diferente a 13 no es valido ya que un isbn es de 13 digitos
                        if len_isbn != 13:
                            print(f"Un ISBN es de 13 digitos, tu introdujiste {len_isbn}")
                        else:
                            #si la estanteria no tiene libros aun registrados se guarda automaticamente
                            if estanteria.longitud() == 0:
                                break
                            else:
                                #si tiene libros se checa el isbn ingresado para evitar duplicidad
                                for i in self.check_ISBN():
                                    if isbn == i:
                                        print("Ya hay un libro con el mismo ISBN, intente con otro")
                                        continue
                                    else:
                                        isbn_go = False
                                        #avanzamos
                                        break
                #varibale que almacenara el titulo
                titulo = input("Titulo del libro:\n")
                #variable que almacenara el autor
                autor = input("Autor del libro:\n")
                # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta

                while True:
                    #definimos un bloque de excepciones para verificar que el dato ingresado coincide con el requerido

                    try:
                        _año = input("Año de publicacion:\n")
                        año = datetime.strptime(_año, '%Y')
                        año = año.year
                    except:
                        print("Valor no valido, solo enteros")

                    else:
                        #avanzamos
                        break
                # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta

                while True:
                    #definimos un bloque de excepciones para verificar que el dato ingresado coincide con el requerido

                    try:
                        precio = int(input("Precio del libro:\n"))
                    except:
                        print("Valor no valido, solo enteros")
                    else:
                        #avanzamos
                        break
                    #imprimimos los datos
                print("Datos: ")
                print(f"ISBN: {isbn}\nTitulo: {titulo}\nAutor: {autor}\nAño Publicación: {año}\nPrecio: {precio}")
                # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta

                while True:
                    #definimos un bloque de excepciones para verificar que el dato ingresado coincide con el requerido

                    try:
                        save = int(
                            input("Desea guardar los datos? (1 guardar y volver al menu, 0 cancelar y volver al menu)"))
                    except:
                        print("Valor no valido, solo enteros")
                    else:
                        # si el valor ingresado es 1, el libro se guarda
                        if save == 1:
                            #se instancia un objeto de la clase Libro y le pasamos los correspondientes parametros

                            libro = Libro(isbn, titulo, autor, año, precio)
                            #usamos el metodo añadirLibro de esta clase para guardar el registro
                            self.añadirLibro(libro)
                            print("Libro guardado correctamente")
                            continuar = False
                            #volvemos al menu
                            break
                        # si es 0 no se guarda y volvemos al inicio
                        elif save == 0:
                            continuar = False
                            break
                        else:
                            print("Opcion no valida")
            #si el valor ingresado es 0 volvemos al inicio
            elif _opcion == 0:
                continuar = False
            else:
                print("Opcion no valida intente de nuevo")
    #metodo para añadir el libro a la estanteria
    def añadirLibro(self,libro):
        self.__libros.append(libro)
    #metodo para mostrar en consola los libros que se tienen registrados
    def mostrarLibros(self):
        c=0
        #se recorren todos los libros y se llama al metodo mostrarDatos de la clase Libro por cada elemento de la lista
        for i in self.__libros:
            c=c+1
            print(f"Posicion: {c}")
            i.mostrarDatos()
            print(50*"*")
    #metodo para mostra un libro en especifico a la hora de editar
    def mostrarLibro(self,posicion):
        #se llama al metodo mostrarDatos de la clase Libro en funcion del elemento elegido
        self.__libros[posicion-1].mostrarDatos()
    #metodo para eliminar libros
    def eliminarLibro(self):
        #primero mostramos en consola todos los libros
        self.mostrarLibros()
        print("Elija la posicion en el estante del libro que desee borrar, 0 para cancelar")
        # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta

        while True:

            try:
                posicion = int(input())
            except:
                print("Valor no valido")
            else:

                if posicion == 0:
                    #volvemos al menu
                    break
                else:
                    #definimos un bloque de tratamiento de excepciones en dado caso de que el usuario ingrese un valor
                    # no valido o fuera de rango
                    try:
                        self.__libros.pop(posicion-1)
                    except:
                        print("Lugar no ocupado, intente con otra posicion o presione 0 para salir")
                        continue
                    else:
                        #una vez ingresado un valor valido y en el rango de la longitud de la lista
                        #se define una copia de la lista
                        self.__libros_copy=self.__libros
                        #vaciamos la lista original
                        self.__libros=list()
                        print("Libro eliminado.")
                        print("Reacomodando libros...")
                        #en base a la lista original que tenemos en la copia de la lista, llenamos la lista original
                        # de nuevo para que se recorran los espacios
                        for i in self.__libros_copy:
                            self.__libros.append(i)
                        print("Libros ordenados correctamente.")
                        #terminamos el ciclo y volvemos al menu
                        break
    #metodo que devuelve la longitud de la lista
    def longitud(self):
        return len(self.__libros)
    #metodo que ayuda a checar los ISBN ya registrados
    def check_ISBN(self):
        #se define la lista donde iran los ISBN
        self.__isbns = list()
        #recorremos la lista donde se almacenan los libros, y usamos el metodo get_isbn de la clase Libro para poder
        #obtener el isbn y almacenar los isbn
        for i in self.__libros:
            self.__isbns.append(i.get_isbn())
        #devolvemos la lista
        return self.__isbns
    #metodos usados para editar los atributos de los libros gracias a los metodos setters de la clase Libro
    def editarISBN(self,posicion,isbn):
        self.__libros[posicion-1].set_isbn(isbn)
    def editarTitulo(self,posicion,titulo):
        self.__libros[posicion-1].set_titulo(titulo)
    def editarAutor(self,posicion,autor):
        self.__libros[posicion-1].set_autor(autor)
    def editarAño(self,posicion,año):
        self.__libros[posicion-1].set_año(año)
    def editarPrecio(self,posicion,precio):
        self.__libros[posicion-1].set_precio(precio)
    #metodo para editar el libro
    def editarLibro(self):
        #primero verificamos que haya libros
        if self.longitud() == 0:
            print("No se han añadido libros aun.")
        else:
            #una vez pasada la condicion anterior imprimimos los libros gracias al metodo mostrarLibros
            self.mostrarLibros()
            # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta

            while True:
                # definimos un bloque de tratamiento de excepciones en dado caso de que el usuario ingrese un valor
                # no valido o fuera de rango
                try:
                    print("Elija la posicion del estante en la que se encuentra el libro que quiere editar. 0 Volver al menu")
                    posicion = int(input())
                except:
                    print("Valor no admitido, presione 0 para salir")
                else:
                    #si el valor ingresado es 0, volvera al menu el usuario
                    if posicion == 0:
                        break
                    elif posicion > self.longitud():
                        print("Posicion fuera de rango. Intente de nuevo.")
                    else:
                        #una vez superado el bloque anterior lo que hacemos es mostrar en pantalla el libro seleccionado
                        self.mostrarLibro(posicion)
                        opciones_edit = True
                        # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta

                        while opciones_edit:
                            # definimos un bloque de tratamiento de excepciones en dado caso de que el usuario ingrese
                            # un valor no valido
                            try:
                                print("Presione el numero segun el atributo a cambiar")
                                print("1)ISBN\n2)Titulo\n3)Autor\n4)Año Publicacion\n5)Precio\n0)Volver")
                                _opcion = int(input())
                            except:
                                print("Valor no valido")
                            else:
                                #si elije 0 volvera a la opcion de elegir el libro
                                if _opcion == 0:
                                    opciones_edit = False

                                #si elige 1 editara el ISBN
                                elif _opcion == 1:
                                    isbn_go = True
                                    while isbn_go:
                                        # definimos un bloque de tratamiento de excepciones en dado caso de que el usuario ingrese
                            # un valor no valido
                                        try:
                                            isbn = int(input("ISBN:\n"))
                                        except:
                                            print("Valor no valido, solo enteros")
                                        else:
                                            # variable para ver el largo del isbn
                                            len_isbn = len(str(isbn))
                                            #si el largo del valor ingresado es diferente a 13 no dejara avanzar
                                            if len_isbn != 13:
                                                print(f"Un ISBN es de 13 digitos, tu introdujiste {len_isbn}")
                                            else:
                                                #verificamos el isbn para ver que no este anteriormente ingresado
                                                for i in self.check_ISBN():
                                                    if isbn == i:
                                                        print("Ya hay un libro con el mismo ISBN, intente con otro")
                                                        continue
                                                    else:
                                                        #una vez pasados los filtros usamos el metodo editarISBN para
                                                        #registrar el cambio
                                                        self.editarISBN(posicion, isbn)
                                                        print("Cambio guardado con exito")
                                                        isbn_go = False
                                                        #avanzamos
                                                        break
                                #opcion para cambiar el titulo
                                elif _opcion == 2:
                                    #variable del nuevo titulo
                                    titulo = input("Titulo del libro:\n")
                                    #usamos el metodo editarTitulo
                                    self.editarTitulo(posicion, titulo)
                                    print("Cambio guardado con exito.")
                                #opcion para cambiar el autor
                                elif _opcion == 3:
                                    #variable del nuevo titulo
                                    autor = input("Autor del libro:\n")
                                    #usamos el metodo editarAutor
                                    self.editarAutor(posicion,autor)
                                    print("Cambio guardado con exito.")
                                #opcion para cambiar el año de la publicacion
                                elif _opcion == 4:
                                    # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta

                                    while True:
                                        # definimos un bloque de excepciones para verificar que el dato ingresado coincide con el requerido

                                        try:
                                            _año = input("Año de publicacion:\n")
                                            año = datetime.strptime(_año, '%Y')
                                            año = año.year
                                        except:
                                            print("Valor no valido, solo enteros")
                                        else:
                                            #si coincide entonces usamos el metodo editarAño para cambiar el año
                                            self.editarAño(posicion, año)
                                            print("Cambio guardado con exito")
                                            #volvemos al menu
                                            break
                                elif _opcion == 5:
                                    # iniciamos ciclo para que haya una repiticion en dado caso de no ingresar una respuesta correcta

                                    while True:
                                        # definimos un bloque de excepciones para verificar que el dato ingresado coincide con el requerido

                                        try:
                                            precio = int(input("Precio del libro:\n"))
                                        except:
                                            print("Valor no valido, solo enteros")
                                        else:
                                            #si coincide entonces usamos el metodo editarPrecio para cambiar el precio

                                            self.editarPrecio(posicion, precio)
                                            print("Cambio guardado con exito")
                                            #volvemos al menu
                                            break
#clase definida para construir un Menu
class Menu:
    #iniciador  del menu
    def __init__(self):
        self.iniciarMenu()
        #metodo contenedor del menu
    def iniciarMenu(self):
        print("Elija una opción: ")
        print("1)Añadir Libro")
        print("2)Eliminar Libro")
        print("3)Editar Libro")
        print("4)Mostrar Libros")
        print("5)Salir")
        #iniciamos ciclo por si hay respuesta no validas
        while True:
            #definimos un bloque de tratamiento de excepciones por si un valor ingresado no es valido
            try:
                opcion = int(input())
            except:
                print("Opcion no valida intente de nuevo")
            else:
                #avanzamos
                break

        #en la opcion 2,3,4 primero se verifica si hay libros o no
        #si el valor ingresado es 1 entonces llamado al metodo registrarLibro de la clase Estanteria
        if opcion == 1:
            estanteria.registrarLibro()
        # si el valor ingresado es 2 entonces llamado al metodo eliminarLibro de la clase Estanteria

        elif opcion == 2:
            if estanteria.longitud() == 0:
                print("No se han añadido libros aun.")
            else:
                estanteria.eliminarLibro()
        # si el valor ingresado es 3 entonces llamado al metodo editarLibro de la clase Estanteria
        elif opcion == 3:
            if estanteria.longitud()==0:
                print("No se han añadido libros aun.")
            else:
                estanteria.editarLibro()

            # si el valor ingresado es 4 entonces llamado al metodo mostrarLibro de la clase Estanteria
        elif opcion == 4:
            if estanteria.longitud()==0:
                print("No se han añadido libros aun.")
            else:
                estanteria.mostrarLibros()
            #si el valor ingresado es 5 entonces con ayuda del metodo salir  salimos del programa
        elif opcion == 5:
            self.salir()
        else:
            print("Opcion no valida, intente de nuevo...")
    #metodo para salir del programa gracias al metodo exit de la libreria sys
    def salir(self):
        sys.exit()
#instanciamos un objeto
estanteria = Estanteria()
#definimos un ciclo para que se ejecute el programa continuamente
while True:
    menu=Menu()
