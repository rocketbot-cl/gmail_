



# Gmail
  
Módulo para realizar acciones en Gmail  

*Read this in other languages: [English](Manual_gmail_.md), [Português](Manual_gmail_.pr.md), [Español](Manual_gmail_.es.md)*
  
![banner](imgs/Banner_gmail_.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## How to use this module

To use this module we will have to make the following configuration in our Gmail account:
1. Go to the "Manage your Google Account" section.
2. Then we will go to the section of "Security" that is in the left panel.
3. Activate two-step verification
4. In the "Access to Google" option, access Application passwords.
5. In "Select application" we place 'Other' and assign it a name to identify it.
6. We click on the Generate button and copy the generated application password.
7. In the gmail_ module we place the chosen email and as password we use the generated application password.

Documentation to generate application password: https://docs.rocketbot.com/2024/08/07/crear-contrasena-de-aplicacion-para-gmail/


## Descripción de los comandos

### Configurar Servidor
  
Con este comando habilitamos la ejecucion de los demas comandos, configurando el servidor con nuestro mail y contraseña.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Usuario|Correo electrónico a utilizar|user@example.com|
|Contraseña|Contraseña del correo electrónico o contraseña de aplicación|******|
|SSL Connection|Habilitar conexión SSL|True|
|Asignar resultado a Variable|Nombre de la variable donde se almacenará el resultado sin {}|Variable|

### Enviar Email
  
Envia un email, previamente debe configurar el servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|De|Opcional. Indica el nombre del remitente del email|Test|
|Para|Indica el destinatario, para varios destinatarios separar por coma|to@mail.com, to2@mail.com|
|Copia|Indica a quien enviar copia, para varios destinatarios separar por coma|cc@mail.com, cc2@mail.com|
|Copia Oculta|Seleccionar para enviar una copia oculta|bcc@mail.com, bcc2@mail.com|
|Asunto|Indica el asunto del email|This is a test email|
|Mensaje|Indica el cuerpo del email|Hi from Rocketbot!|
|Archivo Adjunto|Selecciona un archivo para adjuntar|C:/User/Desktop/test.txt|
|Carpeta (Varios archivos)|Selecciona una carpeta para adjuntar varios archivos|C:/User/Desktop/Files|

### Lista todos los email
  
Lista todos los email, se puede especificar un filtro
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro|Filtro de mail. Luego del filtro, se debe colocar el parametro de busqueda en comillas dobles. Dejar vacío para traerlos todos|SUBJECT "Example text"|
|Carpeta|Carpeta de mail. Dejar vacío para traer unicamente de INBOX|Carpeta|
|Asignar a variable|Nombre de la variable donde se almacenará el resultado|Variable|

### Lista emails no leídos
  
Lista emails no leídos. Puedes especificar un filtro.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro|Filtro a aplicar a los mails no leídos. Luego del filtro, se debe colocar el parametro de busqueda en comillas dobles. Dejar vacío para traer todos los no leídos.|SUBJECT "Example text"|
|Label|Nombre de la carpeta donde buscar el mail. Si no es un label nativo de gmail, escribir el nombre con comillas|[Gmail]/Todos|
|Asignar a variable|Variable donde se guardarán los mails no leidos.|Variable|

### Leer email por ID
  
Lee un email por ID y obtiene todos los datos del email, el cuerpo de mensaje y sus archivos adjuntos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|ID del email a leer|345|
|Label|Nombre de la carpeta donde buscar el mail. Si no es un label nativo de gmail, escribir el nombre con comillas|[Gmail]/Todos|
|Asignar a variable|Nombre de variable donde se guardará el email|Variable|
|Ruta para descargar adjuntos|Ruta donde se guardarán los adjuntos|C:/User/Desktop|

### Obtener datos de tabla de email por ID
  
Lee un email por ID y devuelve una lista de los datos de las tablas del cuerpo del email
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|ID del email a leer|345|
|Asignar a variable|Nombre de variable donde se guardará la lista de datos de la tabla|Variable|

### Responder email por ID
  
Responde un email por su ID, teniendo la posibilidad de agregar un cuerpo de mensaje y archivos adjuntos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Email|ID del email a responder|355|
|Carpeta|Carpeta de mail. Dejar vacío para traer unicamente de INBOX|Carpeta|
|Mensaje|Mensaje a reenviar|This is a test response|
|Archivo Adjunto|Archivo adjunto que se reenviara junto al mail|C:/User/Desktop/test.txt|

### Crear Etiqueta
  
Crea una etiqueta en Gmail, donde podremos mover nuestros mails teniendo el comportamiento de una carpeta.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre Etiqueta|Nombre de la etiqueta a crear|test_label|

### Mover email a etiqueta
  
Mueve un email a una etiqueta. Debemos tener en cuenta el ID del mail a mover y el nombre de la etiqueta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|ID del email que se movera a otro label|345|
|Nombre de la etiqueta|Nombre de la etiqueta a la que se movera el email|test|
|Asignar resultado a variable|Nombre de la variable a la que se asignara el resultado|Variable|

### Marcar email como no leído
  
Marcar email como no leído indicando su ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|ID del email a marcar como no leído|345|
|Carpeta|Carpeta de mail. Dejar vacío para traer unicamente de INBOX|Carpeta|

### Reenviar email por ID
  
Reenviar email por ID. Indicamos el o los destinatarios a quien reenviar el mail y la posibilidad de cambiar el asunto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Email|ID del email a reenviar|355|
|Email|Email de destino|test@email.com|

### Descargar adjuntos por ID
  
Descarga los archivos adjuntos de un correo y los guarda en una carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del email|ID del email a leer|345|
|Label|Nombre de la carpeta donde buscar el mail. Si no es un label nativo de gmail, escribir el nombre con comillas|[Gmail]/Todos|
|Extensiones|Extensiones de los archivos a descargar. Separar por comas|pdf,jpg,xslx|
|Ruta para descargar adjuntos|Ruta donde se guardarán los adjuntos|C:/User/Desktop|

### Cerrar Conexión
  
Cierra la conexión del servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
