



# Gmail
  
Módulo para realizar acciones en Gmail  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


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

11. Reenviar email por ID  
Reenviar email por ID. Indicamos el o los destinatarios a quien reenviar el mail y la posibilidad de cambiar el asunto

12. Descargar adjuntos por ID  
Descarga los archivos adjuntos de un correo y los guarda en una carpeta

13. Cerrar Conexión  
Cierra la conexión del servidor  

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