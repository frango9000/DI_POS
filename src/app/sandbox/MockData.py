from random import random, randint

from app.data import ClientesDao, ProductosDao, VentasDao, VendidosDao
from app.model.Cliente import Cliente
from app.model.Producto import Producto
from app.model.Vendido import Vendido
from app.model.Venta import Venta


def mock_clientes():
    for i in range(1, 1000):
        Cliente('DNI' + str(i), "Cliente " + str(i), "Apellido " + str(i), i * 555, 'Direccion ' + str(i)).insert()


def mock_productos():
    for i in range(1, 1000):
        Producto('Producto ' + str(i), 'Descripcion ' + str(i), i).insert()


def mock_ventas():
    vendidos = list()
    for year in range(2019, 2020):
        print("Start year " + str(year))
        for month in range(1, 13):
            print("Start month " + str(month))
            for day in range(1, 29):
                print("Start day " + str(day))
                for i in range(1, 6):
                    month_str = str(month) if len(str(month)) > 1 else str(0) + str(month)
                    day_str = str(day) if len(str(day)) > 1 else str(0) + str(day)
                    id_venta = Venta(randint(1, 999), str(year) + '-' + month_str + '-' + day_str).insert()
                    for j in range(1, 6):
                        vendidos.append(Vendido(id_venta, randint(1, 999), 1, randint(1, 8)))
    print('insertando ' + str(len(vendidos)) + ' vendidos')
    VendidosDao.insert_list(vendidos)
    print('insercion terminada')

# mock_clientes()
# mock_productos()
# mock_ventas()
