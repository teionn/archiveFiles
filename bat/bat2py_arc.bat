echo off
set batPath=%~dp0\..
@rem cd /d C:\Python26\

set getPath=%*
python "%batPath%\lib\rate_archiveFiles_BAT.py" "%getPath: =~%;_archive;_v"

TIMEOUT /T 2

