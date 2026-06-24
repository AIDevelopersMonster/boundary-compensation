@echo off
REM BC-Origin Windows run helper without PowerShell execution policy issues.
REM Run from repository root:
REM   bc_origin\lab\run_windows.bat

cd /d "%~dp0\..\.."

echo BC-Origin: starting Windows execution pipeline

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    py -3 --version >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        set PYTHON_CMD=py -3
        goto found_python
    )
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python --version >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        set PYTHON_CMD=python
        goto found_python
    )
)

echo No Python 3 interpreter found.
echo Install Python from https://www.python.org/downloads/windows/ and enable Add python.exe to PATH.
exit /b 1

:found_python
echo Using Python: %PYTHON_CMD%

echo Installing dependencies...
%PYTHON_CMD% -m pip install -r bc_origin\lab\requirements.txt
if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

echo Running visual generator...
%PYTHON_CMD% bc_origin\lab\python\generate_visuals.py --out bc_origin\lab\outputs
if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

echo Done. Outputs:
dir bc_origin\lab\outputs
