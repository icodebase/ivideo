#!/bin/bash

rm -fr ivideo_Win64_pyinstaller.7z build dist

pyinstaller -wy -i "../ivideo/misc/icon.ico" "../ivideo/ivideo.py"

cp -R ./qss ./dist/ivideo

cp -R ./bin/* ./dist/ivideo

cp -R ./languages ./dist/ivideo

cp icon.ico ./dist/ivideo

cp sponsor.jpg ./dist/ivideo

7z a -t7z ivideo_Win64_pyinstaller.7z ./dist/ivideo -mx=9 -ms=200m -mf -mhc -mhcf  -mmt -r
