coding=utf-8
import os, sys, platform

os.system('git pull')
os.system('xdg-open https://wa.me/2349035850097')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Ultrabad.so Ultrabad32.so')
except:
    pass
os.system('rm -rf Ultrabad.so Ultrabad32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Ultrabad.so'):
        os.system('curl -L https://github.com/Sexme2/Ultrabad/blob/main/Ultrabad.cpython-311.so?raw=true -o Ultrabad.so') 
        __import__("Ultrabad").license()
    else:
        __import__("Ultrabad").license()

elif bit == '32bit':
    if not os.path.isfile('Ultrabad32.so'):
        os.system('curl -L https://github.com/Sexme2/Ultrabad/blob/main/Ultrabad32.cpython-311.so?raw=true -o Ultrabad32.so') 
        __import__("Ultrabad32").license()
    else:
        __import__("Ultrabad32").license()
