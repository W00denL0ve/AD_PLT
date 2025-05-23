@echo off
chcp 65001 >nul
echo 正在从GitHub获取项目内容...

REM 检查是否提供了命令行参数作为仓库URL
if "%1"=="" (
    set /p REPO_URL="请输入GitHub仓库URL (例如 https://github.com/username/repo.git): "
) else (
    set REPO_URL=%1
)

REM 检查是否已经初始化git仓库
if not exist .git (
    echo 本地仓库不存在，准备创建...
    
    REM 检查当前目录是否为空
    dir /b /a | findstr "^" > nul
    if errorlevel 1 (
        REM 目录为空，执行克隆操作
        echo 目录为空，正在克隆远程仓库...
        git clone %REPO_URL% .
    ) else (
        REM 目录不为空，执行初始化和关联操作
        echo 目录不为空，执行初始化和关联操作...
        
        REM 初始化本地仓库
        echo 初始化本地Git仓库...
        git init
        
        REM 检查远程仓库是否已关联
        git remote -v | findstr "origin" > nul
        if errorlevel 1 (
            echo 添加远程仓库关联...
            git remote add origin %REPO_URL%
        )
        
        REM 配置默认分支为main
        git branch -M main
        
        REM 添加现有文件
        echo 添加现有文件到暂存区...
        git add .
        
        REM 创建初始提交
        echo 创建初始提交...
        git commit -m "feat: 初始化广告平台项目"
        
        REM 尝试拉取远程仓库（允许不相关历史）
        echo 拉取远程仓库内容...
        git pull origin main --allow-unrelated-histories || (
            echo 拉取失败，尝试强制推送本地内容...
            git push -f origin main
        )
    )
) else (
    echo 本地仓库已存在，检查远程仓库配置...
    
    REM 检查远程仓库是否已配置
    git remote -v | findstr "origin" > nul
    if errorlevel 1 (
        echo 添加远程仓库关联...
        git remote add origin %REPO_URL%
    )
    
    REM 获取所有远程分支
    echo 获取远程分支信息...
    git fetch --all
    
    REM 显示当前分支
    echo 当前分支:
    git branch
    
    REM 获取当前分支名
    for /f "tokens=* delims=" %%i in ('git rev-parse --abbrev-ref HEAD') do set current_branch=%%i
    
    REM 拉取更新
    echo 正在从远程仓库拉取更新...
    git pull origin %current_branch%
    
    REM 显示仓库状态
    echo 当前仓库状态:
    git status
)

echo 完成！
pause