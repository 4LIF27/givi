C='./run32'
import os as A,sys,platform as D
try:import requests
except:A.system('pip install requests')
import requests
try:
	if sys.argv[1]=='up':A.system('git pull');A.system('rm -rf run')
except:pass
B=D.architecture()[0]
if B=='64bit':exit(' maaf untuk sc ini belum support 64 bit ')
elif B=='32bit':
	if not A.path.isfile('requirements.txt'):A.system('pip install -r requirements.txt');A.system('chmod +x run32');A.system(C)
	else:A.system(C)
