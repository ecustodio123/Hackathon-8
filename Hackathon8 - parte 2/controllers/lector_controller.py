from helpers.helper import input_data, print_table, pregunta, input_isbn, input_fecha, ingresar_dni
from helpers.menu import Menu
from classes.lector import Lector

class Lector_controller:
    def __init__(self):
        self.lector = Lector()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Lector
                ===============
                ''')
                menu = ['Lista lector', 'Buscar lector', "Nuevo lector", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_lector()
                elif respuesta == 2:
                    self.buscar_lector()
                elif respuesta == 3:
                    self.insertar_lector()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_lector(self):
        print('''
        ========================
            Lista de Lectores
        ========================
        ''')
        lectores = self.lector.obtener_lectores('id_lector')
        print(print_table(lectores, ['ID', 'Nombre', 'DNI']))
        input("\nPresione una tecla para continuar...")

    def buscar_lector(self):
        print('''
        =====================
            Buscar Lector
        =====================
        ''')
        try:
            id_lector = input_data("Ingrese el ID del lector >> ", "int")
            lector = self.lector.buscar_lectores({'id_lector': id_lector})
            print(print_table(lector,  ['ID', 'Nombre', 'DNI']))

            if lector:
                if pregunta("¿Deseas actualizar datos del lector?"):
                    opciones = ['Editar lector', 'Eliminar lector', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_lector(id_lector)
                    elif respuesta == 2:
                        self.eliminar_lector(id_lector)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_lector(self):
        nombre = input_data("Ingrese el nombre del lector >> ")
        # dni = input_data("Ingrese el dni del lector >> ")
        dni = ingresar_dni()

        self.lector.guardar_lector({
            'nombre_del_lector': nombre,
            'dni' : dni,
        })
        print('''
        ==============================
            Nuevo lector agregado !
        ==============================
        ''')
        self.listar_lector()

    def editar_lector(self, id_lector):
        nombre = input_data("Ingrese el nuevo nombre del lector >> ")
        # dni = input_data("Ingrese el nuevo dni del lector >> ")
        dni = ingresar_dni()

        self.lector.modificar_lector({
            'id_lector': id_lector
        }, {
            'nombre_del_lector': nombre,
            'dni' : dni
        })
        print('''
        ========================
            lector Editado !
        ========================
        ''')

    def eliminar_lector(self, id_lector):
        self.lector.eliminar_lector({
            'id_lector': id_lector
        })
        print('''
        ========================
            Lector Eliminado !
        ========================
        ''')