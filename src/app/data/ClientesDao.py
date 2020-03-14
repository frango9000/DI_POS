import sqlite3

from app.data import GenericDao
from src.app import Globals
from src.app.model.Cliente import Cliente

debug: bool = GenericDao.debug


def get_all() -> list:
    """
    Obtiene una lista con todos los clientes existentes en la base de datos
    :return: lista de Clientes
    :rtype: list
    """
    clientes = []
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM clientes")
    for row in cursor:
        cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[0])
        clientes.append(cliente)
        if debug:
            print(str(cliente))
    conn.close()
    return clientes


def get_id(idd: int) -> Cliente:
    """
    Buscar 1 cliente en la base de datos proporcionando el id
    :param idd: id del cliente
    :type idd: int
    :return: Cliente con idd, si existe
    :rtype: Cliente
    """
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM clientes where id = ?", (str(idd),))
    row = cursor.fetchone()
    cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[0])
    conn.close()
    if debug:
        print(str(cliente))
    return cliente


def insert(cliente: Cliente) -> int:
    """
    Inserta un nuevo cliente en la base de datos
    :param cliente: el cliente a insertar
    :type cliente: Cliente
    :return: el id generado para el cliente insertado
    :rtype: int
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    sql = 'INSERT INTO clientes(dni, nombre, apellido, telefono, direccion) VALUES ( ?,?,?,?,?)'
    values = (cliente.dni, cliente.nombre, cliente.apellido, int(cliente.telefono), cliente.direccion)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    cliente.idd = cursor.lastrowid
    if debug:
        print("Clientes insertado: " + str(cliente))
    return cliente.idd


def remove_id(idd: int) -> bool:
    """
    Elimina un cliente de la base de datos en por su id
    :param idd: id del cliente a eliminar
    :type idd: int
    :return: True si fue eliminado
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.execute("DELETE FROM clientes where id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Cliente eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(cliente: Cliente) -> bool:
    """
    Elimina un cliente de la base de datos en por su objeto
    :param cliente: cliente a eliminar
    :type cliente: Cliente
    :return: True si fue eliminado
    :rtype: bool
    """
    return remove_id(cliente.idd)


def update(cliente: Cliente) -> bool:
    """
    Actualiza los datos de un objeto Cliente a la representación en base de datos
    :param cliente: cliente a actualizar
    :type cliente: Cliente
    :return: True si hubo modificaciones
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    sql = 'UPDATE clientes SET dni=?, nombre=?, apellido=?, telefono=?, direccion=? WHERE id = ?'
    values = (cliente.dni, cliente.nombre, cliente.apellido, cliente.telefono, cliente.direccion, cliente.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Cliente actualizado: " + str(cliente))
    return cursor.rowcount > 0
