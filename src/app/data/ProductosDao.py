from src.app.data import GenericDao
from src.app.model.Producto import Producto

debug: bool = GenericDao.debug


def get_all() -> list:
    """
    Obtiene una lista con todos los productos existentes en la base de datos
    :return: lista de Productos
    :rtype: list
    """
    productos = []
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM productos")
    for row in cursor:
        producto = Producto(row[1], row[2], row[3], row[4], row[0])
        productos.append(producto)
        if debug:
            print(str(producto))
    conn.close()
    return productos


def get_id(idd: int) -> Producto:
    """
    Buscar 1 producto en la base de datos proporcionando el id
    :param idd: id del producto
    :type idd: int
    :return: Producto con idd, si existe
    :rtype: Producto
    """
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM productos where id = ?", (str(idd),))
    row = cursor.fetchone()
    producto = Producto(row[1], row[2], row[3], row[4], row[0])
    conn.close()

    if debug:
        print(str(producto))
    return producto


def insert(producto: Producto) -> int:
    """
    Inserta un nuevo producto en la base de datos
    :param producto: el producto a insertar
    :type producto: Producto
    :return: el id generado para el producto insertado
    :rtype: int
    """
    conn = GenericDao.connect()
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


def remove_id(idd: int) -> bool:
    """
    Elimina un producto de la base de datos en por su id
    :param idd: id del producto a eliminar
    :type idd: int
    :return: True si fue eliminado
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.execute("DELETE FROM productos where id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Producto eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(producto: Producto) -> bool:
    """
    Elimina un producto de la base de datos en por su objeto
    :param producto: producto a eliminar
    :type producto: Producto
    :return: True si fue eliminado
    :rtype: bool
    """
    return remove_id(producto.idd)


def update(producto: Producto) -> bool:
    """
    Actualiza los datos de un objeto Producto a la representación en base de datos
    :param producto: producto a actualizar
    :type producto: Producto
    :return: True si hubo modificaciones
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    sql = 'UPDATE productos SET nombre=?, descripcion=?, precio=?, stock=? WHERE id = ?'
    values = (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Producto actualizado: " + str(producto))
    return cursor.rowcount > 0


def get_mapped() -> dict:
    """
    Genera un mapa de id => Producto con todos los productos en la base de datos
    :return: Mapa de Productos
    :rtype: dict
    """
    mapped = dict()
    productos = get_all()
    for producto in productos:
        mapped[producto.idd] = producto.nombre
    return mapped
