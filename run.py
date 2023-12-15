G='./run32'
F='rm requirements.txt'
E='pip install -r requirements.txt'
D='./run64'
C='requirements.txt'
import os as A,sys,platform as H
try:import requests
except ImportError:A.system('pip install requests')
A.system('git pull')
B=H.architecture()[0]
if B=='64bit':
	if not A.path.isfile(C):A.system(D)
	else:A.system(E);A.system(F);A.system('chmod +x run64');A.system(D)
elif B=='32bit':
	if not A.path.isfile(C):A.system(G)
	else:A.system(E);A.system(F);A.system('chmod +x run32');A.system(G)
