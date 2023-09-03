@echo off
setlocal
setlocal enabledelayedexpansion

:: ------------------- execute script -------------------
@rem build locale converter image
docker build -t py-ckip .\conf\docker\ckip

@rem create cache
IF NOT EXIST cache (
    mkdir cache
)

@rem execute converter
docker run -ti --rm ^
    -v %cd%\cache\data:/app/data ^
    -v %cd%\src:/app ^
    py-ckip bash
