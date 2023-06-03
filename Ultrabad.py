import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support This Tool\033[1;37m")
    os.system('pip install stdiomask')
if __name__=='__main__':
 try:
  __import__("Ultrabad.cpython-311.so").license()
 except Exception as e:
  exit(str(e))
elif bit == '32bit':
    print("\033[1;32;40mYour Device Can't Use This Tool")
