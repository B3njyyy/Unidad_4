@echo off
echo Generando ejecutable con PyInstaller
pyinstaller --onefile actividad.py
echo Ejecutable generado en dist\sha256-tool.exe
pause