#!/bin/sh -x

rm ./src/ui_*.py || true

pyside6-uic ./src/mountPrimaryWindow.ui > ./src/ui_mountPrimaryWindow.py
pyside6-uic ./src/s3_config_common.ui > ./src/ui_s3_config_common.py
pyside6-uic ./src/azure_config_common.ui > ./src/ui_azure_config_common.py
pyside6-uic ./src/azure_config_advanced.ui > ./src/ui_azure_config_advanced.py
pyside6-uic ./src/s3_config_advanced.ui > ./src/ui_s3_config_advanced.py
