# App-web-con-Flask-Javascript
App web que grafica los niveles de contaminación ambiental de material particulado 1.0, 2.5 y 10 ug/m3 y la temperatura de manera dinámica. La app cuenta con un bot el cual al hacer click en los botones se envía el grafico dinámico asociado a su SmartPhone cuenta Telegram. Se utiliza la librería Canvas.js y python telegram bot 20.0 
de python junto con Web Server Flask  el cual envia estos datos en tiempo real. </br>
La app cuenta con un mapa de la ciudad de Temuco con 5 estaciones ambientales (marcadores). Haciendo click sobre cualquiera de ellos se grafican los 
niveles de contaminación de manera dinámica asociado a ese marcador.</br>
Además la aplicación muestra el mapa de Temuco con las rutas de los vehículos en la base de dato gps.db de SQLite. Haciendo click sobre los botones se graficará la ruta del vehículo 
asociado en el mapa. En la tabla data esta toda la información de los 10 vehículos. El Web Server Flask, enviará toda la información JSON a Jquery Javascript de la página html 
asociada. Por el lado del Web Server Flask, se debe recibirá la clave del vehiculo a buscar en la tabla data.

Para probar en forma local basta con iniciar el Web Server Flask. La ruta principal se ubica en: http://127.0.0.1:5000/1

Se trabaja con las librerias: random </br>
requests </br>
time </br>
csv </br>
sqlite3 </br>
json </br>
base64 </br>
telegram </br>
PIL </br>
io </br>
base64 </br> 



