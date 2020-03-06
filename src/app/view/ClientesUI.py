import gi

from app.data import ClientesDao
from app.view.ClienteEditor import ClienteEditor

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ClientesUI(Gtk.Box):

    def __init__(self, parent=None):
        Gtk.Box.__init__(self)
        self.parent = parent
        self.cliente_editor_ui: ClienteEditor = None
        builder = Gtk.Builder()
        builder.add_from_file("../../res/ListaUI.glade")
        signals = {
            "btn_agregar": self.on_btn_agregar,
            "btn_editar": self.on_btn_editar,
            "btn_remover": self.on_btn_remover,
            "btn_volver": self.on_btn_volver,
        }
        builder.connect_signals(signals)

        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)
        self.treeview_container = builder.get_object("tree_view_container")

        # Creating the ListStore model
        self.clientes_liststore = Gtk.ListStore(int, str, str, str, int, str)
        self.refrescar_tabla()

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

    def refrescar_tabla(self):
        self.clientes_liststore.clear()
        clientes = ClientesDao.get_db_clientes()
        for cliente in clientes:
            cliente_detalles = [cliente.idd, cliente.dni, cliente.nombre, cliente.apellido, cliente.telefono,
                                cliente.direccion]
            self.clientes_liststore.append(cliente_detalles)

    def on_btn_volver(self, button):
        self.parent.show_main_menu()

    def on_btn_agregar(self, button):
        self.set_sensitive(False)
        self.cliente_editor_ui = ClienteEditor(self)
        self.cliente_editor_ui.show()

    def on_btn_editar(self, button):
        self.parent.show_main_menu()

    def on_btn_remover(self, button):
        self.parent.show_main_menu()

    def return_from_child(self):
        self.set_sensitive(True)
        self.refrescar_tabla()
        self.cliente_editor_ui.destroy()
        self.cliente_editor_ui = None
