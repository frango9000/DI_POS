from setuptools import setup, find_packages

setup(
    name="MyPos",
    version="0.0.1",
    packages=find_packages(),
    author="Francisco Javier Sanchez Temprano",
    author_email="fsancheztemprano@danielcastelao.org",
    package_data={
        "": ["*.txt", "*.rst", "*.glade", "*.py"],
        "res": ["*"],
        "src": ["*"],
    },
    entry_points={
        "gui_scripts": [
            "mypos = src.App:main_func"
        ]
    },
    install_requires=['PyGObject', 'pycairo']
)
