import gi

from app.data import ClientesDao
from app.view import PyDialogs
from app.view.ClienteEditor import ClienteEditor

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ClientesUI(Gtk.Box):
    """
    clase que genera y controla el navegador de clientes
    """

    def __init__(self, parent=None):
        Gtk.Box.__init__(self)
        self.parent = parent
        self.editor_ui: ClienteEditor = None
        builder = Gtk.Builder()
        builder.add_from_file("../../res/ListaUI.glade")
        signals = {
            "btn_agregar": self.on_btn_agregar,
            "btn_editar": self.on_btn_editar,
            "btn_remover": self.on_btn_remover,
            "btn_volver": self.on_btn_volver,
            "btn_refrescar": self.on_btn_refrescar
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
        """limpia la tabla y busca en base de datos para rellenarla"""
        self.clientes_liststore.clear()
        clientes = ClientesDao.get_all()
        for cliente in clientes:
            cliente_detalles = [cliente.idd, cliente.dni, cliente.nombre, cliente.apellido, cliente.telefono,
                                cliente.direccion]
            self.clientes_liststore.append(cliente_detalles)

    def on_btn_volver(self, button):
        """vuelve al menu principal"""
        self.parent.show_main_menu()

    def on_btn_agregar(self, button):
        """
        abre el editor de clientes en modo generacion
        :param button:
        :type button:
        :return:
        :rtype:
        """
        self.set_sensitive(False)
        self.editor_ui = ClienteEditor(self)
        self.editor_ui.show()

    def on_btn_editar(self, button):
        """
        abre el editor de clientes en modo edicion con el id del cliente seleccionado
        :param button:
        :type button:
        :return:
        :rtype:
        """
        selected_id = self.get_selected_id()
        if selected_id > 0:
            self.set_sensitive(False)
            selected_object = ClientesDao.get_id(int(selected_id))
            self.editor_ui = ClienteEditor(self, selected_object)
            self.editor_ui.show()

    def on_btn_remover(self, button):
        """
        solicita confirmacion al usuario antes de eliminar el cliente seleccionado
        :param button:
        :type button:
        :return:
        :rtype:
        """
        selected_id = self.get_selected_id()
        if selected_id > 0:
            confirm = PyDialogs.show_warn_confirm_dialog(self.parent, "Eliminando Cliente",
                                                         "Estas seguro que deseas eliminar el cliente con id: "
                                                         + str(selected_id))
            if confirm:
                print("Eliminando cliente " + str(selected_id))
                eliminado = ClientesDao.remove_id(selected_id)
                elim = " " if eliminado else " no "
                PyDialogs.show_info_dialog(self.parent, "Eliminando Cliente", "Cliente" + elim + "eliminado.")
                self.refrescar_tabla()


    def on_btn_refrescar(self, button):
        """accion del boton refrescar tabla"""
        self.refrescar_tabla()

    def return_from_child(self):
        """
        metodo que reactiva la ventana al cerrar una ventana secundaria (ej. editor )
        :return:
        :rtype:
        """
        self.set_sensitive(True)
        self.refrescar_tabla()
        self.editor_ui.destroy()
        self.editor_ui = None

    def get_selected_id(self) -> int:
        """retorna el id del objeto seleccionado"""
        model, treeiter = self.treeview.get_selection().get_selected()
        if treeiter is not None:
            selected_id = model[treeiter][0]
            return selected_id
        return 0
