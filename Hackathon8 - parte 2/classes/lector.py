from connection.conn import Conexion

class Lector:
    def __init__(self):
        self.model = Conexion('informacion_lector')

    def guardar_lector(self, lector):
        return self.model.insert(lector)

    def obtener_lector(self, id_lector):
        return self.model.get_by_id(id_lector)

    def obtener_lectores(self, order):
        return self.model.get_all(order)

    def buscar_lectores(self, data_lector):
        return self.model.get_by_column(data_lector)

    def modificar_lector(self, id_lector, data_lector):
        return self.model.update(id_lector, data_lector)

    def eliminar_lector(self, id_lector):
        return self.model.delete(id_lector)
