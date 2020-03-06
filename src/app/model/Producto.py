from app.data import ProductosDao


class Producto:

    def __init__(self, nombre, descripcion, precio=0, stock=0, idd=0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.idd = idd

    def insert(self):
        return ProductosDao.insert(self)

    def remove(self):
        return ProductosDao.remove(self)

    def update(self):
        return ProductosDao.update(self)

    def __str__(self) -> str:
        return 'Producto { ' + \
               str(self.idd) + ', ' + \
               self.nombre + ', ' + \
               str(self.precio) + ', ' + \
               self.descripcion + ' };'
