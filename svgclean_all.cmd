@echo off
rem https://github.com/RazrFalcon/svgcleaner
cd Onigiri\icons
for %%f in (*.svg) do svgcleaner "%%f" "%%f"
pause
