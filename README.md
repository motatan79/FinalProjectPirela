# Proyecto Final Coder House - Python Flex
Comisión: 56060.

Creador: Pirela, Moises.
## Nombre del Proyecto
KIDDO SWAPP 
## Versión
1.0

# DESCRIPCIÓN DEL PROYECTO 

KIDDO SWAPP
Es una app de intercambio de ropa de segunda mano para niños, con presencia en Latinoamérica. 

## Extraer el contenido desde el siguiente repositorio en git con el siguiente comando
git clone https://github.com/motatan79/FinalProjectPirela.git

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
- En la página de inicio, esquina superior izquierda, al pulsar sobre el nombre de APP siempre retornará a la página de Inicio, al igual que al pulsar la palabra INICIO en la barra de navegación. 
- En la barra de navegación al pulsar la Palabra Nosotros, llevará al usuario a información relacionada con Kiddo Swapp. Para retornar al inicio puede pulsar sobre el nombre de la app o la palabra INICIO.
- El botón Whatsapp, llevará al usuario a la app de Whatsapp y podrá comenzar a interactuar con nuestro equipo. 
- En la página de inicio, en la esquina inferior izquierda al pulsar las palabras "Servicios" o "Contáctanos", se obtienen información relacionada con la Kiddo Swapp. 

## Para realizar la búsqueda de información en la base de datos (Buscar Tienda).
En la Pantalla Inicio, al colocar el nombre de una tienda y presionar el botón "Buscar Tienda". Esto llevará al usuario a otro url donde le indicará la existencia o no de la tienda, y en caso de encontrarse en la base de datos mostrará información adicional relacionada con ciudad y descripción de la activdad de la tienda. 


## En la barra de navegación lado derecho, hay dos funciones adicionales: 
- Registrarse. El usuario podrá registrarse en la app, creando una cuenta con nombre de usuario y contraseña, los cuales deben cumplir con las especificaciones mencionadas en la url. Si presiona el Boton Cancelar será redirigido al inicio.
- Acceder. El usuario, previamente registrado en la app, podrá acceder a una nueva url colocando su nombre de usuario  y contraseña y presionando el Botón Iniciar Sesión. En caso de presionar el Botón Cancelar, se redirigira al inicio.

## USUARIO ACCEDE CON SU NOMBRE DE USUARIO Y CONTRASEÑA. 
El usuario conectado a la app, con nombre y contraseña, además de visualizar su nombre de usuario en la barra de navegación, tendrá acceso a nuevas funcionalidades dentro de la barra de navegación.
- Perfil. Podrá ver: 
    - Lista de usuarios (Swapper) registrados y su país, y: 
        - Botón Ver. El usuario podrá ver el detalle de cada Swapper al presionar el Botón Ver que se muestra en la lista. El usuario podrá ver la información (id, email, país, teléfono, fecha de nacimiento, tienda, dueño de tienda). 
    - Crear Perfil. 
        - Registrar PERFIL. El usuario podrá completar su perfil, rellenando el formulario y presionando el Botón Registrar PERFIL. El Botón Registrar PERFIL llevará al usuario a la página anterior pero en este caso en la lista de Swappers podrá ver al final de la lista su usuario.
        - Atrás. El usuario podrá presionar el Botón Atrás para volver a la pantalla anterior que incluye la lista de Swappers y botón para Crear PERFIL. 
    - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.

- Tienda. En esta página podra visualizar: 
    - Registrar Tienda. Para registrar una nueva tienda deberá completar el formulario y presionar el botón Registrar Tienda. Luego verá una lista de tiendas registradas y al final de la lista la tienda recientemente registrada. 
        - Atrás. El usuario podrá presionar el Botón Atrás para volver al formulario de registro de tienda.
    - Tiendas Registradas. Para consultar las tiendas existentes deberá presionar el botón Tiendas Registradas.
        - Atrás. El usuario podrá presionar el Botón Atrás para volver al formulario de registro de tienda.
    
- País. En esta página podra visualizar:
    - Registrar País. Para registrar un nuevo país deberá completar el formulario y presionar el botón Registrar País. Luego verá una lista de países registrados y al final de la lista el país recientemente agregado. 
        - Atrás. El usuario podrá presionar el Botón Atrás para volver al formulario de registro de país.
    - Países Registrados. Para consultar los países existentes deberá presionar el botón Países Registrads.
        - Atrás. El usuario podrá presionar el Botón Atrás para volver al formulario de registro de país.

