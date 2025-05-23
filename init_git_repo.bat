@echo off
chcp 65001 >nul
echo 正在初始化Git仓库...

:: 初始化git仓库
git init

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
git add .

:: 进行首次提交
echo 进行首次提交...
git commit -m "初始化提交：广告平台项目基础架构"

:: 添加远程仓库（需要手动替换）
echo 请输入远程仓库地址（例如：https://github.com/username/repository.git）：
set /p REPO_URL=
git remote add origin %REPO_URL%

:: 推送到远程仓库
echo 推送到远程仓库...
git push -u origin master

echo 完成！
pause
