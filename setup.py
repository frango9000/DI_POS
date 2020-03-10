from setuptools import setup, find_packages

setup(
    name="Punto de Venta",
    version="0.0.1",
    packages=['src', 'res'],
    author="Francisco Javier Sanchez Temprano",
    author_email="fsancheztemprano@danielcastelao.org",
    py_modules=['src'],
    package_data={
        "": ["*.txt", "*.rst", "*.glade"],
        "res": ["*"],
        "src": ["*"],
    },
    entry_points={
        "gui_scripts": [
            "mypos = App:main_func"
        ]
    }
)
