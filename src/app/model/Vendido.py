from app.data import VendidosDao


class Vendido:

    def __init__(self, id_venta, id_producto, cantidad, precio_unidad, idd=0):
        self.idd = idd
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unidad = precio_unidad

    def insert(self):
        return VendidosDao.insert(self)

    def remove(self):
        return VendidosDao.remove(self)

    def update(self):
        return VendidosDao.update(self)

    def __str__(self) -> str:
        return 'Vendido { ' + \
               str(self.idd) + ', ' + \
               str(self.id_venta) + ', ' + \
               str(self.id_producto) + ', ' + \
               str(self.cantidad) + ', ' + \
               str(self.precio_unidad) + ' };'
