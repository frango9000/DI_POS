import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ClientesUI(Gtk.Box):
    def __init__(self, parent):
        self.parent = parent
        builder = Gtk.Builder()
        builder.add_from_file("../../res/ClientesUI.glade")

        self.container = builder.get_object("tree_view_container")

        # Creating the ListStore model
        self.software_liststore = Gtk.ListStore(int, str, str, str, int, str)
        for software_ref in software_list:
            self.software_liststore.append(list(software_ref))

# https: // python - gtk - 3 - tutorial.readthedocs.io / en / latest / treeview.html
