rem @echo off
rem --https://github.com/RazrFalcon/svgcleaner-- no it remove color name "black"
rem use https://github.com/scour-project/scour/
cd Onigiri\icons\dark
rem for %%f in (*.svg) do svgcleaner "%%f" "%%f" --keep-named-ids
ren %%f %%f.svg
for %%f in (*.svg) do scour -i %%f.svg %%f --enable-comment-stripping --shorten-ids --indent=none --disable-simplify-colors --strip-xml-prolog --remove-titles --no-line-breaks
cd ..\light
ren %%f %%f.svg
for %%f in (*.svg) do scour -i %%f.svg %%f --enable-comment-stripping --shorten-ids --indent=none --disable-simplify-colors --strip-xml-prolog --remove-titles --no-line-breaks
pause
