#Shell reconer
device = "none"
device = input("enter the target IP >")
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
        os.system("sudo nmap -O "+device+"   "+filesrt)
    elif command == "update":
        print("Updating pleas wait :")
        print("getting updates ...[github.com/h-tech-dev36/ReconerShell] ")

    else:
        print("'"+command+"' is not a command ! type 'help' to view commands.")
        loopback()

loopback()