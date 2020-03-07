import sqlite3

from app import Globals
from app.model.Vendido import Vendido

debug: bool = False


def get_all() -> list:
    vendidos = []
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT * FROM vendidos")
    for row in cursor:
        vendido = Vendido(row[1], row[2], row[3], row[4], row[0])
        vendidos.append(vendido)
        if debug:
            print(str(vendido))
    conn.close()
    return vendidos


def get_id_venta(id_venta) -> list:
    vendidos = []
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT * FROM vendidos where id_venta = ?", (str(id_venta),))
    for row in cursor:
        vendido = Vendido(row[1], row[2], row[3], row[4], row[0])
        vendidos.append(vendido)
        if debug:
            print(str(vendido))

    conn.close()
    return vendidos


def get_id(idd) -> Vendido:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT * FROM vendidos where id = ?", (str(idd),))
    row = cursor.fetchone()
    vendido = Vendido(row[1], row[2], row[3], row[4], row[0])
    if debug:
        print(str(vendido))
    conn.close()
    return vendido


def insert(vendido) -> int:
    conn = sqlite3.connect(Globals.db_src)
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


def insert_list(vendidos: list):
    conn = sqlite3.connect(Globals.db_src)
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
    return vendido.idd


def remove_id(idd) -> bool:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("DELETE FROM vendidos where id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Vendido eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(vendido) -> bool:
    return remove_id(vendido.idd)


def update(vendido) -> bool:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.cursor()
    sql = 'UPDATE vendidos SET id_venta=?, id_producto=?,cantidad=?, precio_unidad=? WHERE id = ?'
    values = (vendido.id_venta, vendido.id_producto, vendido.cantidad, vendido.precio_unidad, vendido.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Vendido actualizada: " + str(vendido))
    return cursor.rowcount > 0


def get_total(id_venta) -> int:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT sum(v.cantidad*v.precio_unidad) FROM vendidos v where id_venta = ?", (str(id_venta),))
    total: int = cursor.fetchone()[0]
    conn.close()
    if debug:
        print('Vendido eliminado: ' + str(cursor.rowcount))
    return total
