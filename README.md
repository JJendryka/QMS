# QMS - Quadrupole Management Software
This software controls a quadrupole mass spectrometer

## Installation
To install run:
```bash
pip install git+https://github.com/JJendryka/QMS.git
```
To install as a developer run:
```bash
git clone https://github.com/JJendryka/QMS.git
cd ./QMS
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```
After that call:
```bash
qms
```
To be able to run the program from venv create a `qms.sh` script and add it to path:
```bash
#!/usr/bin/env bash
source /path/to/.venv/bin/activate
qms "$@"
deactivate
```
```bash
ln -sf /path/to/qms.sh ~/.local/bin/qms
```