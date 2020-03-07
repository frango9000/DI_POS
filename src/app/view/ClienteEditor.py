import gi

from app.model.Cliente import Cliente

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ClienteEditor(Gtk.Window):
    """
    clase que genera y controla el editor de clientes
    """

    def __init__(self, parent, cliente: Cliente = None):
        Gtk.Window.__init__(self)
        self.parent = parent
        self.creating: bool = cliente is None
        if self.creating:
            self.cliente = Cliente('', '', '', 0, '')
        else:
            self.cliente = cliente

        builder = Gtk.Builder()
        builder.add_from_file("../../res/ClienteUI.glade")
        signals = {
            "btn_cancelar_act": self.on_btn_cancelar_act,
            "btn_guardar_act": self.on_btn_guardar_act
        }
        builder.connect_signals(signals)
        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)

        self.field_cliente_id: Gtk.Entry = builder.get_object("field_cliente_id")
        self.field_cliente_dni: Gtk.Entry = builder.get_object("field_cliente_dni")
        self.field_cliente_nombre: Gtk.Entry = builder.get_object("field_cliente_nombre")
        self.field_cliente_apellido: Gtk.Entry = builder.get_object("field_cliente_apellido")
        self.field_cliente_telefono: Gtk.Entry = builder.get_object("field_cliente_telefono")
        self.field_cliente_direccion: Gtk.Entry = builder.get_object("field_cliente_direccion")

        self.field_cliente_id.set_text(str(self.cliente.idd))
        self.field_cliente_dni.set_text(self.cliente.dni)
        self.field_cliente_nombre.set_text(self.cliente.nombre)
        self.field_cliente_apellido.set_text(self.cliente.apellido)
        self.field_cliente_telefono.set_text(str(self.cliente.telefono))
        self.field_cliente_direccion.set_text(self.cliente.direccion)

        self.show_all()

    def on_btn_cancelar_act(self, button):
        """volver a la lista"""
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
        self.cliente.dni = self.field_cliente_dni.get_text()
        self.cliente.nombre = self.field_cliente_nombre.get_text()
        self.cliente.apellido = self.field_cliente_apellido.get_text()
        self.cliente.telefono = int(self.field_cliente_telefono.get_text())
        self.cliente.direccion = self.field_cliente_direccion.get_text()
        if self.creating:
            self.cliente.insert()
        else:
            self.cliente.update()
        self.parent.return_from_child()
