echo "Creating packages from downloads ..."
pypi-mirror create -d packages -m simple
echo "Starting server ..."
echo "Command to run: pip install --trusted-host <ip> -i <ip> <package>"
hostname -I
python3 -m http.server