@echo off

7z a -r "./Releases/Onigiri-%DATE:~-4%-%DATE:~4,2%-%DATE:~7,2%.7z" Onigiri/*.* -xr!.vscode -xr!__pycache__ -xr!Onigiri.code-workspace
if errorlevel 1 goto erroroccurred

goto noerrors

:erroroccurred

echo ???????????????????
echo    Error compile
echo ???????????????????
pause
goto :EOF
:noerrors

echo #######################
echo    Compile completed
echo #######################
pause
