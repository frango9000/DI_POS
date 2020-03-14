import sqlite3

from src.app import Globals

"""
variable que determina si se imprimen las sentencias sql (debugging)
"""
debug: bool = False


def connect() -> sqlite3.Connection:
    """
    inicia la conexion a la base de datos activando las restricciones de foreign keys
    :return: la conexion hecha a la base de datos
    :rtype: sqlite3.Connection
    """
    conn = sqlite3.connect(Globals.db_src)
    conn.execute('PRAGMA foreign_keys=1;')
    return conn
