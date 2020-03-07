import os

import gi

from app.reportes import Reportes
from app.view import PyDialogs

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ReportesUI(Gtk.Box):
    """
    clase que genera y controla el menu de reportes dando opcion a elegir un dia o mes,
    elegir una ubicacion y un nombre de archivo, generara el reporte solicitado y lo guardara
    """

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
        """
        activa opcion reporte diario
        :param button:
        :type button:
        :return:
        :rtype:
        """
        self.tgl_btn_mes.set_active(not self.tgl_btn_dia.get_active())

    def on_tgl_mes(self, button):
        """
        activa opcion reporte mensual
        :param button:
        :type button:
        :return:
        :rtype:
        """
        self.tgl_btn_dia.set_active(not self.tgl_btn_mes.get_active())

    def on_btn_guardar(self, button):
        """
        verifica los datos y genera el reporte solicitado
        :param button:
        :type button:
        :return:
        :rtype:
        """
        if len(self.entry_nombre_archivo.get_text()) > 0 and self.folder_chooser.get_filename() is not None:
            ano = self.calendar.get_date()[0]
            mes = self.calendar.get_date()[1] + 1
            if self.tgl_btn_dia.get_active():
                dia = self.calendar.get_date()[2]
                Reportes.generar_reporte_diario(dia, mes, ano, os.path.join(self.folder_chooser.get_filename(),
                                                                            self.entry_nombre_archivo.get_text()) + '.pdf')
            else:
                Reportes.generar_reporte_mensual(mes, ano, os.path.join(self.folder_chooser.get_filename(),
                                                                        self.entry_nombre_archivo.get_text()) + '.pdf')
            PyDialogs.show_info_dialog(self.parent, "Informacion",
                                       "Reporte guardado en " + os.path.join(self.folder_chooser.get_filename(),
                                                                             self.entry_nombre_archivo.get_text()) + '.pdf')
        else:
            PyDialogs.show_error_dialog(self.parent, "Error", "Nombre de archivo o ruta erronea")

    def on_btn_volver(self, button):
        """vuelve al menu principal"""
        self.parent.show_main_menu()
