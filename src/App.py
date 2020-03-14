import gi

from src.app.view.MainUI import MainUi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

"""
entrypoint de la app
"""


# if __name__ == "__main__":
#     MainUi()
#     Gtk.main()
#

def main_func():
    MainUi()
    Gtk.main()


main_func()

# main_func()
