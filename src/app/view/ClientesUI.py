import gi

from app.data import ClientesDao

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ClientesUI(Gtk.Box):

    def __init__(self, parent=None):
        Gtk.Box.__init__(self)
        self.clientes = ClientesDao.get_db_clientes()
        self.parent = parent
        builder = Gtk.Builder()
        builder.add_from_file("../../res/ClientesUI.glade")

        self.box_clientes_ui = builder.get_object("box_clientes_ui")
        self.add(self.box_clientes_ui)
        self.treeview_container = builder.get_object("tree_view_container")

        # Creating the ListStore model
        self.clientes_liststore = Gtk.ListStore(int, str, str, str, int, str)
        for cliente in self.clientes:
            cliente_detalles = [cliente.idd, cliente.dni, cliente.nombre, cliente.apellido, cliente.telefono,
                                cliente.direccion]
            self.clientes_liststore.append(cliente_detalles)

        self.treeview = Gtk.TreeView(model=self.clientes_liststore)
        for i, column_title in enumerate(["ID", "DNI", "Nombre", "Apellido", "Telefono", "Direccion"]):
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
