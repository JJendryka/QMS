python3 -m venv .venv > /dev/null 2>&1
.venv/bin/python3 -m pip install .

echo '#!/usr/bin/env bash' > qms-backend.sh
echo "$(pwd)/.venv/bin/python3 $(pwd)/src/main.py \"\$@\"">> qms-backend.sh
chmod +x qms-backend.sh

mkdir --parents "$HOME/.local/bin/"
ln -sf "$(pwd)/qms-backend.sh" "$HOME/.local/bin/qms-backend"