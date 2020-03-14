from src.app.data import GenericDao
from src.app.model.Venta import Venta

debug: bool = GenericDao.debug


def get_all() -> list:
    """
    Obtiene una lista con todos los ventas existentes en la base de datos
    :return: lista de Ventas
    :rtype: list
    """
    ventas = []
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM ventas")
    for row in cursor:
        venta = Venta(row[1], row[2], row[0])
        ventas.append(venta)
        if debug:
            print(str(venta))

    conn.close()
    return ventas


def get_id(idd: int) -> Venta:
    """
    Buscar 1 venta en la base de datos proporcionando el id
    :param idd: id del venta
    :type idd: int
    :return: Venta con idd, si existe
    :rtype: Venta
    """
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM ventas where id = ?", (str(idd),))
    row = cursor.fetchone()
    venta = Venta(row[1], row[2], row[0])
    if debug:
        print(str(venta))

    conn.close()
    return venta


def insert(venta: Venta) -> int:
    """
    Inserta un nuevo venta en la base de datos
    :param venta: el venta a insertar
    :type venta: Venta
    :return: el id generado para el venta insertado
    :rtype: int
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    if (venta.fecha_hora is None):
        sql = 'INSERT INTO ventas(id_cliente) VALUES (?)'
        values = (int(venta.id_cliente),)
    else:
        sql = 'INSERT INTO ventas(id_cliente, fecha_hora) VALUES (?,datetime(?))'
        values = (int(venta.id_cliente), venta.fecha_hora)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    venta.idd = cursor.lastrowid
    if debug:
        print("Venta insertada: " + str(venta))
    return venta.idd


def remove_id(idd: int) -> bool:
    """
    Elimina un venta de la base de datos en por su id
    :param idd: id del venta a eliminar
    :type idd: int
    :return: True si fue eliminado
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.execute("DELETE FROM ventas where id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Venta eliminada: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(venta: Venta) -> bool:
    """
    Elimina un venta de la base de datos en por su objeto
    :param venta: venta a eliminar
    :type venta: Venta
    :return: True si fue eliminado
    :rtype: bool
    """
    return remove_id(venta.idd)


def update(venta: Venta) -> bool:
    """
    Actualiza los datos de un objeto Venta a la representación en base de datos
    :param venta: venta a actualizar
    :type venta: Venta
    :return: True si hubo modificaciones
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    sql = 'UPDATE ventas SET id_cliente=?, fecha_hora=? WHERE id = ?'
    values = (venta.id_cliente, venta.fecha_hora, venta.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Venta actualizada: " + str(venta))
    return cursor.rowcount > 0


def get_dia(dia: int, mes: int, ano: int) -> list:
    """
    Genera una lista con todas las ventas de el dia/mes/año seleccionado
    :param dia: dia
    :type dia: int
    :param mes: mes
    :type mes: int
    :param ano: año
    :type ano: int
    :return: lista de Ventas filtradas por dia
    :rtype: list<Venta>
    """
    ventas = []
    conn = GenericDao.connect()
    month_str = str(mes) if len(str(mes)) > 1 else str(0) + str(mes)
    day_str = str(dia) if len(str(dia)) > 1 else str(0) + str(dia)
    date = str(ano) + "-" + month_str + "-" + day_str
    sql = "select * from ventas where date(fecha_hora) = date(?)"
    cursor = conn.execute(sql, (date,))
    for row in cursor:
        venta = Venta(row[1], row[2], row[0])
        ventas.append(venta)
        if debug:
            print(str(venta))
    conn.close()
    return ventas


def get_mes(mes: int, ano: int) -> list:
    """
    Genera una lista con todas las ventas de el mes/año seleccionado
    :param mes: mes
    :type mes: int
    :param ano: año
    :type ano: int
    :return: lista de ventas filtradas por mes
    :rtype: list<Venta>
    """
    ventas = []
    conn = GenericDao.connect()
    sql = "select * from ventas where date(fecha_hora) >= date(?) and date(fecha_hora) < date(?, 'start of month', '+1 months', 'start of month')"
    month_str = str(mes) if len(str(mes)) > 1 else str(0) + str(mes)
    date = str(ano) + '-' + month_str + '-01'
    values = (date, date)
    cursor = conn.execute(sql, values)
    for row in cursor:
        venta = Venta(row[1], row[2], row[0])
        ventas.append(venta)
        if debug:
            print(str(venta))
    conn.close()
    return ventas
