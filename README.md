# pythonDjango

Proyecto en Django para hacer una API de catalogo de libros, es decir una Bibioteca

# Para levantar el server, lo hacemos con el comando py manage.py runserver

# Para poder generar la migracion necesaria que nos pide al principio, ejecutamos el comando py manage.py migrate

# Para crear una aplicacion usamos el comando py manage.py startapp <nombre_aplicacion>

# Si queremos que la nueva aplicacion este disponible en django, tenemos que agregarla en el archivo settings de la carpeta root, en la lista llamada INSTALLED_APPS con el nombre de la carpeta.apps.nombreclase

# Para crear archivos de migracion a partir de modelos armados (nuevos o actualizados), hay que ejecutar py manage.py makemigrations <nombre_aplicacion>, el cual nos va a crear un archivo de migracion dentro de la carpeta migrations de la aplicacion. Si no especificamos el <nombre_aplicacion> nos va a crear archivos de migracion para todas las aplicaciones. Luego si queremos que se efectuen en la base de datos el archivo de migracion, ejecutamos py manage.py migrate

# Para pooder crear datos en la BD, es necesario crear un super usuario, para eso ejecutamos: py manage.py createsuperuser, y cargar los datos que se piden

# Si queremos ir al panel administrador de django, vamos a http://localhost:8000/admin/

# Para hacer que un modelo sea visible desde el panel, tenemos que registrar ese modelo en el archivo admin de la carpeta de la aplicacion

# Hasta los 40 mmin