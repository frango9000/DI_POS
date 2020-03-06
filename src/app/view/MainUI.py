import gi

from app.view.CajaUI import CajaUI
from app.view.ClientesUI import ClientesUI
from app.view.ProductosUI import ProductosUI
from app.view.VendidosUI import VendidosUI
from app.view.VentasUI import VentasUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainUi(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)

        self.active_pane = None

        builder = Gtk.Builder()
        builder.add_from_file("../../res/MainUI.glade")
        self.box_ui = builder.get_object("box_ui")
        self.show_main_menu()

        signals = {
            "btn_caja_act": self.on_btn_caja,
            "btn_clientes_act": self.on_btn_clientes,
            "btn_productos_act": self.on_btn_productos,
            "btn_ventas_act": self.on_btn_ventas,
            "btn_vendidos_act": self.on_btn_vendidos,
            "btn_reportes_act": self.on_btn_activate,
            "btn_documentacion_act": self.on_btn_activate,
            "btn_salir_act": Gtk.main_quit
        }
        builder.connect_signals(signals)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def on_btn_activate(self, button):
        print("Click" + self.label)

    def on_btn_clientes(self, button):
        clientes_ui = ClientesUI(self)
        self.set_active_pane(clientes_ui)

    def on_btn_productos(self, button):
        productos_ui = ProductosUI(self)
        self.set_active_pane(productos_ui)

    def on_btn_ventas(self, button):
        ventas_ui = VentasUI(self)
        self.set_active_pane(ventas_ui)

    def on_btn_vendidos(self, button):
        vendidos_ui = VendidosUI(self)
        self.set_active_pane(vendidos_ui)

    def on_btn_caja(self, button):
        caja_ui = CajaUI(self, None)
        self.set_active_pane(caja_ui)

    def set_active_pane(self, pane):
        if self.active_pane is not None:
            self.remove(self.active_pane)
        self.active_pane = pane
        if self.active_pane is not None:
            self.add(self.active_pane)

    def show_main_menu(self):
        self.set_active_pane(self.box_ui)
