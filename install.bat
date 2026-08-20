@echo off
chcp 65001 >nul
setlocal

echo.
echo  ============================================
echo    Memphis Resume Site - 技能安装
echo  ============================================
echo.

set "TARGET=%USERPROFILE%\.agents\skills\memphis-resume-site"

if exist "%TARGET%" (
    echo  [提示] 检测到已安装，正在覆盖更新...
    rmdir /s /q "%TARGET%"
)

xcopy /E /I /Y "%~dp0memphis-resume-site" "%TARGET%" >nul

echo  [完成] 安装成功！
echo  技能位置: %TARGET%
echo.
echo  使用方法：打开 ZCode，新开一个对话，输入
echo      "把简历做成网站"   并附上你的简历文件
echo.
pause
