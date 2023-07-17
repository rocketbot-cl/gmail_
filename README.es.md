# Gmail
  
Módulo para realizar acciones en Gmail  

*Read this in other languages: [English](README.md), [Portugues](README.pr.md), [Español](README.es.md).*

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  


## Como usar este módulo
Para usar este modulo debemos realizar la siguiente configuracion en nuestra cuenta de Gmail:
1. Ir a la seccion de "Gestionar tu cuenta de Google"
2. Luego iremos al apartado de "Seguridad" que se encuentra en el panel izquierdo.
3. Activar verificación en dos pasos
4. En la opción "Acceso a Google" acceder a Contraseñas de aplicaciones.
5. En "Seleccionar aplicación" colocamos 'Otro' y le asignamos un nombre para identificarla.
6. Hacemos click en el botón Generar y copiamos la contraseña de aplicación generada.
7. En el módulo gmail_ colocamos el email elegido y como contraseña se utiliza la contraseña de aplicación generada.



## Overview


1. Configurar Servidor  
Con este comando habilitamos la ejecucion de los demas comandos, configurando el servidor con nuestro mail y contraseña.

2. Enviar Email  
Envia un email, previamente debe configurar el servidor

3. Lista todos los email  
Lista todos los email, se puede especificar un filtro

4. Lista emails no leídos  
Lista emails no leídos. Puedes especificar un filtro.

5. Leer email por ID  
Lee un email por ID y obtiene todos los datos del email, el cuerpo de mensaje y sus archivos adjuntos

6. Obtener datos de tabla de email por ID  
Lee un email por ID y devuelve una lista de los datos de las tablas del cuerpo del email

7. Responder email por ID  
Responde un email por su ID, teniendo la posibilidad de agregar un cuerpo de mensaje y archivos adjuntos

8. Crear Etiqueta  
Crea una etiqueta en Gmail, donde podremos mover nuestros mails teniendo el comportamiento de una carpeta.

9. Mover email a etiqueta  
Mueve un email a una etiqueta. Debemos tener en cuenta el ID del mail a mover y el nombre de la etiqueta

10. Marcar email como no leído  
Marcar email como no leído indicando su ID

11. Cerrar Conexión  
Cierra la conexión del servidor

12. Reenviar email por ID  
Reenviar email por ID. Indicamos el o los destinatarios a quien reenviar el mail y la posibilidad de cambiar el asunto

13. Descargar adjuntos por ID  
Descarga los archivos adjuntos de un correo y los guarda en una carpeta  



### Changes
Mon Aug 29 20:20:55 2022  [hidden] steps to generate application password in manual.
Wed Feb 17 13:47:47 2021  Merge branch master of https://github.com/rocketbot-cl/gmail_
Wed Sep 2 10:43:37 2020  Merge branch master of https://github.com/rocketbot-cl/gmail_
Fri Nov 15 15:36:49 2019  Merge branch master of https://github.com/rocketbot-cl/Gmail
Tue Nov 5 14:32:16 2019  Merge branch master of https://github.com/rocketbot-cl/Gmail

----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**mail-parser**](https://pypi.org/project/mail-parser/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)