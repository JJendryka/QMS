#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

for filename in $SCRIPT_DIR/*.ui; do
    pyside6-uic "$filename" -o "${filename::-3}_ui.py"
done