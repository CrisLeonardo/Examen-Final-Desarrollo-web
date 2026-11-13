$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
function Abrir-Postman {
    $postman = Join-Path $env:LOCALAPPDATA 'Postman/Postman.exe'
    if (Test-Path $postman) {
        Start-Process -FilePath $postman
    } else {
        Write-Host 'Abre Postman para probar http://127.0.0.1:8000/api/animales/'
    }
}
try {
    $active = Get-NetTCPConnection -State Listen -LocalPort 8000 -ErrorAction SilentlyContinue
    if ($active) {
        try {
            $api = Invoke-RestMethod 'http://127.0.0.1:8000/api/animales/' -Headers @{Accept='application/json'} -TimeoutSec 5
            Write-Host 'La API ya está iniciada. Se abrirá Postman.'
            Abrir-Postman
            exit 0
        } catch {
            throw 'El puerto 8000 está ocupado por otro programa. Ciérralo y vuelve a iniciar.'
        }
    }
    & "$PSScriptRoot/preparar.ps1"
    if ($LASTEXITCODE -ne 0) { throw 'No se pudo preparar el proyecto.' }
    Abrir-Postman
    Write-Host 'Deja esta ventana abierta. Para detener la API, presiona Ctrl+C.'
    & './.venv/Scripts/python.exe' manage.py runserver 127.0.0.1:8000 --noreload
} catch {
    Write-Host $_ -ForegroundColor Red
    exit 1
}
