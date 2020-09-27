from helpers.menu import Menu
from controllers.libro_controller import Libros_controller
from controllers.lector_controller import Lector_controller
from controllers.registrar_controller import Registrar_controller
from controllers.rol_controller import Roles_controller

def iniciar_app():
    try:
        print('''
        ===============================
            Biblioteca - El Grupo 03
        ===============================
        ''')
        menu_inicio = ["admin", "lector", "salir"]
        respuesta = Menu(menu_inicio).show()
        if respuesta == 1:
            rol = Roles_controller()
            rol.inicio_admin()
            if rol.admin:
                menu_principal = ["Registrar","Libros", "Lectores", "Salir"]
                respuesta = Menu(menu_principal).show()
                if respuesta == 1:
                    rol = Roles_controller()
                    rol.menu()
                    if rol.salir:
                        iniciar_app()
                elif respuesta == 2:
                    libro = Libros_controller()
                    libro.menu()
                    if libro.salir:
                        iniciar_app()
                elif respuesta == 3:
                    lector = Lector_controller()
                    lector.menu()
                    if lector.salir:
                        iniciar_app()
                # print("\nGracias por utilizar el sistema\n")

        elif respuesta == 2:
            rol = Roles_controller()
            rol.inicio_lector()
            if rol.admin == False:
                menu_principal = ["Alquilar/Devolver libro", "Salir"]
                respuesta = Menu(menu_principal).show()
                if respuesta == 1:
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