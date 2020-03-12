import sqlite3

from app import Globals


class SessionDB:

    def __init__(self):
        self.conn: sqlite3.Connection
        self.auto_close: bool = True

    def getConnection(self) -> sqlite3.Connection:
        self.conn = sqlite3.connect(Globals.db_src)
        return self.conn

    def closeConnection(self):
        self.conn.close()

    def setAutoClose(self, auto_close: bool):
        self.auto_close = auto_close
