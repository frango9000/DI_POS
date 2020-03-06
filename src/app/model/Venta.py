from app.data import VentasDao


class Venta:

    def __init__(self, id_cliente, fecha_hora=None, idd=0):
        self.idd: int = idd
        self.id_cliente: int = id_cliente
        self.fecha_hora: str = fecha_hora

    def insert(self):
        return VentasDao.insert(self)

    def remove(self):
        return VentasDao.remove(self)

    def update(self):
        return VentasDao.update(self)

    def __str__(self) -> str:
        return 'Venta { ' + \
               str(self.idd) + ', ' + \
               str(self.id_cliente) + ', ' + \
               str(self.fecha_hora) + ' };'
