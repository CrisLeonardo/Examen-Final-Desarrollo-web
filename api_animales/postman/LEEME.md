# Pruebas con Postman

Postman ya está instalado en esta computadora. Abre INICIAR.bat para iniciar
la API y abrir Postman. Mantén la ventana del servidor abierta.

Sin cuenta: elige Continue without an account > Open Lightweight API Client.
Usa Ctrl+T para una solicitud nueva, selecciona el método y escribe la URL.
En POST y PUT selecciona Body > raw > JSON. Presiona Send para enviar.

Las seis pruebas realizadas están en el historial de Postman y la guía personal
explica cómo repetirlas. El id de las capturas fue eliminado en la última prueba:
crea un registro nuevo y escribe su id en las solicitudes individuales.

Si ya tienes una cuenta de Postman, también puedes importar
Animales.postman_collection.json mediante Import. Ejecuta las solicitudes en orden;
el script del primer POST conserva el id automáticamente en animal_id.
base_url ya tiene el valor http://127.0.0.1:8000.
