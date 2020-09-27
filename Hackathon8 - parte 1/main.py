from helpers.menu import Menu
from controllers.libro_controller import Libros_controller
from controllers.lector_controller import Lector_controller
from controllers.registrar_controller import Registrar_controller

def iniciar_app():
    try:
        print('''
        ===============================
            Biblioteca - El Grupo 03
        ===============================
        ''')
        menu_principal = ["Libros", "Lectores", "Registro", "Salir"]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            libro = Libros_controller()
            libro.menu()
            if libro.salir:
                iniciar_app()
        elif respuesta == 2:
            lector = Lector_controller()
            lector.menu()
            if lector.salir:
                iniciar_app()
        elif respuesta == 3:
            registro = Registrar_controller()
            registro.menu()
            if registro.salir:
                iniciar_app()
        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()