cd %~dp0 
cd src
rem main.exe Ø‚è”²‚­ŠÔ@‰¡‚Ì’·‚³@fps@‚Å‚·
SET PATH=%PATH%;%~dp0src\ffmpeg\bin
for %%i in (%*) do main.exe 5 720 30 %%i
pause

