import gi

from app.data import ClientesDao, ProductosDao

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ProductosUI(Gtk.Box):

    def __init__(self, parent=None):
        Gtk.Box.__init__(self)
        self.productos = ProductosDao.get_db_productos()
        self.parent = parent
        builder = Gtk.Builder()
        builder.add_from_file("../../res/ListaUI.glade")
        signals = {
            "btn_agregar": self.on_btn_agregar,
            "btn_editar": self.on_btn_editar,
            "btn_remover": self.on_btn_remover,
            "btn_volver": self.on_btn_volver,
        }
        builder.connect_signals(signals)

        self.box_productos_ui = builder.get_object("box_ui")
        self.add(self.box_productos_ui)
        self.treeview_container = builder.get_object("tree_view_container")

        # Creating the ListStore model
        self.productos_liststore = Gtk.ListStore(int, str, str, int, int)
        for producto in self.productos:
            producto_detalles = [producto.idd, producto.nombre, producto.descripcion, producto.precio, producto.stock]
            self.productos_liststore.append(producto_detalles)

        self.treeview = Gtk.TreeView(model=self.productos_liststore)
        for i, column_title in enumerate(["ID", "Nombre", "Precio", "Stock", "Descripcion"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column.set_resizable(True)
            if column_title == "Direccion":
                column.set_min_width(900)
            self.treeview.append_column(column)

        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.treeview_container.add(self.scrollable_treelist)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()

    def on_btn_volver(self, button):
        self.parent.show_main_menu()

    def on_btn_agregar(self, button):
        self.parent.show_main_menu()

    def on_btn_editar(self, button):
        self.parent.show_main_menu()

    def on_btn_remover(self, button):
        self.parent.show_main_menu()
