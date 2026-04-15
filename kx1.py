#!/usr/bin/env python3
from colorama import init, Fore, Style
import argparse
import sys
import os
from modules.subdomain import passive_subdomain_scanner

init(autoreset=True)

def banner():
    print(Fore.RED + Style.BRIGHT + r"""
    ██╗  ██╗██╗  ██╗ ██╗
    ██║ ██╔╝╚██╗██╔╝██╔╝
    █████╔╝  ╚███╔╝██╔╝ 
    ██╔═██╗  ██╔██╗██╔╝  
    ██║  ██╗██╔╝ ██╗███████╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
          KX1 v2.0 - Passive Recon Engine
                  By Moa
    """ + Style.RESET_ALL)

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="KX1 v2.0 - Passive Subdomain Finder")
    parser.add_argument("-d", "--domain", required=True, help="الدومين المستهدف")
    parser.add_argument("-o", "--output", help="اسم ملف الإخراج")
    parser.add_argument("-t", "--threads", type=int, default=20, help="عدد الـ Threads")
    
    args = parser.parse_args()

    print(Fore.CYAN + f"[+] بدء Passive Scan المتقدم على {args.domain}\n")
    
    passive_subdomain_scanner(
        domain=args.domain,
        output_file=args.output,
        threads=args.threads
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] تم إيقاف KX1")
        sys.exit(0)
