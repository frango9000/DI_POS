# DI_POS

## Descrición do proxecto:

### Realizar unha aplicación 

 [x] con varias fiestras que 
 
 [x] ten que funcionar sobre o entorno gráfico de ubuntu (Gtk3). 
 
 [x] A aplicación ten que ter polo menos 3 formularios. 
 
 [x] A aplicación terá un formulario de entrada que permita o usuario elixir entre, Xestión de Clientes e Produtos/Servizos,
  
 [x] permitindo a posibilidade de saír. 
 

### No formulario de xestión de clientes dará a posibilidade de
 
 [x] Insertar,
  
 [x] Consultar e
  
 [x] Borrar un cliente.
  
 [x] Os datos persoais a gardar serán os habituais (non menos de 6).
 

### No programa hai que inserir algún

 [x]  Treeview 

 [x] e algún ComboBox. 

 [x] O Treeview ten que ser sensible a eventos (ou selección ou edición).


### Usabilidad
Tamén ter en conta os criterios de usabilidade para deseñara a aplicación: 
 
 [x] Acesibilidade, 
 
 [x] facilidade de uso, 
 
 [ ] xestión e prevención de erros, etc.

### Base de datos
A aplicación haberá usar unha base de datos e conectarnos a ela. Mellor usar SQLite en modo local, pero tendo en conta as súas limitacións (si alguén quere utilizar outra base de datos, non hai problema).

 [x] sqlite


### Informes
O proxecto ten que xerar polo menos dous informes realizados con Reportlab. Os informes terá que xeralos a aplicación dende o programa cos datos da base de datos. O tipo de informe poderá ser un listado, factura, ficha cliente, etc. A xeración dos informes se fará a través dalgunha acción nalgún control.
 
 [x] Factura
 
 [x] reporte dia
 
 [x] reporte mes


### Documentacion:

 [x] código da aplicación, 

 Sphinx:
 
 [x] modulos y paquetes 
 
 [x] funcionamento e uso da aplicación
 

### Entregarase a aplicación:
 
 [x] empaquetada e 
 
 [x] funcional, 
 
 [x] preparada para instalar nun linux ubuntu.


### Data tope de entrega do traballo 15 marzo.

## Prof. Manuel Guimarey

# Comandos linux env:
 
sudo apt install build-essential libcairo2-dev pkg-config python3-dev libgtk-3-dev glade python3-sphinx

### instalacion de dependencias en entorno virtual 

python3 -m pip install pycairo pygobject reportlab
        
### generacion de documentacion
sphinx-quickstart
sphinx-apidoc -o . docs/
make html
 
 
### packaging
python3 setup.py sdist
 
### instalacion
pip install dist/MyPos-0.0.1.tar.gz 

### ejecucion
mypos
