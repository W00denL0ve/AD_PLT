@echo off
chcp 65001 >nul
echo 正在初始化Git仓库...

REM 检查git是否安装
git --version > nul 2>&1
if errorlevel 1 (
    echo 错误：未检测到Git，请先安装Git
    pause
    exit /b 1
)

:: 初始化git仓库
echo 初始化Git仓库...
git init

REM 配置默认分支为main
git branch -M main

:: 创建.gitignore文件
echo 创建.gitignore文件...
(
echo # Python
echo __pycache__/
echo *.py[cod]
echo *$py.class
echo *.so
echo .Python
echo build/
echo develop-eggs/
echo dist/
echo downloads/
echo eggs/
echo .eggs/
echo lib/
echo lib64/
echo parts/
echo sdist/
echo var/
echo wheels/
echo *.egg-info/
echo .installed.cfg
echo *.egg
echo .env
echo .venv
echo env/
echo venv/
echo ENV/
echo .idea/
echo .vscode/
echo *.log
) > .gitignore

:: 添加所有文件到暂存区
echo 添加文件到Git...
git status
set /p ADD_CONFIRM="是否添加以上更改？(Y/N): "
if /i "%ADD_CONFIRM%"=="Y" (
    git add .
) else (
    echo 操作已取消
    pause
    exit /b 0
)

:: 检查git用户配置
git config user.name > nul 2>&1
if errorlevel 1 (
    echo 配置Git用户信息...
    set /p GIT_NAME="请输入Git用户名: "
    set /p GIT_EMAIL="请输入Git邮箱: "
    git config --global user.name "%GIT_NAME%"
    git config --global user.email "%GIT_EMAIL%"
)

:: 进行首次提交
echo 进行首次提交...
git commit -m "初始化提交：广告平台项目基础架构"
if errorlevel 1 (
    echo 错误：提交失败，请检查Git配置
    pause
    exit /b 1
)

:: 添加远程仓库
echo 请输入远程仓库地址（例如：https://github.com/username/repository.git）：
set /p REPO_URL=
git remote add origin %REPO_URL%
if errorlevel 1 (
    echo 错误：添加远程仓库失败
    pause
    exit /b 1
)

:: 推送到远程仓库
echo 推送到远程仓库...
echo 确保GitHub仓库已创建且为空
set /p PUSH_CONFIRM="是否继续推送？(Y/N): "
if /i "%PUSH_CONFIRM%"=="Y" (
    git push -u origin main
    if errorlevel 1 (
        echo.
        echo 错误：推送失败
        echo 可能的原因：
        echo 1. GitHub仓库未创建
        echo 2. 仓库URL不正确
        echo 3. 没有推送权限
        echo 4. 远程仓库不为空
        echo.
        echo 建议操作：
        echo 1. 检查仓库URL是否正确
        echo 2. 确认已在GitHub创建仓库
        echo 3. 检查是否已配置GitHub身份验证
        pause
        exit /b 1
    )
) else (
    echo 推送已取消
    pause
    exit /b 0
)

echo =====================================
echo 初始化完成！
echo 仓库已成功推送到GitHub
echo =====================================
pause
