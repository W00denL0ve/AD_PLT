@echo off
cd /d %~dp0

REM 设置你的 GitHub 仓库地址
set REPO=https://github.com/W00denL0ve/AD_PLT

REM 添加所有更改
git add .

REM 提交更改，提交信息为当前日期时间
git commit -m "自动提交 %date% %time%"

REM 设置远程仓库（如已设置可忽略此行）
git remote add origin %REPO% 2>nul

REM 拉取远程最新代码，避免冲突
git pull origin main

REM 推送到远程仓库
git push origin main

pause