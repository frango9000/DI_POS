import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainUi(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(400, 200
                              )
        builder = Gtk.Builder()
        builder.add_from_file("../../res/MainUI.glade")
        self.grid = builder.get_object("home_buttons_grid")

        self.add(self.grid)

        signals = {
            "btn_caja_act": self.on_btn_activate,
            "btn_clientes_act": self.on_btn_activate,
            "btn_productos_act": self.on_btn_activate,
            "btn_reportes_act": self.on_btn_activate,
            "btn_documentacion_act": self.on_btn_activate,
            "btn_salir_act": Gtk.main_quit
        }
        builder.connect_signals(signals)
        self.show_all()

    def on_btn_activate(self, button):
        print("Click" + self.label)


if __name__ == "__main__":
    MainUi()
    Gtk.main()
