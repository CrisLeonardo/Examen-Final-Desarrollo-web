$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)

if (-not (Test-Path './.venv/Scripts/python.exe')) {
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw 'Se necesita Python 3.14 instalado.' }
}
& './.venv/Scripts/python.exe' -m pip install -r requirements.txt --disable-pip-version-check
if ($LASTEXITCODE -ne 0) { throw 'No se pudieron instalar las dependencias.' }

$local = Join-Path $env:LOCALAPPDATA 'ExamenAnimales'
$mysql = Join-Path $local 'mysql-8.4.13-winx64'
$data = Join-Path $local 'data'
New-Item -ItemType Directory -Force $local | Out-Null
if (-not (Test-Path "$mysql/bin/mysqld.exe")) {
    Write-Host 'Descargando MySQL (solo la primera vez)...'
    curl.exe -L --fail 'https://cdn.mysql.com/Downloads/MySQL-8.4/mysql-8.4.13-winx64.zip' -o "$local/mysql.zip"
    if ($LASTEXITCODE -ne 0) { throw 'No se pudo descargar MySQL.' }
    Expand-Archive -LiteralPath "$local/mysql.zip" -DestinationPath $local -Force
}
if (-not (Test-Path "$data/mysql")) {
    & "$mysql/bin/mysqld.exe" --no-defaults "--basedir=$mysql" "--datadir=$data" --initialize-insecure
    if ($LASTEXITCODE -ne 0) { throw 'No se pudo inicializar MySQL.' }
}

$listener = Get-NetTCPConnection -State Listen -LocalPort 3307 -ErrorAction SilentlyContinue
if (-not $listener) {
    Start-Process -FilePath "$mysql/bin/mysqld.exe" -ArgumentList @('--no-defaults', "--basedir=`"$mysql`"", "--datadir=`"$data`"", '--port=3307', '--bind-address=127.0.0.1', '--mysqlx=0') -WindowStyle Hidden
}
& './.venv/Scripts/python.exe' herramientas/preparar_db.py
if ($LASTEXITCODE -ne 0) { throw 'No se pudo preparar la base de datos.' }
& './.venv/Scripts/python.exe' manage.py migrate --noinput
if ($LASTEXITCODE -ne 0) { throw 'No se pudieron crear las tablas.' }
