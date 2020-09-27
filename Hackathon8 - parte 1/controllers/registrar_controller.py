from helpers.helper import input_data, print_table, pregunta, input_isbn, input_fecha
from helpers.menu import Menu
from classes.lector import Lector
from classes.libro import Libro

class Registrar_controller:
    def __init__(self):
        self.lector = Lector()
        self.libro = Libro()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                =======================
                    Registrar Libros
                =======================
                ''')
                menu = ["Prestar Libro", "Devolver Libro", "Salir"]
                respuesta = Menu(menu).show()
                if respuesta == 1:
                    self.prestar_libros()
                elif respuesta == 2:
                    self.devovler_libros()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')        
    
    def prestar_libros(self):
        print('''
        =============================================
            Entregar libro al lector
        =============================================
        ''')
        libro_deseado = input_data("Introduzca el libro que está buscando >>")
        buscar_libro = self.libro.buscar_libro_like(libro_deseado)
        if not buscar_libro:
            print('\nEl Libro elegido no existe !')
            return
        if buscar_libro[5] == "No Disponible":
            print('\nEl Libro ha sido prestado a otro lector !')
            return
        print(f'\nElija el ID del lector al cual se le va prestar el libro {buscar_libro[2]} >> ')
        lectores = self.lector.obtener_lectores('id_lector')
        print(print_table(lectores,  ['ID', 'Nombre', 'DNI', 'Nombre del libro', 'ID_Estado_Servicio']))
        id_lector_elegido = input_data("\nEscriba el ID del alumno >> ", "int")
        buscar_lector = self.lector.obtener_lector({'id_lector' : id_lector_elegido})
        if not buscar_lector:
            print('\nEl Lector elegido no existe !')
            return
        self.libro.modificar_libro({
            'id_libro' : buscar_libro[0]
        }, {
            'estado_libro' : "No Disponible",
            'nombre_del_lector' : buscar_lector[1]
        })
        print('''
        ========================
            Libro Prestado !
        ========================
        ''')    
    
    def devovler_libros(self):
        print('''
        ==================================================
            Devovler libro a Biblioteca -  Grupo 03
        ==================================================
        ''')
        libro_devuelto = input_data("Introduzca el libro que está devolviendo >>")
        buscar_libro = self.libro.buscar_libro_like(libro_devuelto)
        if not buscar_libro:
            print('\nEl Libro que esta devolviendo no existe en nuestra base de datos, verifique bien !')
            return
        if buscar_libro[5] == "Disponible":
            print(f'\nNosotros no hemos prestado el libro {buscar_libro[2]}, ya que lo tenemos en nuestro almacen. Verifique bien!')
            return
        # print(f'\nPor favor introduzca su ID de lector para poder proceder a dar la devolución del libro {buscar_libro[2]} >> ')
        # lectores = self.lector.obtener_lectores('id_lector')
        # print(print_table(lectores,  ['ID', 'Nombre', 'DNI', 'Nombre del libro', 'ID_Estado_Servicio']))
        id_lector_elegido = input_data("\nPor favor identifiquese y escriba su ID de lector >> ", "int")
        lector = self.lector.obtener_lector({'id_lector' : id_lector_elegido})
        if buscar_libro[6] != lector[1]:
            print(f'\nEn nuestra base de datos, tenemos que se le presto a {buscar_libro[6]}, y usted no es el/ella. Verifique bien!')
            return 
        # buscar_lector = self.lector.obtener_lector({'id_lector' : id_lector_elegido})
        # if not buscar_lector:
            # print('\nSu ID de lector no coincide con ninguno de nuestro registro de base de datos, verifique colocar bien su ID !')
            # return
        self.libro.modificar_libro({
            'id_libro' : buscar_libro[0]
        }, {
            'estado_libro' : "Disponible",
            'nombre_del_lector' : "Disponible"
        })
        print('''
        ========================
            Libro Devuelto !
        ========================
        ''')            

        
            

