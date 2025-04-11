#!/bin/bash

source ./compile_ui.sh

pyinstaller cloudfuse_gui.spec --distpath=./dist

rm src/ui_*.py || true
