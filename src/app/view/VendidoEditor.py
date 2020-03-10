import gi

from app import Globals
from app.model.Vendido import Vendido

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VendidoEditor(Gtk.Window):
    """
    clase que genera y controla el editor de Vendidos
    """

    def __init__(self, parent, vendido: Vendido = None):
        Gtk.Window.__init__(self)
        self.parent = parent
        self.creating: bool = vendido is None
        if self.creating:
            self.vendido = Vendido(0, 0, 0, 0)
        else:
            self.vendido = vendido

        builder = Gtk.Builder()
        builder.add_from_file(Globals.path_res + "/VendidoUI.glade")
        signals = {
            "btn_cancelar_act": self.on_btn_cancelar_act,
            "btn_guardar_act": self.on_btn_guardar_act
        }
        builder.connect_signals(signals)
        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)

        self.field_vendido_id: Gtk.Entry = builder.get_object("field_vendido_id")
        self.field_vendido_id_venta: Gtk.Entry = builder.get_object("field_vendido_id_venta")
        self.field_vendido_id_producto: Gtk.Entry = builder.get_object("field_vendido_id_producto")
        self.field_vendido_cantidad: Gtk.Entry = builder.get_object("field_vendido_cantidad")
        self.field_vendido_precio_unidad: Gtk.Entry = builder.get_object("field_vendido_precio_unidad")

        self.field_vendido_id.set_text(str(self.vendido.idd))
        self.field_vendido_id_venta.set_text(str(self.vendido.id_venta))
        self.field_vendido_id_producto.set_text(str(self.vendido.id_producto))
        self.field_vendido_cantidad.set_text(str(self.vendido.cantidad))
        self.field_vendido_precio_unidad.set_text(str(self.vendido.precio_unidad))

        self.show_all()

    def on_btn_cancelar_act(self, button):
        """volver a la lista"""
        self.parent.return_from_child()

    def on_btn_abrir_act(self, button):
        self.parent.return_from_child()

    def on_btn_guardar_act(self, button):
        """
        guardar los datos introducidos ya sea creando e
        insertando un nuevo objeto o actualizandolo
        :param button:
        :type button:
        :return:
        :rtype:
        """
        self.vendido.id_venta = self.field_vendido_id_venta.get_text()
        self.vendido.id_producto = self.field_vendido_id_producto.get_text()
        self.vendido.cantidad = self.field_vendido_cantidad.get_text()
        self.vendido.precio_unidad = self.field_vendido_precio_unidad.get_text()
        if self.creating:
            self.vendido.insert()
        else:
            self.vendido.update()
        self.parent.return_from_child()
