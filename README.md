Pre Entrega # 3
Tú Primera Página

KIDDO SWAPP
Es una app de intercambio de ropa de segunda mano para niños, con presencia en Latinoamérica. 

## Extraer el contenido desde el siguiente repositorio en git con el siguiente comando
git clone https://github.com/motatan79/TuPrimeraPaginaPirela.git

## Para ingresar al proyecto se debe crear un ambiente virtual en la terminal
- python -m venv .venv (Windows)
- python3 -m venv .venv (Linux o Mac)

## Posteriormente activar el entorno virtual
- .\.venv\Scripts\activate (Windows Powershell)
- source .venv/bin/activate (Linux o Mac)

## Instalar Django
pip install django


## Ejecutar el servidor
python manage.py runserver

## En la página inicio (Usuario sin sesión activa)
En la página de inicio, esquina superior izquierda, al pulsar sobre el nombre de APP siempre retornará a la página de Inicio, al igual que al pulsar la palabra INICIO en la barra de navegación. 
En la barra de navegación al pulsar la Palabra Nosotros, llevará al usuario a información relacionada con Kiddo Swapp. Para retornar al inicio puede pulsar sobre el nombre de la app o la palabra INICIO.
El botón Whatsapp, llevará al usuario a la app de Whatsapp y podrá comenzar a interactuar con nuestro equipo. 
En la página de inicio, en la esquina inferior izquierda al pulsar las palabras "Servicios" o "Contáctanos", se obtienen información relacionada con la Kiddo Swapp. 

## Para realizar la búsqueda de información en la base de datos (Buscar Tienda).
En la Pantalla Inicio, colocar el nombre de una tienda y presionar el botón "Buscar Tienda". Esto llevará al usuario a otro url donde le indicará la existencia o no de la tienda, y en caso de encontrarse en la base de datos información adicional relacionada con ciudad y descripción de la activdad de la tienda. 


## En la página de inicio, barra de navegación lado derecho, hay dos funciones adicionales: 
- Registrarse. El usuario podrá registrarse en la app, creando una cuenta con nombre de usuario y contraseña, los cuales deben cumplir con las especificaciones mencionadas en la url. Si presiona el Boton Cancelar será redirigido al inicio.
- Acceder. El usuario, previamente registrado en la app, podrá acceder a una nueva url colocando su nombre de usuario  y contraseña y presionando el Botón Iniciar Sesión. En caso de presionar el Botón Cancelar, se redirigira al inicio.

## USUARIO ACCEDE CON SU NOMBRE DE USUARIO Y CONTRASEÑA. 
El usuario conectado a la app, con nombre y contraseña, además de visualizar su nombre de usuario en la barra de navegación, tendrá acceso a nuevas funcionalidades dentro de la barra de navegación.
- Perfil. Podrá ver: 
    - Lista de usuarios (Swapper) registrados y su país, y: 
        - Botón Ver. El usuario podrá ver el detalle de cada Swapper al presionar el Botón Ver que se muestra en la lista. El usuario podrá ver la información (id, email, país, teléfono, fecha de nacimiento, tienda, dueño de tienda). 
    - Crear Perfil. 
        - Registrar. El usuario podrá completar su perfil, rellenando el formulario y presionando el Botón Registrar. El Botón Registrar llevará al usuario a la página anterior pero en este caso en la lista de Swappers podrá ver al final de la lista su usuario.
        - Cancelar. En caso de presionar el Botón Cancelar, se redirigira al inicio. 
    - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.

- Tienda. En esta página podra visualizar: 
    - Registrar Tienda. Para registrar una nueva tienda deberá completar el formulario y presionar el botón Registrar Tienda. Luego verá una lista de tiendas registradas y al final de la lista la tienda recientemente registrada. 
        - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.
    - Tiendas Registradas. Para consultar las tiendas existentes deberá presionar el botón Tiendas Registradas.
        - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.
    
- País. En esta página podra visualizar:
    - Registrar País. Para registrar un nuevo país deberá completar el formulario y presionar el botón Registrar País. Luego verá una lista de países registrados y al final de la lista el país recientemente registrado. 
        - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.
    - Países Registrados. Para consultar los países existentes deberá presionar el botón Países Registrads.
        - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.

- Evento. En esta página podra visualizar:
    - Registrar Evento. Para registrar un nuevo evento deberá completar el formulario, vinculando el evento a un Patrocinante, País y Tienda Patrocinante existentes. Y además indicar si el evento es gratis o requiere una Cuota de Participación. En caso de ser gratis deberá completar la Cuota de Participación con cero (0). Cuando el formulario esté completo presionar el botón Registrar Evento. Luego verá una lista de eventos registrados y al final de la lista el evento recientemente registrado. 
        - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.
    - Eventos Registrados. Para consultar los eventos existentes deberá presionar el botón Eventos Registrads.
        - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.

- Nombre de Usuario. El Usuario verá su nombre de USUARIO en LETRAS MAYÚSCULAS para saber que se encuentra conectado.

- Logout. El usuario podrá presionar el Botón Logout para cerrar la sesión y volver a la pagina de inicio. Donde solamente podrá ver en la barra de navegación las funcionalidades descritas al inicio para un usuario no conectado. 

## USUARIO ACCEDE CON SU CREDENCIALES DE ADMINISTRADOR. 
## Creación, actualización y eliminación de usuarios usando clases propias de Django
Los usuarios que accedan con credenciales de administrador, en la página de inicio tendrán las mismas funcionalidades que los usuarios conectados a la app.
Así como todo las funcionalidades de la barra de navegación (crear perfiles, tiendas, países y eventos) y la barra de búsqueda de tienda, descritas en el apartado anterior.

Sólo el administrador podrá actualizar y eliminar perfiles de swappers en la app, desde la barra de navegación accediendo a través de Perfil:
-   Perfil. Podrá ver:
    - Lista de swapper registrados y su país, y: 
        - Ver. El usuario podrá ver el detalle de cada Swapper al presionar el Botón Ver (id, email, país, teléfono, fecha de nacimiento, tienda, dueño de tienda). Para volver a la página anterior deberá presionar Botón Atrás. 
        - Editar. El usuario podrá presionar el Botón Editar para editar la información de un Swapper rellenando el formulario y presionando el Botón Guardar Contacto perfil. Luego se redirigira a la pantalla de edición.

    - Crear Perfil. 
        - Registrar. El usuario podrá completar su perfil, rellenando el formulario y presionando el Botón Registrar. El Botón Registrar llevará al usuario a la página anterior pero en este caso en la lista de Swappers podrá ver al final de la lista su usuario.
        - Cancelar. En caso de presionar el Botón Cancelar, se redirigira al inicio. 
    - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.


Usando clases propias de Django la app permite actualizar y eliminar swappers. 
Es importante considerar que sólo usuarios que inicien sesión como superusuario o que pertenezcan al staff, en el panel de administración pueden modificar contactos ya creados desde la app. 
Solo usuarios que inicien sesión como superusuario pueden eliminar o actualizar swappers ya creados en la app. 



