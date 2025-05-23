@echo off
chcp 65001 >nul
echo 正在上传项目到GitHub...

REM 检查git是否安装
git --version > nul 2>&1
if errorlevel 1 (
    echo 错误：未检测到Git，请先安装Git
    pause
    exit /b 1
)

REM 检查是否已经初始化git仓库
if not exist .git (
    echo 初始化Git仓库...
    git init
    if errorlevel 1 (
        echo 错误：Git初始化失败
        pause
        exit /b 1
    )
)

REM 检查并配置Git用户信息
git config user.name > nul 2>&1
if errorlevel 1 (
    echo 配置Git用户信息...
    set /p GIT_NAME="请输入Git用户名: "
    set /p GIT_EMAIL="请输入Git邮箱: "
    git config --global user.name "%GIT_NAME%"
    git config --global user.email "%GIT_EMAIL%"
)

REM 检查远程仓库配置
git remote -v | findstr "origin" > nul
if errorlevel 1 (
    echo 配置远程仓库...
    set /p REPO_URL="请输入GitHub仓库URL (例如 https://github.com/username/repo.git): "
    git remote add origin %REPO_URL%
) else (
    echo 检测到远程仓库配置，是否需要更新？(Y/N)
    set /p UPDATE_REMOTE="输入Y更新，输入N保持现有配置: "
    if /i "%UPDATE_REMOTE%"=="Y" (
        git remote remove origin
        set /p REPO_URL="请输入新的GitHub仓库URL: "
        git remote add origin %REPO_URL%
    )
)

REM 清理工作区
echo 清理工作区...
git clean -n
set /p CLEAN_CONFIRM="是否删除以上未跟踪的文件？(Y/N): "
if /i "%CLEAN_CONFIRM%"=="Y" (
    git clean -f
)

REM 从远程仓库抓取更新
echo 正在从远程仓库获取更新...
git fetch origin
if errorlevel 1 (
    echo 错误：无法从远程仓库获取更新
    pause
    exit /b 1
)

REM 检查当前分支
for /f "tokens=* delims=" %%i in ('git rev-parse --abbrev-ref HEAD') do set current_branch=%%i
echo 当前分支：%current_branch%

REM 尝试与远程分支同步
git branch -r | findstr "origin/main" > nul
if errorlevel 1 (
    echo 远程仓库无main分支，将创建新分支...
) else (
    echo 正在同步远程更新...
    git pull origin main --allow-unrelated-histories
    if errorlevel 1 (
        echo 警告：无法自动合并更新，请手动解决冲突
        pause
        exit /b 1
    )
)

REM 添加文件到暂存区
echo 准备添加更改的文件...
git status
set /p ADD_CONFIRM="是否添加以上更改？(Y/N): "
if /i "%ADD_CONFIRM%"=="Y" (
    git add .
) else (
    echo 操作已取消
    pause
    exit /b 0
)

REM 显示提交信息格式指南
echo.
echo 提交信息格式指南:
echo 1. 类型: feat(新功能), fix(修复), docs(文档), style(格式), refactor(重构), perf(性能), test(测试), chore(构建)
echo 2. 影响范围: (auth), (ad), (user), (payment) 等
echo 3. 简要描述: 一句话说明改动内容
echo.
echo 示例: feat(ad): 添加广告预算控制功能
echo       fix(auth): 修复登录验证失败问题
echo.

REM 提交更改
set /p COMMIT_MSG="请按格式输入提交信息: "
if "%COMMIT_MSG%"=="" (
    echo 错误：提交信息不能为空
    pause
    exit /b 1
)
echo 提交更改...
git commit -m "%COMMIT_MSG%"
if errorlevel 1 (
    echo 错误：提交失败
    pause
    exit /b 1
)

REM 推送到GitHub
echo 准备推送到GitHub...
echo 当前更改将推送到远程仓库，请确认
git show --name-status HEAD
set /p PUSH_CONFIRM="确认推送这些更改？(Y/N): "
if /i "%PUSH_CONFIRM%"=="Y" (
    echo 推送中...
    git push -u origin main
    if errorlevel 1 (
        echo 错误：推送失败，请检查网络连接和仓库权限
        pause
        exit /b 1
    )
) else (
    echo 推送已取消
    pause
    exit /b 0
)

echo =====================================
echo 操作完成！
echo 更新已成功推送到GitHub仓库
echo =====================================
pause