from app.reportes import Reportes


def reporte_anual(ano: int):
    for i in range(1, 13):
        Reportes.generar_reporte_mensual(i, 2019, 'reportes/' + str(ano) + '-' + str(i) + '.pdf')
        for j in range(1, 29):
            Reportes.generar_reporte_diario(j, i, 2019, 'reportes/' + str(ano) + '-' + str(i) + '-' + str(j) + '.pdf')


def generador_de_facturas():
    for i in range(1, 100):
        Reportes.generar_factura(i, 'facturas/factura-' + str(i) + '.pdf')


