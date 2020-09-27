from helpers.helper import input_data, print_table, pregunta, input_isbn, input_fecha
from helpers.menu import Menu
from classes.libro import Libro

class Libros_controller():
    def __init__(self):
        self.libro = Libro()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Libros
                ===============
                ''')
                menu = ['Listar libros', 'Buscar Libro', "Nuevo Libro", "Salir"]
                respuesta = Menu(menu).show()

                if respuesta == 1:
                    self.listar_libros()
                elif respuesta == 2:
                    self.buscar_libro()
                elif respuesta == 3:
                    self.insertar_libro()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_libros(self):
        print('''
        ========================
            Lista de Libros
        ========================
        ''')
        libros = self.libro.obtener_libros('id_libro')
        print(print_table(libros, ['ID', 'ISBN', 'Nombre del libro', 'Autor', 'Editorial', 'Estado del Libro', 'Nombre del lector']))
        input("\nPresione una tecla para continuar...")

    def insertar_libro(self):
        isbn = input_isbn()
        nombre = input_data("Ingrese el nombre del libro >> " )
        autor = input_data("Ingrese el nombre del autor del libro >> ")
        editorial = input_data("Ingrese la editorial a la cual corresponde el libro >> ")
        estado_libro = "Disponible"
        nombre_del_lector = "Disponible"


        self.libro.guardar_libro({
            'isbn' : isbn,
            'nombre_del_libro' : nombre,
            'autor' : autor,
            'editorial' : editorial,
            'estado_libro' : estado_libro,
            'nombre_del_lector' : nombre_del_lector
        })
        print('''
        ==============================
            Nuevo libro agregado !
        ==============================
        ''')
        self.listar_libros()

    def buscar_libro(self):
        print('''
        =====================
            Buscar Libro
        =====================
        ''')
        try:
            id_libro = input_data("Ingrese el ID del libro >> ", "int")
            libro = self.libro.obtener_libro({'id_libro' : id_libro})
            print(print_table(libro, ['ID', 'ISBN', 'Nombre del libro', 'Autor', 'Editorial', 'Estado del Libro', 'Nombre del lector']))

            if libro:
                if pregunta("¿Deseas dar mantenimiento al libro?"):
                    opciones = ['Editar libro', 'Eliminar Libro', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_libro(id_libro)
                    elif respuesta == 2:
                        self.eliminar_libro(id_libro)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def editar_libro(self, id_libro):
        nombre = input_data("Ingrese el nuevo nombre del libro >> ")
        autor = input_data("Ingrese el nuevo nombre del autor del libro >> ")
        editorial = input_data("Ingrese la nueva editorial a la cual corresponde el libro >> ")
        self.libro.modificar_libro({
            'id_libro' : id_libro
        }, {
            'nombre_del_libro' : nombre,
            'autor' : autor,
            'editorial' : editorial,
        })
        print('''
        ========================
            Libro Editado !
        ========================
        ''')     

    def eliminar_libro(self, id_libro):
        self.libro.eliminar_libro({
            'id_libro' : id_libro
        })
        print('''
        ========================
            Libro Eliminado !
        ========================
        ''')


