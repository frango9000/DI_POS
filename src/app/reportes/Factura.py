import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, Spacer, SimpleDocTemplate, Table

from app import Globals
from app.data import VentasDao, ClientesDao, ProductosDao, VendidosDao


def generar_factura(id_venta: int, nombre_archivo: str):
    venta = VentasDao.get_id(id_venta)
    cliente = ClientesDao.get_id(venta.id_cliente)
    vendidos = VendidosDao.get_id_venta(id_venta)
    productos_map = ProductosDao.get_mapped()
    print(len(vendidos))

    hoja_estilo = getSampleStyleSheet()
    guion = []
    logo_img = Image(Globals.logo_src, width=100, height=100)
    guion.append(logo_img)
    guion.append(Spacer(0, -100))

    heading = hoja_estilo['Heading3']
    guion.append(Paragraph("NIF: B1327869", heading))
    guion.append(Paragraph("Tienda SL", heading))
    guion.append(Paragraph("Vigo", heading))
    guion.append(Paragraph("986424242", heading))
    guion.append(Spacer(0, 40))

    div_cliente = hoja_estilo['BodyText']
    guion.append(Paragraph("Factura # " + str(venta.idd), div_cliente))
    guion.append(Paragraph("Fecha  " + venta.fecha_hora, div_cliente))

    guion.append(Spacer(0, 20))

    cliente_dni = Paragraph("Cliente: " + cliente.dni, div_cliente)
    cliente_nombre = Paragraph("Nombre: " + cliente.nombre + " " + cliente.apellido, div_cliente)
    cliente_telefono = Paragraph("Telefono: " + str(cliente.telefono), div_cliente)
    guion.append(cliente_dni)
    guion.append(cliente_nombre)
    guion.append(cliente_telefono)

    guion.append(Spacer(0, 40))

    datos = [['Id Vendido', 'Producto', 'Cantidad', 'Precio Unidad']]
    sum = 0
    for vendido in vendidos:
        sum += (vendido.cantidad * vendido.precio_unidad)
        row = [vendido.idd, str(productos_map[vendido.id_producto]), str(vendido.cantidad),
               str(vendido.precio_unidad) + "€"]
        datos.append(row)
    tabla = Table(datos)

    guion.append(tabla)

    guion.append(Spacer(0, 80))

    guion.append(Paragraph("Total :                                 " + str(sum) + "€", hoja_estilo['BodyText']))

    doc = SimpleDocTemplate(nombre_archivo, pagesize=A4, showBoundary=0)
    doc.build(guion)
