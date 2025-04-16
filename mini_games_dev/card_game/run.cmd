@echo off
setlocal
title game cart 1
chcp 1251 > nul
cls
python src %*
pause
endlocal
exit /b 0
