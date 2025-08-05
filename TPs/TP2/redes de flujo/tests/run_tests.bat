@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

set TRASLADO=python ../traslado.py
set CASES_DIR=cases
set PASSED=0
set FAILED=0

echo Ejecutando pruebas de traslado...

for /D %%C in (%CASES_DIR%\case-*) do (
    set "CASE_PATH=%%C"
    echo -----------------------------------------
    echo Probando !CASE_PATH!

    set N=
    set S=
    for /F "tokens=1,2" %%a in (!CASE_PATH!\config.txt) do (
        set N=%%a
        set S=%%b
    )

    if not defined N (
        echo ❌ Error: config.txt mal formado
        set /a FAILED+=1
        goto :continue
    )

    %TRASLADO% !N! !S! !CASE_PATH!\ciudades.txt !CASE_PATH!\espias.txt > output.txt 2> nul

    fc /b output.txt !CASE_PATH!\esperado.txt > nul
    if !ERRORLEVEL! EQU 0 (
        echo ✅ Test !CASE_PATH! pasó
        set /a PASSED+=1
    ) else (
        echo ❌ Test !CASE_PATH! falló
        echo Esperado:
        type !CASE_PATH!\esperado.txt
        echo Obtenido:
        type output.txt
        set /a FAILED+=1
    )

    :continue
    echo.
)

del /f /q output.txt > nul 2>&1

echo =====================================
echo ✔ Pasaron: %PASSED%
echo ✘ Fallaron: %FAILED%

if %FAILED% GTR 0 (
    exit /b 1
) else (
    echo 🎉 Todos los tests pasaron
    exit /b 0
)
