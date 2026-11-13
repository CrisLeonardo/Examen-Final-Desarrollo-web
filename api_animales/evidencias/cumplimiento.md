# Revisión de la Serie 4: apartados a) y b)

| Requisito visible | Implementación y evidencia |
| --- | --- |
| Elegir Animales o Vehículos | Clase `Animal` en `animales/models.py`. |
| Laravel o Django REST Framework | Django 5.2.19 y Django REST Framework 3.18.3, fijados en `requirements.txt`. |
| No implementar autenticación | Sin clases de autenticación, acceso AllowAny y sin aplicación de usuarios. Las seis peticiones de prueba se enviaron sin credenciales ni tokens. |
| Conectar a MySQL | Backend `django.db.backends.mysql`, servidor MySQL Community 8.4.13, base `examen_animales`, puerto 3307. Versión, nombre de base y estructura obtenidos directamente por SQL en `resultados_http_mysql.json`. |
| Crear modelo y tabla | Modelo `Animal`, tabla `animales` y migración `0001_initial.py`, aplicada correctamente. |
| Al menos cuatro atributos | `nombre`, `especie`, `raza`, `edad`. |
| Identificador adicional | `id`, entero autoincremental generado por Django/MySQL. |
| Fechas de creación y actualización | `created_at` con auto_now_add y `updated_at` con auto_now. Se verificó que al editar cambia la segunda y se conserva la primera. |
| Desarrollo y pruebas REST | POST, GET de lista, GET por id, PUT, POST inválido y DELETE, en el orden exacto de la consigna, ejecutados en Postman Desktop 12.36.3 (Lightweight API Client). |
| Respuestas JSON | JSONRenderer y Content-Type application/json comprobado en todas las respuestas con cuerpo. DELETE devuelve 204 sin cuerpo. |
| Validación obligatoria | Se rechazan nombre vacío, especie y raza ausentes y edad negativa con estado 400 y errores JSON. |
| Inciso B (5 puntos) | Descripción de useState, useEffect, fetch y map con key en el PDF; fragmento de 14 líneas en react/ListaAnimales.jsx con la URL real de la API. |
| Único PDF entregable | output/pdf/entregable_serie_4.pdf: portada con nombre, recurso y herramienta; seis capturas con URL/cuerpo/respuesta/estado; descripción y código React. |

## Seis capturas con URL visible

Cada imagen muestra el método, la URL completa realmente utilizada, los datos
enviados y el estado HTTP devuelto por el servidor. No se utiliza una respuesta simulada.

| Captura | Solicitud | Estado observado |
| --- | --- | --- |
| `01_crear.jpg` | POST `http://127.0.0.1:8000/api/animales/` | 201 Created |
| `02_lista.jpg` | GET `http://127.0.0.1:8000/api/animales/` | 200 OK |
| `03_detalle.jpg` | GET al id creado, visible en la captura | 200 OK |
| `04_reemplazar.jpg` | PUT al mismo id, con los cuatro atributos | 200 OK |
| `05_invalido.jpg` | POST a la lista, con campos inválidos y obligatorios ausentes | 400 Bad Request |
| `06_eliminar.jpg` | DELETE al mismo id | 204 No Content |

El JSON adjunto registra las URL completas de las seis solicitudes. El id utilizado
en estas capturas se eliminó en la última prueba. Para repetirlas se debe crear un
registro nuevo con POST; la pantalla selecciona automáticamente su nuevo id.

## Verificaciones adicionales

- Se comprobó directamente en MySQL el registro creado en Postman después de PUT.
- PUT cambió la edad a 4 en MySQL, conservó created_at y actualizó updated_at.
- DELETE dejó de tener una fila en MySQL; un GET posterior devolvió 404.
- Los datos incompletos y la edad negativa se rechazaron con 400.
- Las pruebas automatizadas de `animales/tests.py` cubren CRUD y validaciones,
  usando una base de pruebas separada. Resultado en `pruebas.txt`.

La herramienta usada es Postman Desktop, una de las enumeradas en la consigna.
Las capturas son de su aplicación real y se tomaron después de enviar las peticiones.
El cliente web propio fue retirado del código y del paquete de entrega.
