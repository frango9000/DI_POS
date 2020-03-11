import pathlib

# rutas globales
# path_res = "../../res/"
path_res = str((pathlib.Path(__file__).parent.parent.parent / "res/").absolute())
db_src = str((pathlib.Path(__file__).parent / str(path_res + '/pos.db')).absolute())
logo_src = str((pathlib.Path(__file__).parent / str(path_res + '/logo.jpg')).absolute())
