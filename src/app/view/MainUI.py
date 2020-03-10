import gi
from src import app

from src.app import Globals
from src.app.view.ClientesUI import ClientesUI
from src.app.view.ProductosUI import ProductosUI
from src.app.view.ReportesUI import ReportesUI
from src.app.view.CajaUI import CajaUI
from src.app.view.VendidosUI import VendidosUI
from src.app.view.VentasUI import VentasUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainUi(Gtk.Window):
    """
    clase que genera y controla la el menu principal de la applicacion
    """

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)

        self.active_pane = None

        builder = Gtk.Builder()
        builder.add_from_file(Globals.path_res + "/MainUI.glade")
        self.box_ui = builder.get_object("box_ui")
        self.show_main_menu()

        signals = {
            "btn_caja_act": self.on_btn_caja,
            "btn_clientes_act": self.on_btn_clientes,
            "btn_productos_act": self.on_btn_productos,
            "btn_ventas_act": self.on_btn_ventas,
            "btn_vendidos_act": self.on_btn_vendidos,
            "btn_reportes_act": self.on_btn_reportes,
            "btn_salir_act": Gtk.main_quit
        }
        builder.connect_signals(signals)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def on_btn_reportes(self, button):
        """
        abre el menu de reportes
        :param button:
        :type button:
        :return:
        :rtype:
        """
        reportes_ui = ReportesUI(self)
        self.set_active_pane(reportes_ui)

    def on_btn_clientes(self, button):
        """
        abre el editor de clientes
        :param button:
        :type button:
        :return:
        :rtype:
        """
        clientes_ui = ClientesUI(self)
        self.set_active_pane(clientes_ui)

    def on_btn_productos(self, button):
        """
        abre el editor de productos
        :param button:
        :type button:
        :return:
        :rtype:
        """
        productos_ui = ProductosUI(self)
        self.set_active_pane(productos_ui)

    def on_btn_ventas(self, button):
        """
        abre el editor de ventas
        :param button:
        :type button:
        :return:
        :rtype:
        """
        ventas_ui = VentasUI(self)
        self.set_active_pane(ventas_ui)

    def on_btn_vendidos(self, button):
        """
        abre el editor de vendidos
        :param button:
        :type button:
        :return:
        :rtype:
        """
        vendidos_ui = VendidosUI(self)
        self.set_active_pane(vendidos_ui)

    def on_btn_caja(self, button):
        """
        abre la caja en modo generacion de ventas
        :param button:
        :type button:
        :return:
        :rtype:
        """
        caja_ui = CajaUI(self, None)
        self.set_active_pane(caja_ui)

    def set_active_pane(self, pane):
        """
        metodo que amuestra en la ventana principal un Gtk.Widget recibido como parametro
        :param pane:
        :type pane:
        :return:
        :rtype:
        """
        if self.active_pane is not None:
            self.remove(self.active_pane)
        self.active_pane = pane
        if self.active_pane is not None:
            self.add(self.active_pane)

    def show_main_menu(self):
        """
        muestra el menu principal

        este metodo sera llamado por todos los hijos de esta ventana para volver al menu principal
        :return:
        :rtype:
        """
        self.set_active_pane(self.box_ui)
