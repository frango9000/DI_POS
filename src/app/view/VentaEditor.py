import gi

from app.model.Venta import Venta

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VentaEditor(Gtk.Window):
    """
    clase que genera y controla el editor de Ventas
    """

    def __init__(self, parent, venta: Venta = None):
        Gtk.Window.__init__(self)
        self.parent = parent
        self.creating: bool = venta is None
        if self.creating:
            self.venta = Venta(0, 0)
        else:
            self.venta = venta

        builder = Gtk.Builder()
        builder.add_from_file("../../res/VentaUI.glade")
        signals = {
            "btn_cancelar_act": self.on_btn_cancelar_act,
            "btn_guardar_act": self.on_btn_guardar_act,
            "btn_abrir_act": self.on_btn_abrir_act
        }
        builder.connect_signals(signals)
        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)

        self.field_venta_id: Gtk.Entry = builder.get_object("field_venta_id")
        self.field_venta_id_cliente: Gtk.Entry = builder.get_object("field_venta_id_cliente")
        self.field_venta_fecha_hora: Gtk.Entry = builder.get_object("field_venta_fecha_hora")

        self.field_venta_id.set_text(str(self.venta.idd))
        self.field_venta_id_cliente.set_text(str(self.venta.id_cliente))
        self.field_venta_fecha_hora.set_text(str(self.venta.fecha_hora))

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
        self.venta.id_cliente = self.field_venta_id_cliente.get_text()
        self.venta.fecha_hora = self.field_venta_fecha_hora.get_text()
        if self.creating:
            self.venta.insert()
        else:
            self.venta.update()
        self.parent.return_from_child()
