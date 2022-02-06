#Shell reconer
import os 
import time
# -*- coding: UTF-8 -*-

device = "none"
device = input("enter the target IP > ")
Sys = input("What is your system ? [L|W] >>> ")
if device == "":
    device = input("enter the target IP > ")

else:
    print(device)
def loopback():
    command = input("Reconer("+device+")> ")
    if command == "help":
        print(''' 
        help menu 
        ====================
        Base commands :
        help : displays this help menu 
        inst-deps : install depndencies 
        C-Target : change target IP
        ====================
        ////NOUVEAU////
        Web Server :
        new-server : create a new webserver[###.###.#.##:PORT] [ip:port]
        swipe-file : sent a file to the server 
        ex [> swipe-file   ]
           [> C:\\Users\\USR\\Descktop\\Brute-force.cat]
        ==================== 
        Scan commands :
        nmap-dvs : (-O) search for the remote system
        nmap-full : (all) Full nmap scan 
        nmap-full-H : (all -Pn) full nmap scan without host discorvery
        nmap-dvs-H : search for the remote scan without host discovery (-Pn)
        ====================
        Exporting commands :
        Xport-nmap-dvs : export the nmap scan (.txt file)
        ''')
        loopback()
    elif command == "SEToolkit"+" start":
        print("starting set toolkit [social engeenering]")
    elif command == "SEToolkit"+" steps":
        print('''
        1) [social enngenering attaks]
        2) [click on 2 and hit enter]
        3) [click on 3 and hit enter]
        4) follow the steps ;)
        +.0
        
        ''')
    elif command == "new-server":
        print("wait please....")
                #!/usr/bin/python
        # -*- coding: UTF-8 -*-
        ## Python 3 :
        import http.server
        import socketserver
        ip = "..." #mets ton ip !
        PORT = 7777
        
        #        Serveur http de base delivrant le contenu du repertoire courant via le port indique.

        # Python 3 :
        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("192.168.1.41",8888), Handler) # mets ton ip a la place du 192.168.1.41 ! sinon sa marche pas :(
        print("à l'écoute sur le port : 8888")
        httpd.serve_forever()
    elif command == "C-Target":
        print("Type your target IP.")
        temp = input("IP [###.###.#.##]>")
        
        
        
        loopback()
    elif command == "start-John":
        print("starting john....")
        opt = input("Create log ? [Y/n]> ")
        if opt == "Y":
            os.system("sudo python3 ~/Reconer-Frmwrk/John.py")
        else:
            os.system("")
    elif command == "inst-dep":
        import os 
        os.system("sudo apt-install openvas")
        os.system("sudo apt install gvm")
        os.system("sudo apt install nmap")
        os.system("gvm-check-setup")    
        loopback()
    elif command == "exit":
        print("quitting ["+device+"]")
        import time
        time.sleep(1)
        print("cleaning cach ...")
        time.sleep(2)
        quit()
    elif command == "Xport-nmap-dvs":
        filesrt = input(".txt file destination >>> ")
        print("the txt file will saved on '"+ filesrt +"'")
        os.system("sudo nmap -O "+device+" "+filesrt)
        loopback()
    elif command == "update":
        print("Updating pleas wait :")
        print("getting updates ...[github.com/h-tech-dev36/ReconerShell] ")
        os.system("git clone https://github.com/H-Tech-Dev36/Reconer-Shell.git")
        loopback()
    elif command == "cont-pge":
        print('''Contributors :
        Concept :
        CanardCoinCoin [ @Canrdcoincoin#7086 ]
        H-Tech-Dev36 [ @Le Théoricien#5962]
        Logo :
        CanardCoinCoin le Bg
        Code :
        H-Tech-Dev36 [ @Le Théoricien#++++ ]        
        Tradution [FR|EN]
        Canardcoincoin
        ...............
        ''')
    else:
        print("'"+command+"' is not a command ! type 'help' to view commands.")
        loopback()
    
loopback()


# @DiscordName#DTAG
