import gi

from app import Globals
from app.model.Producto import Producto

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ProductoEditor(Gtk.Window):
    """
    clase que genera y controla el editor de Productos
    """

    def __init__(self, parent, producto: Producto = None):
        Gtk.Window.__init__(self)
        self.parent = parent
        self.creating: bool = producto is None
        if self.creating:
            self.producto = Producto('', '')
        else:
            self.producto = producto

        builder = Gtk.Builder()
        builder.add_from_file(Globals.path_res + "/ProductoUI.glade")
        signals = {
            "btn_cancelar_act": self.on_btn_cancelar_act,
            "btn_guardar_act": self.on_btn_guardar_act
        }
        builder.connect_signals(signals)
        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)

        self.field_producto_id: Gtk.Entry = builder.get_object("field_producto_id")
        self.field_producto_nombre: Gtk.Entry = builder.get_object("field_producto_nombre")
        self.field_producto_precio: Gtk.Entry = builder.get_object("field_producto_precio")
        self.field_producto_stock: Gtk.Entry = builder.get_object("field_producto_stock")
        self.field_producto_descripcion: Gtk.Entry = builder.get_object("field_producto_descripcion")

        self.field_producto_id.set_text(str(self.producto.idd))
        self.field_producto_nombre.set_text(self.producto.nombre)
        self.field_producto_precio.set_text(str(self.producto.precio))
        self.field_producto_stock.set_text(str(self.producto.stock))
        self.field_producto_descripcion.set_text(self.producto.descripcion)

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
        self.producto.nombre = self.field_producto_nombre.get_text()
        self.producto.precio = int(self.field_producto_precio.get_text())
        self.producto.stock = int(self.field_producto_stock.get_text())
        self.producto.descripcion = self.field_producto_descripcion.get_text()
        if self.creating:
            self.producto.insert()
        else:
            self.producto.update()
        self.parent.return_from_child()
