import sqlite3

from app.model.Producto import Producto

dbsrc = '../../res/pos.db'


def get_db_productos() -> list:
    productos = []
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("SELECT * FROM productos")
    for row in cursor:
        producto = Producto(row[1], row[2], row[3], row[4], row[0])
        productos.append(producto)
        print(str(producto))
    return productos


def db_get_producto(idd) -> Producto:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("SELECT * FROM productos where id = ?", str(idd))
    row = cursor.fetchone()
    producto = Producto(row[1], row[2], row[3], row[4], row[0])
    return producto


def db_insert_producto(producto) -> int:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.cursor()
    sql = 'INSERT INTO productos(nombre, descripcion, precio, stock) VALUES (?,?,?,?)'
    values = (producto.nombre, producto.descripcion, int(producto.precio), int(producto.stock))
    cursor.execute(sql, values)
    conn.commit()
    producto.idd = cursor.lastrowid
    print("Producto insertado: " + str(producto))
    return producto.idd


def db_remove_producto_id(idd) -> bool:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("DELETE FROM productos where id = ?", str(idd))
    conn.commit()
    print('Producto eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def db_remove_producto(producto) -> bool:
    return db_remove_producto_id(producto.idd)


def db_update_producto(producto) -> bool:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.cursor()
    sql = 'UPDATE productos SET nombre=?, descripcion=?, precio=?, stock=? WHERE id = ?'
    values = (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.idd)
    cursor.execute(sql, values)
    conn.commit()
    print("Producto actualizado: " + str(producto))
    return cursor.rowcount > 0
