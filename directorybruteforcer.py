from asyncio.windows_events import NULL
from genericpath import exists
import requests
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-w',type=str, required=True,help="Switch for Wordlist")
parser.add_argument('-u',type=str, required=True, help="Switch for URL")
parser.add_argument('--h',type=str, required=False, help="Switch for Headers(y/n)")
args = parser.parse_args()

print("[+] Wordlist: ",args.w)
print("[+] URL: ", args.u)


# Request Headers
headers=NULL
if (args.h=="y"):
	headers ={"User-Agent": "aUserAgent"}
else:
	pass 
	
 
#Working with file
file = open(args.w,'r')
lines = file.readlines()

#Checking if URL schema exists in the url
if ('http' in args.u) or ('https' in args.u):
	pass
else:
	print('Please enter a URL Schema')
	sys.exit()

# Parsing through each word in the wordlist
try:
	for line in lines:
		line = line.strip("\n")
		if(headers!=NULL):
			r = requests.get(args.u+'/'+line,headers=headers)
			(r.status_code != 404)
			print(args.u+'/'+line, ":", r.status_code)
		else:
			r = requests.get(args.u+'/'+line)
			(r.status_code != 404)
			print(args.u+'/'+line, ":", r.status_code)

	
except:
	print("Error Occured")
