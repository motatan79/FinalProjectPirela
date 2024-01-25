Pre Entrega # 3
Tú Primera Página

KIDDO SWAPP
Es una app de intercambio de ropa de segunda mano para niños, con presencia en Latinoamérica. 

## Extraer el contenido desde el siguiente repositorio en git con el siguiente comando
git clone https://github.com/motatan79/ProjectDjangoFinal.git

## Para ingresar al proyecto se debe crear un ambiente virtual en la terminal
- python -m venv .venv (Windows)
- python3 -m venv .venv (Linux o Mac)

## Posteriormente activar el entorno virtual
- .\.venv\Scripts\activate (Windows Powershell)
- source .venv/bin/activate (Linux o Mac)

## Instalar Django
pip install django

## Ingresar a la carpeta ProjectDjangoFinal
cd .\ProjectDjangoFinal\

## Ejecutar el servidor
python manage.py runserver

## En la página de inicio, esquina superior izquierda, al pulsar sobre el nombre de APP siempre retornará a la página de Inicio, al igual que al pulsar la palabra INICIO en la esquina superior derecha. 
## En la página de inicio, en la esquina inferior izquierda al pulsar las palabras "Acerca de Nosotros", "Servicios" o "Contáctanos", se obtienen información relacionada con la Kiddo Swapp. 


## En la página de inicio, esquina superior derecha,  se puede acceder al menú de consultas y adición de nuevas: 
- Tienda. Para registrar una nueva tienda deberá completar el formulario y presionar el botón Submit mientras que para consultar las tiendas existentes deberá presionar el botón Tiendas Registradas.
- Clientes(swapper). Para registrar un nuevo swapper deberá completar el formulario y presionar el botón Submit mientras que para consultar los swapper existentes deberá presionar el botón Swapper Registradas.
- Países. Para añadir un nuevo país deberá completar el formulario y presionar el botón Submit mientras que para consultar los países existentes deberá presionar el botón Países Registradas. 

Una vez registrado el usuario, presionando el botón Acceder, cargando su usuario (Nombre del Swapper) y contraseña podrá acceder a una nueva url donde es posible crear un nuevo evento (Botón Crear Evento) rellenando un formulario. Además se podrá consultar los eventos existentes. 
Importante, sólo los swapper registrados pueden crear eventos. 
## Presionando el botón Cerrar Sesión , será cerrada la sesión iniciada por el usuario. 

## Para realizar la búsqueda de información en la base de datos (Buscar Tienda).
En la Pantalla Inicio, colocar el nombre de una tienda y presionar el botón "Buscar Tienda". Esto llevará al usuario a otro url donde le indicará la existencia o no de la tienda, y en caso de encontrarse en la base de datos información adicional relacionada con ciudad y descripción de la activdad de la tienda. 

## Creación, actualización y eliminación de usuarios usando clases propias de Django
Usando clases propias de Django la app permite crear, actualizar y eliminar usuarios. 
Es importante considerar que sólo usuarios que inicien sesión como superusuario o que pertenezcan al staff, en el panel de administración pueden modificar contactos ya creados desde la app. 
Solo usuarios que inicien sesión como superusuario pueden eliminar usuarios ya creados en la app. 



