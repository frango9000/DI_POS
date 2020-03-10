import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def show_info_dialog(parent, title, message):
    """
    dialogo informativo

    :param parent:
    :type parent:
    :param title:
    :type title:
    :param message:
    :type message:
    :return:
    :rtype:
    """
    dialog = Gtk.MessageDialog(parent, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, title)
    dialog.format_secondary_text(message)
    dialog.run()
    dialog.destroy()


def show_error_dialog(parent, title, message):
    """
    dialogo de error
    :param parent:
    :type parent:
    :param title:
    :type title:
    :param message:
    :type message:
    :return:
    :rtype:
    """
    dialog = Gtk.MessageDialog(parent, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CANCEL, title)
    dialog.format_secondary_text(message)
    dialog.run()
    dialog.destroy()


def show_warn_confirm_dialog(parent, title, message) -> bool:
    """
    dialogo de confirmacion
    :param parent:
    :type parent:
    :param title:
    :type title:
    :param message:
    :type message:
    :return: confirmacion de usuario
    :rtype: bool
    """
    dialog = Gtk.MessageDialog(parent, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK_CANCEL, title)
    dialog.format_secondary_text(message)
    response = dialog.run()
    dialog.destroy()
    return response == Gtk.ResponseType.OK


def show_question_dialog(parent, title, message) -> bool:
    """
    dialogo de confirmacion
    :param parent:
    :type parent:
    :param title:
    :type title:
    :param message:
    :type message:
    :return:  confirmacion de usuario
    :rtype: bool
    """
    dialog = Gtk.MessageDialog(parent, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, title)
    dialog.format_secondary_text(message)
    response = dialog.run()
    dialog.destroy()
    return response == Gtk.ResponseType.YES


def show_input_dialog(parent, title, message, entry_label):
    """
    dialogo de entrada de texto

    :param parent:
    :type parent:
    :param title:
    :type title:
    :param message:
    :type message:
    :param entry_label:
    :type entry_label:
    :return: texto introducido por el usuario
    :rtype: str
    """
    # base this on a message dialog
    dialog = Gtk.MessageDialog(
        parent,
        Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
        Gtk.MessageType.QUESTION,
        Gtk.ButtonsType.OK,
        title)
    # create the text input field
    entry = Gtk.Entry()
    # allow the user to press enter to do ok
    entry.connect("activate", responseToDialog, dialog, Gtk.ResponseType.OK)
    # create a horizontal box to pack the entry and a label
    hbox = Gtk.HBox()
    hbox.pack_start(Gtk.Label(entry_label), False, 5, 8)
    hbox.pack_end(entry, True, True, 8)
    # some secondary text
    dialog.format_secondary_text(message)
    # add it and show it
    dialog.vbox.pack_end(hbox, True, True, 0)
    dialog.show_all()
    # go go go
    dialog.run()
    text = entry.get_text()
    dialog.destroy()
    return text


def responseToDialog(entry, dialog, response):
    """metodo de ayuda de show_input_dialog"""
    dialog.response(response)
