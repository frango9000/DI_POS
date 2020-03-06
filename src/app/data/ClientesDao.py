import sqlite3

from app.model.Cliente import Cliente

dbsrc = '../../res/pos.db'


def get_db_clientes() -> list:
    clientes = []
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("SELECT * FROM clientes")
    for row in cursor:
        cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[0])
        clientes.append(cliente)
        print(str(cliente))
    return clientes


def db_get_cliente(idd) -> Cliente:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("SELECT * FROM clientes where id = " + str(idd))
    row = cursor.fetchone()
    cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[0])
    return cliente


def db_insert_cliente(cliente) -> int:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.cursor()
    sql = 'INSERT INTO clientes(dni, nombre, apellido, telefono, direccion) VALUES ( ?,?,?,?,?)'
    values = (cliente.dni, cliente.nombre, cliente.apellido, int(cliente.telefono), cliente.direccion)
    cursor.execute(sql, values)
    conn.commit()
    cliente.idd = cursor.lastrowid
    print("Clientes insertado: " + str(cliente))
    return cliente.idd


def db_remove_cliente_id(idd) -> bool:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("DELETE FROM clientes where id = ?", str(idd))
    conn.commit()
    print('Cliente eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def db_remove_cliente(cliente) -> bool:
    return db_remove_cliente_id(cliente.idd)


def db_update_cliente(cliente) -> bool:
    conn = sqlite3.connect(dbsrc)
    cursor = conn.cursor()
    sql = 'UPDATE clientes SET dni=?, nombre=?, apellido=?, telefono=?, direccion=? WHERE id = ?'
    values = (cliente.dni, cliente.nombre, cliente.apellido, cliente.telefono, cliente.direccion, cliente.idd)
    cursor.execute(sql, values)
    conn.commit()
    print("Cliente actualizado: " + str(cliente))
    return cursor.rowcount > 0
