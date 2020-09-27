from connection.conn import Conexion

class Libro:
    def __init__(self):
        self.model = Conexion('informacion_libro')

    def guardar_libro(self, libro):
        return self.model.insert(libro)

    def obtener_libro(self, id_libro):
        return self.model.get_by_id(id_libro)

    def obtener_libros(self, order):
        return self.model.get_all(order)

    def buscar_libros(self, data_libro):
        return self.model.get_by_column(data_libro)

    def modificar_libro(self, id_libro, data_libro):
        return self.model.update(id_libro, data_libro)

    def eliminar_libro(self, id_libro):
        return self.model.delete(id_libro)
    
    def buscar_libro_like(self, data_libro):
        return self.model.where_like(data_libro)
