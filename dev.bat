@echo off
setlocal
setlocal enabledelayedexpansion

:: ------------------- execute script -------------------
@rem build locale converter image
docker build -t py-jieba .

@rem create cache
IF NOT EXIST cache (
    mkdir cache
)

@rem execute converter
docker run -ti --rm ^
    -v %cd%\cache:/data ^
    -v %cd%\src:/app ^
    py-jieba bash
