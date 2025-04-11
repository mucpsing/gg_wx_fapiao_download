@REM @Author: CPS
@REM @email: 373704015@qq.com
@REM @Date: 2025-04-11 19:51:42.688386
@REM Last Modified by: CPS
@REM Last Modified time: 2025-04-11 19:51:42.688386
@REM Modified time: 2025-04-11 19:51:42.688386
@REM @file_path "D:\CPS\MyProject\Projects_Personal\GG_wx_fapiao_download"
@REM @Filename "build_scripts.bat"

@echo off && setlocal enabledelayedexpansion
@chcp 65001

npx terser "src/scripts/download_pdf_and_click.js" --output "src/scripts/dist.js" --compress --mangle --comments false