- Evento. En esta página podra visualizar:
    - Registrar Evento. Para registrar un nuevo evento deberá completar el formulario, vinculando el evento a un Patrocinante, País y Tienda Patrocinante existentes. Y además indicar si el evento es gratis o requiere una Cuota de Participación. En caso de ser gratis deberá completar la Cuota de Participación con cero (0). Cuando el formulario esté completo presionar el botón Registrar Evento. Luego verá una lista de eventos registrados y al final de la lista el evento recientemente registrado. 
        - Atrás. El usuario podrá presionar el Botón Atrás para volver al formulario de registro de evento.
    - Eventos Registrados. Para consultar los eventos existentes deberá presionar el botón Eventos Registrados.
        - Atrás. El usuario podrá presionar el Botón Atrás para volver al formulario de registro de evento.

- Nombre de Usuario. El Usuario verá su nombre de USUARIO en LETRAS MAYÚSCULAS para saber que se encuentra conectado.

- Logout. El usuario podrá presionar el Botón Logout para cerrar la sesión y le será indicado con un mensaje que el cierre de sesión fue exitoso y la barra de navegación contendrá solamente las funcionalidades descritas al inicio para un usuario no conectado. Además el usuario podrá presionar sobre el mensaje "Ingresa de nuevo" para redirigirlo a la pantalla a la url de login. 

## USUARIO ACCEDE CON CREDENCIALES DE ADMINISTRADOR. 
## Creación, actualización y eliminación de usuarios usando clases propias de Django
Los usuarios que accedan con credenciales de administrador, en la página de inicio tendrán las mismas funcionalidades que los usuarios conectados a la app. 
Así como todo las funcionalidades de la barra de navegación (crear perfiles, tiendas, países y eventos) y la barra de búsqueda de tienda, descritas en el apartado anterior.

En dicha página de Inicio también contarán con un boton Administración que permite acceder al menú de Administración de Django, pudiendo en este eliminar, crear y cambiar la información de los usuarios, tiendas, países y eventos. 

Otro privilegio exclusivo del administrador será actualizar y eliminar perfiles de Swappers, desde la barra de navegación accediendo a través de Perfil:
-   Perfil. Podrá ver:
    - Lista de swapper registrados y su país, y: 
        - Ver. El administrador podrá ver el detalle de cada Swapper al presionar el Botón Ver (id, email, país, teléfono, fecha de nacimiento, tienda, dueño de tienda).
            - Editar. El administrador podrá presionar el Botón Editar para editar la información de un Swapper rellenando el formulario y presionando el Botón Guardar Contacto. Luego se redirigirá a la pantalla de detalle del usuario.
            - Eliminar. El administrador podrá presionar el Botón Eliminar para eliminar un Swapper de la base de datos. Aparecerá un mensaje de confirmación de la acción de eliminar el Swapper y dos botones.
                - Borrar Contacto. Al presiomar este botón el administrador confirma la eliminación del Swapper. Luego se redirigira a la pantalla de Perfil con la lista de Swappers registrados sin el usuario recientemente eliminado. 
                - Cancelar. Al presionar este botón se redirigira a la pantalla de detalle de  los datos del Swapper.
            - Atrás. Para volver a la página anterior deberá presionar Botón Atrás. 
        - Editar. El administrador será redirigido a la pantalla de edición del formulario de datos del Swapper, debe rellenar los campos que desea editar. Podrá realizar dos acciones:
            - Guardar Contacto.  Actualiza la información del Swapper que queda guardada en la base de datos y en el detalle del perfil del Swapper. 
            - Atrás. No actualiza la información del Swapper y se redirige a la pantalla de Perfil.
        - Eliminar. El administrador podrá presionar el Botón Eliminar para eliminar un Swapper de la base de datos. Aparecerá un mensaje de confirmación de la acción de eliminar el Swapper y dos botones.
            - Borrar Contacto. Al presiomar este botón el administrador confirma la eliminación del Swapper. Luego se redirigira a la pantalla de Perfil con la lista de Swappers registrados sin el usuario recientemente eliminado. 
            - Cancelar. Al presionar este botón se redirigira a la pantalla de detalle de  los datos del Swapper.   
    - Crear Perfil. 
        - Registrar. El usuario podrá completar su perfil, rellenando el formulario y presionando el Botón Registrar. El Botón Registrar llevará al usuario a la página anterior pero en este caso en la lista de Swappers podrá ver al final de la lista su usuario.
        - Cancelar. En caso de presionar el Botón Cancelar, se redirigira al inicio. 
    - Atrás. El usuario podrá presionar el Botón Atrás para volver a la página inicio.
 
## Video Demostración
https://youtu.be/o_wWXDTXg6M
