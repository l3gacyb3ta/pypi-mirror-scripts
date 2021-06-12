import os
for line in open('toinstall.txt', 'r').readlines():
    os.system("pypi-mirror download -d /media/l3gacy/DATA/pypi/packages " + line)