import gi

from app.view.ClientesUI import ClientesUI
from app.view.ProductosUI import ProductosUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainUi(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(400, 200)

        self.active_pane = None

        builder = Gtk.Builder()
        builder.add_from_file("../../res/MainUI.glade")
        self.grid = builder.get_object("home_buttons_grid")

        self.show_main_menu()

        signals = {
            "btn_caja_act": self.on_btn_activate,
            "btn_clientes_act": self.on_btn_clientes,
            "btn_productos_act": self.on_btn_productos,
            "btn_reportes_act": self.on_btn_activate,
            "btn_documentacion_act": self.on_btn_activate,
            "btn_salir_act": Gtk.main_quit
        }
        builder.connect_signals(signals)
        self.show_all()

    def on_btn_activate(self, button):
        print("Click" + self.label)

    def on_btn_clientes(self, button):
        clientesui = ClientesUI(self)
        self.set_active_pane(clientesui)

    def on_btn_productos(self, button):
        productosui = ProductosUI(self)
        self.set_active_pane(productosui)

    def set_active_pane(self, pane):
        if self.active_pane is not None:
            self.remove(self.active_pane)
        self.active_pane = pane
        self.add(self.active_pane)

    def show_main_menu(self):
        self.set_active_pane(self.grid)
