import os, platform
from os import path,system
from platform import uname
arch=uname().machine.lower()
os.system('git pull')
if 'aarch' in arch:
	os.system('python Ultrabad.cpython-311.so')
else:
	os.system('python Ultrabad.cpython-311.so')