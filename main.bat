cd %~dp0 
cd src
rem main.exe �؂蔲�����ԁ@���̒����@fps�@�ł�
SET PATH=%PATH%;%~dp0src\ffmpeg\bin
for %%i in (%*) do main.exe 5 720 30 %%i
pause

