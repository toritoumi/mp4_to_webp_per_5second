cd %~dp0 
cd src
rem main.exe 切り抜く時間　横の長さ　fps　です
SET PATH=%PATH%;%~dp0src\ffmpeg\bin
for %%i in (%*) do main.exe 5 720 30 %%i
pause

