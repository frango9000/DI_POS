from app.data import VendidosDao


class Vendido:
    """
    Clase modelo de cada producto vendido
    """

    def __init__(self, id_venta, id_producto, cantidad, precio_unidad, idd=0):
        """
        Constructor unico, un objeto de este tipo ser inicializara
        con id 0 y al insertarse en sqlite se le asigna un id

        :param id_venta:
        :type id_venta:
        :param id_producto:
        :type id_producto:
        :param cantidad:
        :type cantidad:
        :param precio_unidad:
        :type precio_unidad:
        :param idd:
        :type idd:
        """
        self.idd = idd
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unidad = precio_unidad

    def insert(self):
        """
        insertar en base de datos
        :param self:
        :type self:
        :return: id asignado
        :rtype: int
        """
        return VendidosDao.insert(self)

    def remove(self):
        """
        eliminar de la base de datos
        :param self:
        :type self:
        :return: confirmacion de eliminacion
        :rtype: bool
        """
        return VendidosDao.remove(self)

    def update(self):
        """
        actualizar en base de datos

        :param self:
        :type self:
        :return: confirmacion de actualizacion
        :rtype: bool
        """
        return VendidosDao.update(self)

    def __str__(self) -> str:
        return 'Vendido { ' + \
               str(self.idd) + ', ' + \
               str(self.id_venta) + ', ' + \
               str(self.id_producto) + ', ' + \
               str(self.cantidad) + ', ' + \
               str(self.precio_unidad) + ' };'
