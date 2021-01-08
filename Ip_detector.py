import os
import time
import requests
import subprocess
from cfonts import render
from colorama import Fore
from cfonts.core import say
from colorama.initialise import init

init()

os.system("cls")
time.sleep(1.8)
header = render('Ip Detector', colors=['red', 'green'], align='center')
print(header)
time.sleep(1)
print(f"{Fore.GREEN}[+]{Fore.WHITE} What Do You Want To Do ? \n")
time.sleep(1)
print(f"{Fore.GREEN}[0]{Fore.RED} Show Your Ip Information\n\r")
time.sleep(1.5)
user_input = input(f"{Fore.GREEN}[++]{Fore.WHITE} Choose a Number & Press Enter =>{Fore.LIGHTRED_EX} ")

try:
    if user_input == "0":
        ip = requests.get("https://api.myip.com").text
        ip_encoded = requests.get("https://api.myip.com").encoding
        ip_response = requests.get("https://api.myip.com")

        print(f"{Fore.RED} \n\rGetting Your Ip Information ...\n")
        time.sleep(3)
        print(f"{Fore.GREEN} Server Response :{Fore.WHITE}{ip_response}\n")
        time.sleep(0.8)
        print(f"{Fore.GREEN} Encode Type : {Fore.WHITE}{ip_encoded}\n")
        time.sleep(0.8)
        print(f"{Fore.GREEN} Your Ip Is : {Fore.WHITE}{ip}\n\r\n\r")
        time.sleep(1.5)
        
        extra_input = input(f"{Fore.GREEN}[+]{Fore.WHITE} There is More information in Your System...Would You Like to See Them ?{Fore.CYAN} (if yes type Y else N) =>{Fore.GREEN}")
        if extra_input == "Y":
            shell_command = subprocess.check_output("ifconfig" , shell = True).decode()
            time.sleep(1.5)
            print(f"{Fore.GREEN}{shell_command}")

        elif extra_input == "N":
            print(f"\n{Fore.LIGHTBLUE_EX} Have A Nice Day :)")

    else:
        print(f"{Fore.RED}Enter The Numbers That Available in The App")

except Exception as error:
    print(f"{Fore.RED}Error!" + str(error))

finally:
    pass
