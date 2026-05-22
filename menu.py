import os
import sys
import time

# Colors for terminal (ANSI)
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_banner():
    banner = f"""{GREEN}{BOLD}
    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
    ██╔════╝██║   ██║██╔════╝╚══██╔══╝██╔════╝████╗  ████║
    ███████╗╚██╗ ██╔╝███████╗   ██║   █████╗  ██╔████╔██║
    ╚════██║ ╚████╔╝ ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
    ███████║  ╚██╔╝  ███████║   ██║   ███████╗██║ ╚═╝ ██║
    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
    {CYAN}==============================================================
    [SYSTEM] ADVANCED TARGETING & PAYLOAD DEPLOYMENT FRAMEWORK
    [STATUS] SECURE CONNECTION ESTABLISHED
    =============================================================={RESET}"""
    print(banner)

def run_command(command, description=""):
    print(f"\n{YELLOW}[*] EXECUTING MODULE: {description}{RESET}")
    print(f"{CYAN}[*] COMMAND: python email_campaign/main.py {command}{RESET}\n")
    os.system(f"python email_campaign/main.py {command}")
    input(f"\n{GREEN}[+] OPERATION COMPLETE. Press ENTER to return to main terminal...{RESET}")

def view_file(filepath, title):
    print(f"\n{CYAN}==============================================================")
    print(f"[SYSTEM] ACCESSING RECORD: {title}")
    print(f"=============================================================={RESET}\n")
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"{GREEN}{content}{RESET}")
        else:
            print(f"{RED}[-] ERROR: Record not found at {filepath}.{RESET}")
    except Exception as e:
        print(f"{RED}[-] ERROR READING RECORD: {str(e)}{RESET}")
    input(f"\n{GREEN}[+] END OF RECORD. Press ENTER to return to main terminal...{RESET}")

def main():
    # Enable ANSI colors for Windows
    os.system('') 
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        
        print(f"{BOLD}[ DATA ACQUISITION MODULES ]{RESET}")
        print(f"  {CYAN}[01]{RESET} INITIATE FREE SCRAPING (Job boards)")
        print(f"  {CYAN}[02]{RESET} INITIATE LINKEDIN SCRAPING (Warning: High risk)")
        print(f"  {CYAN}[03]{RESET} ENRICH ACQUIRED TARGETS (Apollo API)")
        print(f"  {CYAN}[04]{RESET} VIEW LATEST ACQUIRED TARGETS (Display scraped emails)")
        
        print(f"\n{BOLD}[ AI PAYLOAD GENERATION MODULES ]{RESET}")
        print(f"  {CYAN}[05]{RESET} MERGE TARGETS & GENERATE AI MESSAGES")
        print(f"  {CYAN}[06]{RESET} VIEW AI GENERATED MESSAGES (Preview configurations)")
        print(f"  {CYAN}[07]{RESET} DISPLAY MASTER TARGET LIST (emails_prospection.md)")
        
        print(f"\n{BOLD}[ DEPLOYMENT & TRACKING MODULES ]{RESET}")
        print(f"  {CYAN}[08]{RESET} TEST PAYLOAD DELIVERY (Send to self)")
        print(f"  {CYAN}[09]{RESET} {RED}EXECUTE MASS DEPLOYMENT (Send Live Emails){RESET}")
        print(f"  {CYAN}[10]{RESET} INITIATE FOLLOW-UP SEQUENCE")
        print(f"  {CYAN}[11]{RESET} MONITOR INBOUND COMMUNICATIONS (Check replies)")
        
        print(f"\n{BOLD}[ SYSTEM ]{RESET}")
        print(f"  {CYAN}[00]{RESET} TERMINATE CONNECTION")
        
        choice = input(f"\n{YELLOW}root@system:~# {RESET}").strip()
        
        if choice == '01' or choice == '1':
            keywords = input(f"\n{CYAN}[?] Enter target keywords (Leave blank for default): {RESET}").strip()
            cmd = "--scrape --site rekrute emploi_ma maroc_annonces bayt indeed"
            if keywords:
                cmd += f' --keywords "{keywords}"'
            run_command(cmd, "FREE BOARDS DATA ACQUISITION")
            
        elif choice == '02' or choice == '2':
            run_command("--scrape --site linkedin", "LINKEDIN DATA ACQUISITION")
            
        elif choice == '03' or choice == '3':
            run_command("--apollo-enrich", "TARGET ENRICHMENT (APOLLO)")
            
        elif choice == '04' or choice == '4':
            filepath = "email_campaign/scraper_output/scraped_contacts_latest.md"
            if not os.path.exists(filepath):
                 filepath = "email_campaign/scraper_output/scraped_contacts_latest.json"
            view_file(filepath, "LATEST SCRAPED CONTACTS")
            
        elif choice == '05' or choice == '5':
            run_command("--merge-scraped", "AI PAYLOAD GENERATION & MERGE")
            
        elif choice == '06' or choice == '6':
            print(f"\n{CYAN}[*] How many payloads to preview? (Inputs default: 5){RESET}")
            count = input(f"{YELLOW}root@system:~# {RESET}").strip()
            num = count if count.isdigit() else "5"
            run_command(f"--preview {num}", f"PREVIEWING {num} AI PAYLOADS")
            
        elif choice == '07' or choice == '7':
             view_file("emails_prospection.md", "MASTER TARGET LIST")
             
        elif choice == '08' or choice == '8':
            run_command("--test", "TEST DEPLOYMENT")
            
        elif choice == '09' or choice == '9':
            print(f"\n{RED}[!] WARNING: LIVE DEPLOYMENT INITIATED.{RESET}")
            stars = input(f"{CYAN}[?] Target minimum quality (1, 2, or 3) [Default 1]: {RESET}").strip()
            cmd = "--send"
            if stars in ['1', '2', '3']:
                cmd += f" --min-stars {stars}"
            run_command(cmd, "LIVE EMAIL DEPLOYMENT")
            
        elif choice == '10':
            run_command("--follow-up", "FOLLOW-UP SEQUENCE")
            
        elif choice == '11':
            run_command("--check-replies", "INBOUND MONITORING")
            
        elif choice == '00' or choice == '0':
            print(f"\n{GREEN}[+] CONNECTION TERMINATED. GOING DARK.{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{RED}[-] INVALID INPUT. Please select a valid module.{RESET}")
            time.sleep(1.5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] MANUAL OVERRIDE DETECTED. TERMINATING...{RESET}\n")
        sys.exit(0)
