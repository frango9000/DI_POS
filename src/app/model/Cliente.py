from app.data import ClientesDao


class Cliente:

    def __init__(self, dni, nombre, apellido, telefono, direccion, idd=0):
        self.idd = idd
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion

    def insert(self):
        return ClientesDao.db_insert_cliente(self)

    def remove(self):
        return ClientesDao.db_remove_cliente(self)

    def update(self):
        return ClientesDao.db_update_cliente(self)

    def __str__(self) -> str:
        return 'Cliente { ' + str(self.idd) + ', ' + self.dni + ', ' + self.nombre + ', ' + self.apellido + ', ' + str(
            self.telefono) + ', ' + self.direccion + ' };'
