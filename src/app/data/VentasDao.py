import sqlite3

from app.model.Venta import Venta

dbsrc = '../../res/pos.db'


def get_all() -> list:
    ventas = []
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("SELECT * FROM ventas")
    for row in cursor:
        venta = Venta(row[1], row[2], row[0])
        ventas.append(venta)
        print(str(venta))
    return ventas


def get_id(idd) -> Venta:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("SELECT * FROM ventas where id = ?", str(idd))
    row = cursor.fetchone()
    venta = Venta(row[1], row[2], row[0])
    return venta


def insert(venta) -> int:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.cursor()
    sql = 'INSERT INTO ventas(id_cliente, fechahora) VALUES (?,?)'
    values = (int(venta.id_cliente), str(venta.fechahora))
    cursor.execute(sql, values)
    conn.commit()
    venta.idd = cursor.lastrowid
    print("Venta insertada: " + str(venta))
    return venta.idd


def remove_id(idd) -> bool:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("DELETE FROM ventas where id = ?", str(idd))
    conn.commit()
    print('Venta eliminada: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(venta) -> bool:
    return remove_id(venta.idd)


def update(venta) -> bool:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.cursor()
    sql = 'UPDATE ventas SET id_cliente=?, fechahora=? WHERE id = ?'
    values = (venta.id_cliente, venta.fechahora, venta.idd)
    cursor.execute(sql, values)
    conn.commit()
    print("Venta actualizada: " + str(venta))
    return cursor.rowcount > 0
