import sqlite3

from app.model.Cliente import Cliente

dbsrc = 'pos.db'


def get_db_clientes():
    clientes = []
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("SELECT * FROM clientes")
    for row in cursor:
        cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[0])
        clientes.append(cliente)
        print(str(cliente))
    return clientes


def db_get_cliente(db_id):
    conn = sqlite3.connect(dbsrc)
    cursor = conn.execute("SELECT * FROM clientes where id = " + db_id)
    row = cursor.fetchone()
    cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[0])
    return cliente


def db_insert_cliente(cliente):
    conn = sqlite3.connect(dbsrc)
    cursor = conn.cursor()
    sql = 'INSERT INTO clientes(dni, nombre, apellido, telefono, direccion) VALUES ( ?,?,?,?,?)'
    values = (cliente.dni, cliente.nombre, cliente.apellido, int(cliente.telefono), cliente.direccion)
    cursor.execute(sql, values)
    conn.commit()
    cliente.idd = cursor.lastrowid
    print("Clientes insertado: " + str(cliente))
    return cliente.idd
