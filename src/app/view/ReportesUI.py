import gi

from app.view import PyDialogs

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ReportesUI(Gtk.Box):

    def __init__(self, parent=None):
        Gtk.Box.__init__(self)
        self.parent = parent
        builder = Gtk.Builder()
        builder.add_from_file("../../res/ReportesUI.glade")
        signals = {
            "tgl_dia": self.on_tgl_dia,
            "tgl_mes": self.on_tgl_mes,
            "btn_guardar": self.on_btn_guardar,
            "btn_volver": self.on_btn_volver
        }
        builder.connect_signals(signals)

        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)

        self.calendar: Gtk.Calendar = builder.get_object("calendario")
        self.tgl_btn_dia: Gtk.ToggleButton = builder.get_object("tgl_btn_dia")
        self.tgl_btn_mes: Gtk.ToggleButton = builder.get_object("tgl_btn_mes")
        self.entry_nombre_archivo: Gtk.Entry = builder.get_object("entry_nombre_archivo")
        self.folder_chooser: Gtk.FileChooserButton = builder.get_object("folder_chooser")

        self.tgl_btn_dia.set_active(True)
        self.tgl_btn_mes.set_active(False)

        self.show_all()

    def on_tgl_dia(self, button):
        self.tgl_btn_mes.set_active(not self.tgl_btn_dia.get_active())

    def on_tgl_mes(self, button):
        self.tgl_btn_dia.set_active(not self.tgl_btn_mes.get_active())

    def on_btn_guardar(self, button):
        if len(self.entry_nombre_archivo.get_text()) > 0 and self.folder_chooser.get_current_folder() is not None:
            pass
        else:
            PyDialogs.show_error_dialog(self.parent, "Error", "Nombre de archivo o ruta erronea")

    def on_btn_volver(self, button):
        pass
