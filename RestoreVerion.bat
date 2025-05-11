@echo off
setlocal
set "template_file=%~1"
python RestoreVerion.py "%template_file%"
endlocal
pause