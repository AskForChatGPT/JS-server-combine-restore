@echo off
echo Starting HTTP server...

REM 清除佔用 8080 端口的進程
echo Killing any process using port 8080...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8080"') do (
  if not "%%a"=="0" (
    taskkill /f /pid %%a
  )
)
timeout /t 2 >nul

REM 切換到指定目錄
cd /d "%~dp0"

REM 啟動 HTTP 伺服器
echo Starting http-server...
start http-server -p 8080

REM 等待伺服器啟動
timeout /t 2 >nul

REM 開啟 LibreWolf
echo Opening LibreWolf...
start librewolf "http://localhost:8080/index.html"

echo Done.
pause

