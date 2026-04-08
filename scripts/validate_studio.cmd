@echo off
setlocal
powershell.exe -ExecutionPolicy Bypass -File "%~dp0validate_studio.ps1"
exit /b %ERRORLEVEL%
