import gi

from app.data import VendidosDao
from app.view.VendidoEditor import VendidoEditor

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VendidosUI(Gtk.Box):

    def __init__(self, parent=None):
        Gtk.Box.__init__(self)
        self.parent = parent
        self.editor_ui: VendidoEditor = None
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
        self.vendidos_liststore = Gtk.ListStore(int, int, int, int, int)
        self.refrescar_tabla()

        self.treeview = Gtk.TreeView(model=self.vendidos_liststore)
        for i, column_title in enumerate(["ID", "ID Venta", "ID Producto", "Cantidad", "Precio Unidad"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column.set_resizable(True)
            if column_title == "Precio Unidad":
                column.set_min_width(900)
            self.treeview.append_column(column)

        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.treeview_container.add(self.scrollable_treelist)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()

    def refrescar_tabla(self):
        self.vendidos_liststore.clear()
        vendidos = VendidosDao.get_all()
        for vendido in vendidos:
            vendido_detalles = [vendido.idd, vendido.id_venta, vendido.id_producto, vendido.cantidad,
                                vendido.precio_unidad]
            self.vendidos_liststore.append(vendido_detalles)

    def on_btn_volver(self, button):
        self.parent.show_main_menu()

    def on_btn_agregar(self, button):
        self.set_sensitive(False)
        self.editor_ui = VendidoEditor(self)
        self.editor_ui.show()

    def on_btn_editar(self, button):
        selected_id = self.get_selected_id()
        if selected_id > 0:
            self.set_sensitive(False)
            selected_object = VendidosDao.get_id(int(selected_id))
            self.editor_ui = VendidoEditor(self, selected_object)
            self.editor_ui.show()

    def on_btn_remover(self, button):
        selected_id = self.get_selected_id()
        if selected_id > 0:
            dialog = Gtk.MessageDialog(self.parent, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK_CANCEL,
                                       "Eliminando Vendido")
            dialog.format_secondary_text("Estas seguro que deseas eliminar el vendido con id: " + str(selected_id))
            response = dialog.run()
            dialog.destroy()
            if response == Gtk.ResponseType.OK:
                print("Eliminando vendido " + str(selected_id))
                eliminado = VendidosDao.remove_id(selected_id)
                dialog2 = Gtk.MessageDialog(self.parent, 0, Gtk.MessageType.INFO,
                                            Gtk.ButtonsType.OK, "Eliminando Vendido")
                elim = " " if eliminado else " no "
                dialog2.format_secondary_text("Vendido" + elim + "eliminado.")
                dialog2.run()
                dialog2.destroy()
                self.refrescar_tabla()

            elif response == Gtk.ResponseType.CANCEL:
                print("Cancelado")

    def on_btn_refrescar(self, button):
        self.refrescar_tabla()

    def return_from_child(self):
        self.set_sensitive(True)
        self.refrescar_tabla()
        self.editor_ui.destroy()
        self.editor_ui = None

    def get_selected_id(self) -> int:
        model, treeiter = self.treeview.get_selection().get_selected()
        if treeiter is not None:
            selected_id = model[treeiter][0]
            return selected_id
        return 0
