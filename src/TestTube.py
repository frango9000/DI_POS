import app.data.ClientesDao as Db
from app.model.Cliente import Cliente

cliente1 = Cliente('53K', 'Francisco', 'Sanchez', 123456, 'Vigo')
cliente1.insert()

# Db.db_insert_cliente(cliente1)


str(Db.get_all())
