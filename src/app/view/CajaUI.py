import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class CajaUI(Gtk.Box):

    def __init__(self, parent=None):
        Gtk.Box.__init__(self)
        self.parent = parent

        builder = Gtk.Builder()
        builder.add_from_file("../../res/CajaUI.glade")
        signals = {
            "btn_agregar": self.on_btn_agregar,
            "btn_limpiar": self.on_btn_limpiar,
            "btn_eliminar": self.on_btn_eliminar,
            "btn_cancelar": self.on_btn_cancelar,
            "btn_guardar": self.on_btn_guardar
        }
        builder.connect_signals(signals)

        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)
        self.combo_box_cliente: Gtk.ComboBox = builder.get_object("combo_box_cliente")
        self.combo_box_producto: Gtk.ComboBox = builder.get_object("combo_box_producto")
        self.field_total: Gtk.Entry = builder.get_object("field_total")
        self.tabla_vendidos: Gtk.Box = builder.get_object("tabla_vendidos")

        self.show_all()

    def on_btn_agregar(self, btn):
        pass

    def on_btn_limpiar(self, btn):
        pass

    def on_btn_eliminar(self, btn):
        pass

    def on_btn_cancelar(self, btn):
        pass

    def on_btn_guardar(self, btn):
        pass
