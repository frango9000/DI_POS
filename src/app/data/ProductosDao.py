import sqlite3

from app import Globals
from app.model.Producto import Producto

debug: bool = False


def get_all() -> list:
    productos = []
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT * FROM productos")
    for row in cursor:
        producto = Producto(row[1], row[2], row[3], row[4], row[0])
        productos.append(producto)
        if debug:
            print(str(producto))
    conn.close()
    return productos


def get_mapped() -> dict:
    mapped = dict()
    productos = get_all()
    for producto in productos:
        mapped[producto.idd] = producto.nombre
    return mapped


def get_id(idd) -> Producto:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT * FROM productos where id = ?", (str(idd),))
    row = cursor.fetchone()
    producto = Producto(row[1], row[2], row[3], row[4], row[0])
    conn.close()

    if debug:
        print(str(producto))
    return producto


def insert(producto) -> int:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.cursor()
    sql = 'INSERT INTO productos(nombre, descripcion, precio, stock) VALUES (?,?,?,?)'
    values = (producto.nombre, producto.descripcion, int(producto.precio), int(producto.stock))
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    producto.idd = cursor.lastrowid

    if debug:
        print("Producto insertado: " + str(producto))
    return producto.idd


def remove_id(idd) -> bool:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("DELETE FROM productos where id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Producto eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(producto) -> bool:
    return remove_id(producto.idd)


def update(producto) -> bool:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.cursor()
    sql = 'UPDATE productos SET nombre=?, descripcion=?, precio=?, stock=? WHERE id = ?'
    values = (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Producto actualizado: " + str(producto))
    return cursor.rowcount > 0
