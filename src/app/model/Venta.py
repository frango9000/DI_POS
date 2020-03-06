from app.data import VentasDao


class Venta:

    def __init__(self, id_cliente, fechahora, idd=0):
        self.idd = idd
        self.id_cliente = id_cliente
        self.fechahora = fechahora

    def insert(self):
        return VentasDao.insert(self)

    def remove(self):
        return VentasDao.remove(self)

    def update(self):
        return VentasDao.update(self)

    def __str__(self) -> str:
        return 'Venta { ' + str(self.idd) + ', ' + str(self.id_cliente) + ', ' + str(self.fechahora) + ' };'
