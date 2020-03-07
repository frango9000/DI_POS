from pathlib import Path

import gi
from gi.repository.Gio import File

from app.data import ClientesDao, ProductosDao, VendidosDao
from app.model.Venta import Venta
from app.reportes import Reportes

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class CajaUI(Gtk.Box):

    def __init__(self, parent=None, venta: Venta = None):
        Gtk.Box.__init__(self)
        self.parent = parent
        self.creating: bool = venta is None

        builder = Gtk.Builder()
        builder.add_from_file("../../res/CajaUI.glade")
        signals = {
            "btn_agregar": self.on_btn_agregar,
            "btn_limpiar": self.on_btn_limpiar,
            "btn_eliminar": self.on_btn_eliminar,
            "btn_cancelar": self.on_btn_cancelar,
            "btn_guardar": self.on_btn_guardar,
            "btn_pdf": self.on_btn_pdf
        }
        builder.connect_signals(signals)

        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)
        self.combo_box_cliente: Gtk.ComboBoxText = builder.get_object("combo_box_cliente")
        self.combo_box_producto: Gtk.ComboBoxText = builder.get_object("combo_box_producto")
        self.field_total: Gtk.Entry = builder.get_object("field_total")
        self.tabla_vendidos: Gtk.Box = builder.get_object("tabla_vendidos")
        self.label_id: Gtk.Label = builder.get_object("label_id")
        self.btn_limpiar: Gtk.Button = builder.get_object("btn_limpiar")
        self.btn_eliminar: Gtk.Button = builder.get_object("btn_eliminar")
        self.btn_agregar: Gtk.Button = builder.get_object("btn_agregar")
        self.btn_guardar: Gtk.Button = builder.get_object("btn_guardar")
        self.btn_pdf: Gtk.Button = builder.get_object("btn_pdf")

        self.combo_box_cliente.set_entry_text_column(0)
        self.combo_box_producto.set_entry_text_column(0)

        # Creating the ListStore model
        self.liststore = Gtk.ListStore(int, str, int)
        self.treeview = Gtk.TreeView(model=self.liststore)
        for i, column_title in enumerate(["ID", "Producto", "Precio"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column.set_resizable(True)
            if column_title == "Producto":
                column.set_min_width(300)
            self.treeview.append_column(column)

        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.scrollable_treelist.add(self.treeview)

        self.tabla_vendidos.add(self.scrollable_treelist)

        if self.creating:
            self.venta = Venta(0)
            self.edicion(True)
            self.refrescar_clientes()
            self.refrescar_productos()
        else:
            self.venta = venta
            self.label_id.set_text(str(self.venta.idd))
            cliente = ClientesDao.get_id(self.venta.id_cliente)
            self.combo_box_cliente.append_text(
                str(cliente.idd) + " - " + cliente.dni + " - " + cliente.nombre + " - " + cliente.apellido)
            self.combo_box_cliente.set_active(0)
            vendidos = VendidosDao.get_id_venta(venta.idd)
            for vendido in vendidos:
                producto = ProductosDao.get_id(vendido.id_producto)
                self.liststore.append([producto.idd, producto.nombre, vendido.precio_unidad])
            self.refrescar_total()
            self.edicion(False)

        self.show_all()

    def refrescar_clientes(self):
        clientes = ClientesDao.get_all()
        for cliente in clientes:
            self.combo_box_cliente.append_text(
                str(cliente.idd) + " - " + cliente.dni + " - " + cliente.nombre + " - " + cliente.apellido)

    def refrescar_productos(self):
        productos = ProductosDao.get_all()
        for producto in productos:
            self.combo_box_producto.append_text(
                str(producto.idd) + " - " + producto.nombre + " - " + str(producto.precio))

    def refrescar_total(self):
        sum: int = 0
        for row in self.liststore:
            sum += row[2]
        self.field_total.set_text(str(sum))

    def on_btn_agregar(self, btn):
        text = self.combo_box_producto.get_active_text()
        if text is not None:
            id_producto = int(text.split(' - ')[0])
            producto = ProductosDao.get_id(id_producto)
            self.liststore.append([producto.idd, producto.nombre, producto.precio])
            self.refrescar_total()

    def on_btn_limpiar(self, btn):
        self.liststore.clear()
        self.refrescar_total()

    def on_btn_eliminar(self, btn):
        model, treeiter = self.treeview.get_selection().get_selected()
        if treeiter is not None:
            self.liststore.remove(treeiter)
        self.refrescar_total()

    def on_btn_cancelar(self, btn):
        self.parent.show_main_menu()

    def on_btn_guardar(self, btn):
        if self.combo_box_cliente.get_active_text() is None:
            self.info_dialog("Debes elegir un cliente", "Venta Incompleta")
        elif len(self.liststore) == 0:
            self.info_dialog("Nada que vender", 'Venta Incompleta')
        elif not self.creating:
            self.info_dialog("Esta venta esta cerrada", "Venta Cerrada")
        else:
            id_cliente = int(self.combo_box_cliente.get_active_text().split(' - ')[0])
            self.venta.id_cliente = id_cliente
            id_venta = self.venta.insert()
            self.label_id.set_text(str(id_venta))
            for row in self.liststore:
                from app.model.Vendido import Vendido
                Vendido(id_venta, row[0], 1, row[2]).insert()
            self.edicion(False)
            self.info_dialog("Venta Guardada", 'Venta Guardada')

    def info_dialog(self, msg, title):
        dialog1 = Gtk.MessageDialog(self.parent, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, title)
        dialog1.format_secondary_text(msg)
        dialog1.run()
        dialog1.destroy()

    def get_selected_id(self) -> int:
        model, treeiter = self.treeview.get_selection().get_selected()
        if treeiter is not None:
            selected_id = model[treeiter][0]
            return selected_id
        return 0

    def edicion(self, b: bool):
        self.combo_box_cliente.set_sensitive(b)
        self.combo_box_producto.set_sensitive(b)
        self.field_total.set_sensitive(b)
        self.tabla_vendidos.set_sensitive(b)
        self.label_id.set_sensitive(b)
        self.btn_limpiar.set_sensitive(b)
        self.btn_eliminar.set_sensitive(b)
        self.btn_agregar.set_sensitive(b)
        self.btn_guardar.set_sensitive(b)
        self.btn_pdf.set_sensitive(not b)

    def on_btn_pdf(self, btn):
        dlg = Gtk.FileChooserDialog("Guardar en...", self.parent, Gtk.FileChooserAction.SAVE,
                                    (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        dlg.set_current_name('Factura-' + str(self.venta.idd) + '.pdf')
        dlg.set_filename(str(Path.home()))
        response = dlg.run()
        if response == Gtk.ResponseType.OK:
            filename = dlg.get_filename()
            Reportes.generar_factura(self.venta.idd, filename)
        dlg.destroy()
