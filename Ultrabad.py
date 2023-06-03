import os
import platform
import webbrowser
os.system('termux-setup-storage')

os.system('git pull')
try:os.system('mkdir Music')
except:pass
try:os.system('touch ua.txt')
except:pass
P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(P))
	exit()

if __name__ == "__main__":
try:
	os.system("git pull")
	if "Nigeria" == fc:
		__import__("Ultrabad").license()
	else:
		__import__("Ultrabad").Main_()