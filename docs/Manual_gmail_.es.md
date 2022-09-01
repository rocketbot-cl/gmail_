# Gmail
  
Módulo para realizar acciones en Gmail  



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


## Descripción de los comandos

### Configurar Servidor
  
Con este comando habilitamos la ejecucion de los demas comandos, configurando el servidor con nuestro mail y contraseña.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Usuario|Correo electrónico a utilizar|user@example.com|
|Contraseña|Contraseña del correo electrónico o contraseña de aplicación|******|
|SSL Connection|Habilitar conexión SSL|Variable|
|Asignar resultado a Variable|Nombre de la variable donde se almacenará el resultado|Variable|

### Enviar Email
  
Envia un email, previamente debe configurar el servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Para|Indica el destinatario, para varios destinatarios separar por coma|to@mail.com, to2@mail.com|
|Copia|Indica el destinatario, para varios destinatarios separar por coma|cc@mail.com, cc2@mail.com|
|Copia Oculta|Seleccionar para enviar una copia oculta|bcc@mail.com, bcc2@mail.com|
|Asunto|Indica el asunto del email|This is a test email|
|Mensaje|Indica el cuerpo del email|Hi from Rocketbot!|
|Archivo Adjunto|Selecciona un archivo para adjuntar|C:/User/Desktop/test.txt|
|Carpeta (Varios archivos)|Selecciona una carpeta para adjuntar varios archivos|C:/User/Desktop/Files|

### Lista todos los email
  
Lista todos los email, se puede especificar un filtro
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro|Filtro de mail. Dejar vacío para traerlos todos|SUBJECT test|
|Carpeta|Carpeta de mail. Dejar vacío para traer unicamente de INBOX|Carpeta|
|Asignar a variable|Nombre de la variable donde se almacenará el resultado|Variable|

### Lista emails no leídos
  
Lista emails no leídos. Puedes especificar un filtro.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro|Filtro que se desea aplicar en la busqueda de los mails no leidos.|SUBJECT test|
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

### Responder email por ID
  
Responde un email por su ID, teniendo la posibilidad de agregar un cuerpo de mensaje y archivos adjuntos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID Email|ID del email a responder|355|
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

### Cerrar Conexión
  
Cierra la conexión del servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
| --- | --- | --- |

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
|Ruta para descargar adjuntos|Ruta donde se guardarán los adjuntos|C:/User/Desktop|
