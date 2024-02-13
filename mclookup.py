import requests
import sys
import os
import time
from mcstatus import *
import subprocess
from subprocess import *
import colorama
from colorama import Fore, Style
from art import *
from termcolor import colored
colorama.init(autoreset=True)

def main():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(text2art("McLookup"), 'red'))
        print(" " * 20 + 'Developed by ' + Fore.CYAN + Style.NORMAL + 'w/zKaiioZ')
        print("\n")
        mc = input(" " * 10 + '[~] Enter a MC Server IP: ')
        api2 = f"http://ip-api.com/json/{mc}"
        response_ip = requests.get(api2)
        response_ip.raise_for_status()  

        data_ip = response_ip.json()
        isp = data_ip.get('isp', 'N/A')
        country = data_ip.get('country', 'N/A')
        city = data_ip.get('city', 'N/A')

        api = f"https://api.mcstatus.io/v2/status/java/{mc}"
        response_mc = requests.get(api)
        response_mc.raise_for_status()  

        data_mc = response_mc.json()
        server_status = "Online" if data_mc['online'] else "Offline"
        players_online = data_mc['players']['online']
        players_max = data_mc['players']['max']
        players_info = f"{players_online}/{players_max}"
        server_description = " ".join(data_mc['motd']['clean'].strip().splitlines())  
        server_version_raw = data_mc.get('version', {}).get('name_raw', 'N/A')
        print("\n\n")
        print(" " * 5 + Fore.LIGHTBLACK_EX + "[/] Basic Information: ")
        print("\n")
        print(Fore.YELLOW + "[$] Server     : ", data_mc['host'])
        print(Fore.YELLOW + "[$] Status     : ", server_status)
        print(Fore.YELLOW + "[$] Online     : ", players_info)
        print(Fore.YELLOW + "[$] Description: ", server_description)  
        print(Fore.YELLOW + "[$] IP         : ", data_mc['ip_address'])
        print(Fore.YELLOW + "[$] Port       : ", data_mc['port'])
        print(Fore.YELLOW + "[$] Version    : ", server_version_raw)
        print("\n\n")
        time.sleep(3)
        print(" " * 5 + Fore.LIGHTBLACK_EX + "[/] Host Information: ")
        print("\n")
        print(Fore.YELLOW + "[$] ISP          : ", isp)
        print(Fore.YELLOW + "[$] Host Country : ", country)
        print(Fore.YELLOW + "[$] Host City    : ", city)
        print("\n\n")
        time.sleep(3)
        print(" " * 5 + Fore.LIGHTBLACK_EX + "[/] Other information: ")
        print("\n")
        print(Fore.YELLOW + "[$] Protocol    : ", data_mc['version']['protocol'])
        print(Fore.YELLOW + "[$] EULA Blocked: ", data_mc['eula_blocked'])
        print(Fore.YELLOW + "[$] Retrieved At: ", data_mc['retrieved_at'])
        print(Fore.YELLOW + "[$] Expires At  : ", data_mc['expires_at'])
        print(Fore.YELLOW + "[$] SRV Record  : ", data_mc['srv_record'])
        print("\n\n")
        print("Back to menu in 4 seconds...")
        time.sleep(4)
        main()  
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error: {e}")
    except KeyError as e:
        print(Fore.RED + f"Error: Missing data key: {e}")
    except KeyboardInterrupt:
        print("\n\n[!] Exiting... Goodbye !")
        time.sleep(2)
        sys.exit(0)

if __name__ == "__main__":
    main()
