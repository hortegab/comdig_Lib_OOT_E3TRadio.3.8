# INTRODUCCION

Este es el principal OOT para GNU Radio creado en la Escuela de Ingenierías Eléctrica Electrónica y Telecomunicaciones (E3T) de la UIS con el propósito de la formación en las asignaturas de comunicaciones. Esta versión está adaptada y probad con GNU Radio version 3.8.1 con Python 3.8.2. Como es bien sabido, un OOT es una especie de libreria, pero no de Python sino de GNURadio, por eso tiene una forma especial de instalación.

# PRERREQUISITOS (DEPENDENCIAS)
Aquí se describe lo que hay que instalar previamente. Lo que se instala solo la primera vez. Todo lo siguiente se instala en forma de comandos por terminal ubuntu.

Se supone que usted ya tiene instalado git si ha podido bajar este paquete. Pero si no es así, este es el comando para hacerlo:

$ sudo apt install git

## Actualización del sistema

$ sudo apt-get update
$ sudo apt-get upgrade

## Instalación de aplicaciones
$ sudo apt install --fix-broken
$ sudo apt-get install xterm cmake make

## Instalación de Liberias de python3

$ sudo apt install python3-pip python3-click-plugins
$ pip3 install numpy scipy mako sphinx lxml pyqt5 yaml click zmq markdown cython matplotlib
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

# LA INSTALACION DEL OOT E3TRADIO
- En la raiz de carpeta bajada del github crea la subcarpeta "buid"
- Entra a la subcarpeta "buid" y allí abre una terminal de comandos de ubunto
- Envía los siguientes comandos:

$ cmake ..
$ make
$ sudo make install
$ sudo ldconfig

# CORRECCION DE PATH
- La instalación con Python 3.8.2 tiene por ahora un bug a corregir:
  -- Los paquetes aparecen instalados en la carpeta:  /usr/local/lib/python3
  -- pero necesitamos que aparezca en /usr/local/lib/python3.8
- Eso se soluciona con el comando:
sudo cp -r /usr/local/lib/python3/dist-packages/E3TRadio /usr/local/lib/python3.8/dist-packages/

# PRUEBAS
Una buena prueba de instalación es llamar, con GNU Radio 3.8.1 el flujograma "Ejemplo diagrama de ojo.grc" que aparece en la carpeta "examples"
En caso de problemas, puede contactar a: hortegab@e3t.uis.edu.co











