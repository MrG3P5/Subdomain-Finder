#!/usr/bin/env python3
import requests
import os
import sys
import re
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init

# Color
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE
cyan = Fore.LIGHTCYAN_EX
blue = Fore.LIGHTBLUE_EX
yellow = Fore.LIGHTYELLOW_EX

init(autoreset=True)
s = requests.Session()
try:
    open("Result.txt", "a")
except:
    pass

def banner():
    os.system("clear||cls")
    __banner__ = f"""{red}
    ⣴⣶⣤⡤⠦⣤⣀⣤⠆     ⣈⣭⣭⣿⣶⣿⣦⣼⣆        
	⠉⠻⢿⣿⠿⣿⣿⣶⣦⠤ ⡠⢾⣿⣿⡿⠋⠉⠉⠻⣿⣿⡛⣦      
          ⠈   ⠈⢿⣿⣟⠦⣾⣿⣿⣷     ⠻⠿⢿⣿⣧⣄    
	   ⣸⣿⣿⢧ ⢻⠻⣿⣿⣷⣄⣀ ⠢⣀⡀    ⠈⠙⠿    
   ⢀      ⢠⣿⣿⣿⠈  ⠡⠌⣻⣿⣿⣿⣿⣿⣿⣿⣛⣳⣤⣀⣀  
   ⢠⣧⣶⣥⡤⢄ ⣸⣿⣿⠘  ⢀⣴⣿⣿⡿⠛⣿⣿⣧⠈⢿⠿⠟⠛⠻⠿    {cyan}---[ {white}MASS Subdomain - Finder {cyan}]---
{red}  ⣰⣿⣿⠛⠻⣿⣿⡦⢹⣿⣷   ⢊⣿⣿⡏  ⢸⣿⣿⡇ ⢀⣠⣄⣾           {cyan}[ {white}Created By X-MrG3P5 {cyan}]
{red} ⣠⣿⠿⠛ ⢀⣿⣿⣷⠘⢿⣿⣦⡀ ⢸⢿⣿⣿⣄ ⣸⣿⣿⡇⣪⣿⡿⠿⣿⣷⡄ 
  ⠙⠃   ⣼⣿⡟⠌ ⠈⠻⣿⣿⣦⣌⡇⠻⣿⣿⣷⣿⣿⣿⠐⣿⣿⡇ ⠛⠻⢷⣄
	⢻⣿⣿⣄   ⠈⠻⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟ ⠫⢿⣿⡆   ⠁
	 ⠻⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣀⣤⣾⡿⠃    """
    print(__banner__ + "\n")

def SubdomainFinder(domain):
    global s
    try:
        domain = domain.strip("\n\r")
        req = s.get(f"https://rapiddns.io/subdomain/{domain}?full=1#result").text
        all_domain = re.findall(r"</th>\n<td>(.*?)</td>", req)
        
        if len(all_domain) != 0:
            sys.stdout.write(f"\n{white}---> {blue}{domain} {white}[ {green}{len(all_domain)} Domain {white}]")
            for x in all_domain:
                x = x.replace("ns1.", "").replace("ns2.", "").replace("www.", "").replace("cpanel.", "").replace("autodiscover.", "").replace("whm.", "").replace("cpcontacts.", "").replace("webdisk.", "").replace("cpcalendars.", "")
                if x in open("Result.txt", "r").read():
                    pass
                else:
                    open("Result.txt", "a").write(x + "\n")
        else:
            sys.stdout.write(f"\n{white}---> {blue}{domain} {white}[ {yellow}BAD! {white}]")
    except:
        sys.stdout.write(f"\n{white}---> {blue}{domain} {white}[ {yellow}BAD! {white}]")

if __name__=="__main__":
    banner()
    list_domain = open(input(f"{cyan}[{yellow}#{cyan}] {white}Domain List : "), "r").readlines()
    Thread = input(f"{cyan}[{yellow}#{cyan}] {white}Thread : ")
    pool = ThreadPool(int(Thread))
    pool.map(SubdomainFinder, list_domain)
    pool.close()
    pool.join()
    sys.stdout.write(f"\n{white}---> DONE!")
