@echo off
setlocal

REM BC-Origin one-click Windows launcher.
REM Double-click this file from the repository root, or run:
REM   START_BC_ORIGIN_WINDOWS.bat

cd /d "%~dp0"

echo ============================================================
echo BC-Origin Shadow Lab - one-click Windows launcher
echo ============================================================
echo.

set "VENV_DIR=.venv-bc-origin"
set "VENV_PY=%VENV_DIR%\Scripts\python.exe"

if exist "%VENV_PY%" goto use_venv

echo Creating local virtual environment: %VENV_DIR%

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    py -3 -m venv "%VENV_DIR%"
    if %ERRORLEVEL% EQU 0 goto use_venv
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python -m venv "%VENV_DIR%"
    if %ERRORLEVEL% EQU 0 goto use_venv
)

echo.
echo ERROR: Could not create Python virtual environment.
echo Install Python 3 from https://www.python.org/downloads/windows/
echo Enable: Add python.exe to PATH
echo.
pause
exit /b 1

:use_venv
echo Using Python environment: %VENV_PY%
echo.

echo Upgrading pip...
"%VENV_PY%" -m pip install --upgrade pip
if %ERRORLEVEL% NEQ 0 goto fail

echo.
echo Installing BC-Origin lab dependencies...
"%VENV_PY%" -m pip install -r bc_origin\lab\requirements.txt
if %ERRORLEVEL% NEQ 0 goto fail

echo.
echo Generating static visuals...
"%VENV_PY%" bc_origin\lab\python\generate_visuals.py --out bc_origin\lab\outputs
if %ERRORLEVEL% NEQ 0 goto fail

echo.
echo Opening generated outputs and standalone GUI...
if exist "bc_origin\lab\outputs" start "" "%CD%\bc_origin\lab\outputs"
if exist "bc_origin\lab\web\index.html" start "" "%CD%\bc_origin\lab\web\index.html"

echo.
echo DONE.
echo Generated files are in:
echo   bc_origin\lab\outputs
echo Standalone GUI:
echo   bc_origin\lab\web\index.html
echo.
pause
exit /b 0

:fail
echo.
echo ERROR: BC-Origin one-click launcher failed.
echo Check the error message above.
echo.
pause
exit /b 1
