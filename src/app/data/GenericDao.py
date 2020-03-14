import sqlite3

from app import Globals

debug: bool = False


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(Globals.db_src)
    conn.execute('PRAGMA foreign_keys=1;')
    return conn
