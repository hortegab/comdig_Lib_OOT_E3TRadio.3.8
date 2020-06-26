# INTRODUCCION

Este es el principal OOT para GNU Radio creado en la Escuela de Ingenierías Eléctrica Electrónica y Telecomunicaciones (E3T) de la UIS con el propósito de la formación en las asignaturas de comunicaciones. Esta versión está adaptada y probad con GNU Radio version 3.8.1 con Python 3.8.2. Como es bien sabido, un OOT es una especie de libreria, pero no de Python sino de GNURadio, por eso tiene una forma especial de instalación.

# PRERREQUISITOS (DEPENDENCIAS)
Aquí se describe lo que hay que instalar previamente. Lo que se instala solo la primera vez. Usted no debe hacer esto si ya ha instalado antes este paquere y ahora solo quiere actualizarlo.

Todo lo siguiente se instala en forma de comandos por terminal ubuntu.

## Lo que siempre se hace - la Actualización del sistema
Siempre que vaya a hacer cualquier cosa sobre Ubuntu debes actualizar tu sistema, más aún cuando se trata de instalaciones de paquetes. Estos son los cmandos para actualizar el sistema:

$ sudo apt-get update
$ sudo apt-get upgrade

## Lo que se supone que usted ya tiene
Se supone que usted ya tiene instalado:

- git ya que seguramente lo usó para bajar este paquete. Si acaso no tiene instalado git, este es el comando para hacerlo:

$ sudo apt install git

- gnuradio version 3.8.1. Si no lo tiene, es tan simple como enviar el comando:

sudo apt install gnuradio

## Instalación de aplicaciones
$ sudo apt install --fix-broken

$ sudo apt install xterm
$ sudo apt-get install cmake make

## Instalación de Liberias de python3

$ sudo apt install python3-pip python3-click-plugins
$ pip3 install numpy scipy mako sphinx lxml pyqt5 click zmq markdown cython matplotlib
$ pip3 install pyyaml
$ pip3 install git+https://github.com/pyqtgraph/pyqtgraph@master

## Instalacion de la libreria de python para el diagrama de ojo

$ pip3 install git+https://github.com/hortegab/comdig_DiagramaOjo.3.8

## Comprobación
Revise si lo que corresponde a python quedó instalado, con este comando:
$ pip3 list

Debe comprobar que mínimamente esté instalado:
- eyediagram
- Markdown
- Matplotlib
- numpy
- scipy

## Actualice el sistema
$ sudo apt-get update
$ sudo apt-get upgrade

# LA INSTALACION DEL OOT E3TRADIO

- Entra a la carpeta principal del paquete bajado del github y crea allí la subcarpeta "build"
- Entra a esa subcarpeta "build" y allí abre una terminal de comandos de ubunto
- Envía por el terminal los siguientes comandos:

## Actualice el sistema
$ sudo apt-get update
$ sudo apt-get upgrade

## Instale el OOT E3T Radio

$ cmake ..
$ make
$ sudo make install
$ sudo ldconfig

# CORRECCION DE PATH
- La instalación con Python 3.8.2 tiene por ahora un bug a corregir. Al parecer el problema es por usar Python 3.8.2, pues al parecer GNURadio 3.1 está siendo más frecuentemente usado en versiones anteriores. El problema consiste en que:

  -- Los paquetes aparecen instalados en la carpeta:  /usr/local/lib/python3
  -- pero necesitamos que aparezca en /usr/local/lib/python3.8

- Eso se soluciona con el comando:
sudo cp -r /usr/local/lib/python3/dist-packages/E3TRadio /usr/local/lib/python3.8/dist-packages/

# PRUEBAS
Una buena prueba de instalación es llamar, con GNU Radio 3.8.1 el flujograma "Ejemplo diagrama de ojo.grc" que aparece en la carpeta "examples"
En caso de problemas, puede contactar a: hortegab@e3t.uis.edu.co











