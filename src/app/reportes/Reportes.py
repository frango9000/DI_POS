from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, Spacer, SimpleDocTemplate, Table

from app import Globals
from app.data import VentasDao, ClientesDao, ProductosDao, VendidosDao

"""
Scripts de generacion de reportes
"""


def generar_factura(id_venta: int, nombre_archivo: str):
    """
    recibe el id de venta y busca el obj en base de datos, y genera una
    factura con los datos de la tienda y del cliente, todos los cargos
    de la factura y el total y la guarda en la ubicacion suministrada en pdf

    :param id_venta:
    :type id_venta:
    :param nombre_archivo:
    :type nombre_archivo:
    :return:
    :rtype:
    """
    venta = VentasDao.get_id(id_venta)
    cliente = ClientesDao.get_id(venta.id_cliente)
    vendidos = VendidosDao.get_id_venta(id_venta)
    productos_map = ProductosDao.get_mapped()

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


def generar_reporte_diario(dia: int, mes: int, ano: int, nombre_archivo: str):
    """
    recibe el dia, mes y año, busca la lista de ventas de ese dia en
    base de datos, y genera una lista resumida de dichas ventas
    y su suma total y la guarda en la ubicacion suministrada en pdf

    :param dia:
    :type dia:
    :param mes:
    :type mes:
    :param ano:
    :type ano:
    :param nombre_archivo:
    :type nombre_archivo:
    :return:
    :rtype:
    """
    ventas = VentasDao.get_dia(dia, mes, ano)

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
    guion.append(Paragraph("Resumen de ventas del: " + str(dia) + '/' + str(mes) + '/' + str(ano), div_cliente))

    guion.append(Spacer(0, 40))

    datos = [['Id Venta', 'ID cliente', 'Fecha Hora', 'Total venta']]
    sum = 0

    for venta in ventas:
        venta_total = VendidosDao.get_total(venta.idd)
        sum += venta_total
        row = [venta.idd, venta.id_cliente, venta.fecha_hora, str(venta_total) + " €"]
        datos.append(row)

    tabla = Table(datos)

    guion.append(tabla)

    guion.append(Spacer(0, 80))

    guion.append(Paragraph("Total dia:                                 " + str(sum) + "€", hoja_estilo['BodyText']))

    doc = SimpleDocTemplate(nombre_archivo, pagesize=A4, showBoundary=0)
    doc.build(guion)


def generar_reporte_mensual(mes: int, ano: int, nombre_archivo: str):
    """
    recibe el mes y año, busca la lista de ventas de ese mes en
    base de datos, y genera una lista resumida de dichas ventas
    y su suma total y la guarda en la ubicacion suministrada en pdf

    :param mes:
    :type mes:
    :param ano:
    :type ano:
    :param nombre_archivo:
    :type nombre_archivo:
    :return:
    :rtype:
    """
    ventas = VentasDao.get_mes(mes, ano)

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
    guion.append(Paragraph("Resumen de ventas del: " + str(mes) + '/' + str(ano), div_cliente))

    guion.append(Spacer(0, 40))

    datos = [['Id Venta', 'ID cliente', 'Fecha Hora', 'Total venta']]
    sum = 0

    for venta in ventas:
        venta_total = VendidosDao.get_total(venta.idd)
        sum += venta_total
        row = [venta.idd, venta.id_cliente, venta.fecha_hora, str(venta_total) + " €"]
        datos.append(row)

    tabla = Table(datos)

    guion.append(tabla)

    guion.append(Spacer(0, 80))

    guion.append(Paragraph("Total mes:                                 " + str(sum) + "€", hoja_estilo['BodyText']))

    doc = SimpleDocTemplate(nombre_archivo, pagesize=A4, showBoundary=0)
    doc.build(guion)
