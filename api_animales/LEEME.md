# API REST de animales

Proyecto sencillo con Django REST Framework y MySQL, sin autenticación.

## Abrir en esta computadora

1. Haz doble clic en `INICIAR.bat`.
2. Espera a que termine de preparar la base de datos y abrir Postman.
3. Deja abierta la ventana negra mientras haces la demostración.
4. En Postman usa http://127.0.0.1:8000/api/animales/ .

Las seis pruebas se hicieron en **Postman Desktop 12.36.3**, en modo sin cuenta:
POST, GET lista, GET por id, PUT, POST inválido y DELETE. Las solicitudes quedan
en History y en las pestañas abiertas de Postman. Para repetirlas, crea un animal
con POST y usa el nuevo id en GET por id, PUT y DELETE.
Para enviar JSON selecciona **Body > raw > JSON** y pulsa **Send**.
DELETE elimina el animal creado para la demostración; úsalo al final.
Se retiró la pantalla de pruebas propia. Django conserva exclusivamente la API.
En `postman/` se incluye la colección exportable con las seis solicitudes;
su importación como colección requiere el modo con cuenta. La guía explica el
procedimiento manual sin cuenta, que es el usado en las capturas entregables.

El documento que se debe entregar es `output/pdf/entregable_serie_4.pdf`:
incluye portada, seis capturas y el inciso B de React con un fragmento de 14 líneas.
`output/pdf/guia_demostracion.pdf` es únicamente tu apoyo personal para la exposición.
El ZIP es un respaldo del código; la consigna pide entregar un único PDF.

Repositorio indicado: https://github.com/CrisLeonardo/Examen-Final-Desarrollo-web.git

## Requisitos y base de datos

Python 3.14 y las versiones de `requirements.txt`. En esta computadora ya quedaron
instalados. `INICIAR.bat` instala las dependencias si falta el entorno virtual.
La primera preparación de MySQL requiere Internet y descarga unos 268 MB.

MySQL Community Server 8.4.13 se instala en `%LOCALAPPDATA%\ExamenAnimales`.
Los datos quedan en la subcarpeta `data`, fuera del código. No se usa SQLite ni XAMPP.
La conexión local usa host `127.0.0.1`, puerto `3307`, base `examen_animales`,
usuario `examen_animales` y contraseña de demostración `AnimalesDemo2026!`.
Solo tiene permisos en la base del proyecto y en su base de pruebas. La clave aleatoria de root queda en
`%LOCALAPPDATA%\ExamenAnimales\root_local.json`; no se incluye en la entrega.
Estos ajustes son para una demostración local. Se pueden cambiar con las variables
`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` y `DB_PORT` en `config/settings.py`.

## Operaciones

| Método | Ruta | Uso |
| --- | --- | --- |
| GET | `/api/animales/` | Obtener todos los animales |
| GET | `/api/animales/1/` | Obtener un animal por su id |
| POST | `/api/animales/` | Guardar un animal |
| PUT | `/api/animales/1/` | Reemplazar los cuatro datos |
| PATCH | `/api/animales/1/` | Actualizar uno o más datos |
| DELETE | `/api/animales/1/` | Eliminar un animal |

El id de la tabla es automático. También se generan `created_at` y `updated_at`.
Para POST envía este JSON desde la pantalla de pruebas:

```json
{"nombre": "Luna", "especie": "Perro", "raza": "Labrador", "edad": 3}
```

POST correcto responde **201 Created**; GET, **200 OK**. Si faltan campos o la edad
es negativa, responde **400 Bad Request**. Un id inexistente responde **404 Not Found**.

## Archivos principales

- `animales/models.py`: modelo y campos de la tabla `animales`.
- `animales/serializers.py`: validación de entrada y conversión a JSON.
- `animales/views.py`: operaciones REST con `ModelViewSet`.
- `config/urls.py`: rutas generadas con el router.
- `animales/migrations/`: creación reproducible de la tabla.
- `postman/Animales.postman_collection.json`: seis solicitudes listas para importar.
- `react/ListaAnimales.jsx`: fragmento de 14 líneas del inciso B.
- `evidencias/`: seis capturas con URL, respuestas HTTP y consultas directas a MySQL.
- `evidencias/cumplimiento.md`: revisión de cada requisito del apartado de 10 puntos.

## Ejecutar pruebas

Con MySQL iniciado, desde una terminal abierta en esta carpeta:

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test animales --noinput
```

Las pruebas usan una base aparte llamada `test_examen_animales` y no borran los
registros de demostración. En una instalación propia, el usuario necesita permisos
para crear y borrar esa base de pruebas.

## Alcance de la consigna recibida

Se implementó la sección visible de la imagen: elegir Animales o Vehículos,
Laravel o Django REST Framework, conexión MySQL, modelo, tabla, cuatro atributos,
identificador, fechas y ausencia de autenticación. También se incluyen pruebas CRUD.
Se incluyó también el inciso B, de 5 puntos: descripción de useState, useEffect,
fetch y map con key, y fragmento de React de máximo 15 líneas con la URL real.
La explicación oral puede centrarse en el apartado a), según la aclaración recibida.
El fragmento React asume que se sirve desde el mismo origen de la API. Si se usa
un servidor de desarrollo separado, se necesita un proxy o configurar CORS.

Referencias: https://www.django-rest-framework.org/tutorial/quickstart/
y https://docs.djangoproject.com/en/5.2/topics/install/ .
