"""Prepara únicamente la base de datos local de esta demostración."""
import json
import os
import secrets
import time
from pathlib import Path
import MySQLdb

credentials = Path(os.environ['LOCALAPPDATA']) / 'ExamenAnimales' / 'root_local.json'
password = json.loads(credentials.read_text())['password'] if credentials.exists() else ''
for attempt in range(30):
    try:
        connection = MySQLdb.connect(host='127.0.0.1', port=3307, user='root', passwd=password)
        break
    except MySQLdb.OperationalError as error:
        if error.args[0] != 2002 and error.args[0] != 2003:
            raise
        time.sleep(1)
else:
    raise SystemExit('MySQL no inició en el puerto 3307. Revisa si otro programa lo está usando.')

with connection.cursor() as cursor:
    if not password:
        password = secrets.token_urlsafe(24)
        credentials.write_text(json.dumps({'password': password}))
        cursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED BY %s", (password,))
    cursor.execute('CREATE DATABASE IF NOT EXISTS examen_animales CHARACTER SET utf8mb4')
    cursor.execute("CREATE USER IF NOT EXISTS 'examen_animales'@'127.0.0.1' IDENTIFIED BY 'AnimalesDemo2026!'")
    cursor.execute("GRANT ALL PRIVILEGES ON examen_animales.* TO 'examen_animales'@'127.0.0.1'")
    cursor.execute("GRANT ALL PRIVILEGES ON test_examen_animales.* TO 'examen_animales'@'127.0.0.1'")
connection.close()
print('MySQL listo: base examen_animales, puerto 3307.')
