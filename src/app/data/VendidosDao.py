from src.app.data import GenericDao
from src.app.model.Vendido import Vendido

debug: bool = GenericDao.debug


def get_all() -> list:
    """
    Obtiene una lista con todos los vendidos existentes en la base de datos
    :return: lista de Vendidos
    :rtype: list
    """
    vendidos = []
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM vendidos")
    for row in cursor:
        vendido = Vendido(row[1], row[2], row[3], row[4], row[0])
        vendidos.append(vendido)
        if debug:
            print(str(vendido))
    conn.close()
    return vendidos


def get_id(idd: int) -> Vendido:
    """
    Buscar 1 vendido en la base de datos proporcionando el id
    :param idd: id del vendido
    :type idd: int
    :return: Vendido con idd, si existe
    :rtype: Vendido
    """
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM vendidos where id = ?", (str(idd),))
    row = cursor.fetchone()
    vendido = Vendido(row[1], row[2], row[3], row[4], row[0])
    if debug:
        print(str(vendido))
    conn.close()
    return vendido


def insert(vendido: Vendido) -> int:
    """
    Inserta un nuevo vendido en la base de datos
    :param vendido: el vendido a insertar
    :type vendido: Vendido
    :return: el id generado para el vendido insertado
    :rtype: int
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    sql = 'INSERT INTO vendidos(id_venta, id_producto, cantidad, precio_unidad) VALUES (?,?,?,?)'
    values = (int(vendido.id_venta), str(vendido.id_producto), int(vendido.cantidad), str(vendido.precio_unidad))
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    vendido.idd = cursor.lastrowid
    if debug:
        print("Vendido insertado: " + str(vendido))
    return vendido.idd


def remove_id(idd: int) -> bool:
    """
    Elimina un vendido de la base de datos en por su id
    :param idd: id del vendido a eliminar
    :type idd: int
    :return: True si fue eliminado
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.execute("DELETE FROM vendidos where id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Vendido eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(vendido: Vendido) -> bool:
    """
    Elimina un vendido de la base de datos en por su objeto
    :param vendido: vendido a eliminar
    :type vendido: Vendido
    :return: True si fue eliminado
    :rtype: bool
    """
    return remove_id(vendido.idd)


def update(vendido: Vendido) -> bool:
    """
    Actualiza los datos de un objeto Vendido a la representación en base de datos
    :param vendido: vendido a actualizar
    :type vendido: Vendido
    :return: True si hubo modificaciones
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    sql = 'UPDATE vendidos SET id_venta=?, id_producto=?,cantidad=?, precio_unidad=? WHERE id = ?'
    values = (vendido.id_venta, vendido.id_producto, vendido.cantidad, vendido.precio_unidad, vendido.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Vendido actualizada: " + str(vendido))
    return cursor.rowcount > 0


def insert_list(vendidos: list) -> int:
    """
    Metodo de ayuda para insertar una lista de Productos Vendidos
    :param vendidos: lista de vendidos a insertar
    :type vendidos: list<Vendido>
    :return: numero de inserciones realizadas
    :rtype: int
    """
    conn = GenericDao.connect()
    sum = 0
    for vendido in vendidos:
        cursor = conn.cursor()
        sql = 'INSERT INTO vendidos(id_venta, id_producto, cantidad, precio_unidad) VALUES (?,?,?,?)'
        values = (int(vendido.id_venta), str(vendido.id_producto), int(vendido.cantidad), str(vendido.precio_unidad))
        cursor.execute(sql, values)
        sum += 1
    conn.commit()
    conn.close()
    if debug:
        print("Vendidos insertados: " + str(sum))
    return sum


def get_id_venta(id_venta: int) -> list:
    """
    genera una lista de todos los productos vendidos asociados a una venta determinada por su id_venta
    :param id_venta: id de la venta
    :type id_venta: int
    :return: lista de productos vendidos
    :rtype: list<Vendido>
    """
    vendidos = []
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM vendidos where id_venta = ?", (str(id_venta),))
    for row in cursor:
        vendido = Vendido(row[1], row[2], row[3], row[4], row[0])
        vendidos.append(vendido)
        if debug:
            print(str(vendido))

    conn.close()
    return vendidos


def get_total(id_venta: int) -> int:
    """
    calcula el total  del importe de una venta buscando el costo de cada item asociado y retornando la suma total
    :param id_venta: id de la venta
    :type id_venta: int
    :return: suma total
    :rtype: int
    """
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT sum(v.cantidad*v.precio_unidad) FROM vendidos v where id_venta = ?", (str(id_venta),))
    total: int = cursor.fetchone()[0]
    conn.close()
    if debug:
        print('Vendido eliminado: ' + str(cursor.rowcount))
    return total
