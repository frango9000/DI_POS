import gi

from app.view.MainUI import MainUi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

if __name__ == "__main__":
    MainUi()
    Gtk.main()
