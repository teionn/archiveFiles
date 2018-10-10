echo off
SET toolPath=%~dp0\..
REM cd /d C:\Python26\

REM if not "%toolPath:\Program Files (x86)\=%" == "%toolPath%" SET batPath=%toolPath:Program Files (x86)=PROGRA~2%
REM else if not "%toolPath:\Program Files\=%" == "%toolPath%" SET batPath=%toolPath:Program Files=PROGRA~1%
SET batPath=%toolPath%

for %%f in (%*) do (
  python %batPath%\lib\rate_archiveFiles_BAT.py %%f;incrementalSave;.
)
TIMEOUT /T 2