about = """
---------------------------------------------------------------
Author: Fredmark Ivan D. Dizon && John Russel L. Escote
GitHub: https://github.com/veilwr4ith && https://github.com/icode3rror

Project: MIRA - GiraSec Solutions's CLI Password Manager
GitHub Repository: https://github.com/veilwr4ith/MIRA
License: General Public License

Version: 1.2.23
Release Date: 2024-03-12

For Concerns and Issues please email us here:
fredmarkivand@gmail.com
johnrussel205@gmail.com
---------------------------------------------------------------
"""
remember = r"""

 ____________________
/                    \
|       Always       |
|      Remember      |
\____________________/
         !  !
         !  !
         L_ !
        / _)!
       / /__L
 _____/ (____)
        (____)
 _____  (____)
      \_(____)
         !  !
         !  !
         \__/
"""
blehhh = r"""
                                \\_V_//
                                \/=|=\/
                                 [=v=]
                               __\___/_____
                              /..[  _____  ]
                             /_  [ [  M /] ]
                            /../.[ [ M /@] ]
                           <-->[_[ [M /@/] ]
                          /../ [.[ [ /@/ ] ]
     _________________]\ /__/  [_[ [/@/ C] ]
    <_________________>>0---]  [=\ \@/ C / /
       ___      ___   ]/000o   /__\ \ C / /
          \    /              /....\ \_/ /
       ....\||/....           [___/=\___/
      .    .  .    .          [...] [...]
     .      ..      .         [___/ \___]
     .    0 .. 0    .         <---> <--->
  /\/\.    .  .    ./\/\      [..]   [..]
 / / / .../|  |\... \ \ \    _[__]   [__]_
/ / /       \/       \ \ \  [____>   <____]
"""
wolf = r'''
                                 ,ood8888booo,
                              ,od8           8bo,
                           ,od                   bo,
                         ,d8                       8b,
                        ,o                           o,    ,a8b
                       ,8                             8,,od8  8
                       8'                             d8'     8b
                       8                           d8'ba     aP'
                       Y,                       o8'         aP'
                        Y8,                      YaaaP'    ba                       __  ___________  ___
                         Y8o                   Y8'         88                      /  |/  /  _/ __ \/   |
                          `Y8               ,8"           `P                      / /|_/ // // /_/ / /| |
                            Y8o        ,d8P'              ba                     / /  / // // _, _/ ___ |
                       ooood8888888P"""'                  P'                    /_/  /_/___/_/ |_/_/  |_|
                    ,od                                  8                              VeilWr4ith
                 ,dP     o88o                           o'                                1.2.23
                ,dP          8                          8
               ,d'   oo       8                       ,8
               $    d$"8      8           Y    Y  o   8
              d    d  d8    od  ""boooooooob   d"" 8   8
              $    8  d   ood' ,   8        b  8   '8  b
              $   $  8  8     d  d8        `b  d    '8  b
               $  $ 8   b    Y  d8          8 ,P     '8  b
               `$$  Yb  b     8b 8b         8 8,      '8  o,
                    `Y  b      8o  $$o      d  b        b   $o
                     8   '$     8$,,$"      $   $o      '$o$$
                      $o$$P"                 $$o$
'''
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from mnemonic import Mnemonic
import base64
import os
import getpass
import argon2
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from secrets import token_bytes
from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import time
from password_strength import PasswordPolicy
from datetime import datetime, timedelta
from threading import Thread
from termcolor import colored
from pyotp import TOTP, random_base32
from functools import wraps
import string
from collections import deque
import random
import json
import platform
import logging
import sys
import paramiko
import io
import validators
import uuid
from phonenumbers import carrier
import phonenumbers
def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
def get_os_distribution():
    system_info = platform.system()
    if system_info == 'Linux':
        try:
            with open('/etc/os-release', 'r') as f:
                lines = f.readlines()
                distribution_info = {}
                for line in lines:
                    key, value = line.strip().split('=')
                    distribution_info[key] = value.replace('"', '')
                distribution = distribution_info.get('PRETTY_NAME', 'Unknown Distribution')
                version = distribution_info.get('VERSION_ID', 'Unknown Version')
                codename = distribution_info.get('VERSION_CODENAME', 'Unknown Codename')
                base = distribution_info.get('ID_LIKE', 'Unknown Base')
                return f"Linux Distribution: {distribution}\nVersion: {version}\nCodename: {codename}\nBase: {base}\nArchitecture: {platform.architecture()[0]}"
        except FileNotFoundError:
            return "Unable to determine distribution. /etc/os-release file not found."
    elif system_info == 'Darwin':
        version, _, _ = platform.mac_ver()
        return f"macOS Version: {version}\nArchitecture: {platform.architecture()[0]}"
    elif system_info == 'Windows':
        version = platform.version()
        return f"Windows Version: {version}\nArchitecture: {platform.architecture()[0]}"
    else:
        return f"Operating System: {system_info}"
def get_python_version():
    return f"Python Version: {platform.python_version()}"
def check_linux_privileges():
    if 'SUDO_UID' in os.environ.keys() or os.getenv('USER') == 'root':
        return True
    return False
def is_admin():
    if platform.system() == 'Windows':
        try:
            from ctypes import windll
            return windll.shell32.IsUserAnAdmin()
        except Exception:
            return colored("[-] Mira requires elevated privileges on Windows. QUITTING!", "red")
    else:
        return False
def check_windows_privileges():
    return is_admin()
def get_current_datetime():
    current_datetime = datetime.now()
    date_str = current_datetime.strftime("%Y-%m-%d")
    time_str = current_datetime.strftime("%H:%M:%S")
    return f"Current Time: {time_str}\nDate: {date_str}"
if os.name == "posix":
    LOCKOUT_FILE = os.environ.get('LOCKOUT_FILE', '/etc/.lockout')
    ADMIN_DATA_FILE = os.environ.get('USER_DATA_FILE', '/etc/.user')
    PASSFILE = os.environ.get('PASSFILE', '/etc/.pass')
    API = os.environ.get('API', '/etc/.api')
    CARD_PIN_FILE = os.environ.get('CARD_PIN_FILE', '/etc/.card')
    SSH = os.environ.get('SSH', '/etc/.ssh')
    PRIVNOTE = os.environ.get('PRIVNOTE', '/etc/.privnote')
    SRCCODE = os.environ.get('SRCCODE', '/etc/.srccode')
    LOGS = os.environ.get('LOGS', '/etc/.loggings')
elif os.name == "nt":
    program_files_dir = os.environ.get('ProgramFiles', 'C:\\Program Files')
    app_folder_name = 'Mira'
    app_folder_path = os.path.join(program_files_dir, app_folder_name)
    os.makedirs(app_folder_path, exist_ok=True)
    LOCKOUT_FILE = os.path.join(app_folder_path, 'lockout')
    USER_DATA_FILE = os.path.join(app_folder_path, 'user_data')
    PASSFILE = os.path.join(app_folder_path, 'pass')
    API = os.path.join(app_folder_path, 'api')
    CARD_PIN_FILE = os.path.join(app_folder_path, 'card')
    SSH = os.path.join(app_folder_path, 'ssh')
    PRIVNOTE = os.path.join(app_folder_path, 'notes')
    SRCCODE = os.path.join(app_folder_path, 'srccode')
    LOGS = os.path.join(app_folder_path, 'loggings')
class PasswordManager:
    MAX_LOGIN_STR = 20
    MAX_LOGIN_ATTEMPTS = 4 
    LOCKOUT_DURATION_SECONDS = 300
    def __init__(self):
        self.history = InMemoryHistory()
        self.session = PromptSession(history=self.history, auto_suggest=AutoSuggestFromHistory())
        self.master_password = None
        self.cipher = None
        self.ph = PasswordHasher()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename=LOGS, level=logging.INFO, format='%(message)s')
        expiry_thread = Thread(target=self.notify_expiry_background)
        pin_expiry_thread = Thread(target=self.notify_pin_expiry_background)
        pin_expiry_thread.daemon = True
        expiry_thread.daemon = True
        expiry_thread.start()
        pin_expiry_thread.start()
        self.totp_secret_key = None
        self.failed_login_attempts = 0
        self.lockout_time = None
        self.load_lockout_time()
        self.replacements = {
                'a' or 'A': ['4', '@', 'á', 'ä', 'å', 'ą', 'ey', 'a', 'A'],
                'b' or 'B': ['8', '6', 'ß', 'B', 'b'],
                'c' or 'C': ['(', '<', 'ç', 'ć', 'si', 'C', 'c'],
                'd' or 'D': ['[)', '|)', 'đ', 'D', 'd'],
                'e' or 'E': ['3', '€', 'é', 'è', 'ê', 'ë', 'ę', 'E', 'e'],
                'f' or 'F': ['ph', '|=', 'ƒ', 'F', 'f'],
                'g' or 'G': ['9', '6', 'ğ', 'ji', 'G', 'g'],
                'h' or 'H': ['#', '|-|', 'ħ', 'eych', 'H', 'h'],
                'i' or 'I': ['1', '!', 'í', 'ì', 'î', 'ï', 'į', 'ay', 'I', 'i'],
                'j' or 'J': ['_|', '_]', 'й', 'j', 'J'],
                'k' or 'K': ['|<', '|{', 'ķ', 'K', 'k'],
                'l' or 'L': ['1', '|_', 'ł', 'L', 'l'],
                'm' or 'M': ['/\\/\\', '|\\/|', 'м', 'M', 'm'],
                'n' or 'N': ['|\\|', '/\\/', 'ñ', 'ń', 'ň', 'N', 'n'],
                'o' or 'O': ['0', '*', 'ó', 'ö', 'ø', 'ô', 'ő', 'O', 'o'],
                'p' or 'P': ['|>', '|D', 'þ', 'р', 'P'],
                'q' or 'Q': ['(,)', 'kw', 'q', 'Q'],
                'r' or 'R': ['2', '|?', 'г', 'ř', 'R', 'r'],
                's' or 'S': ['$', '5', 'ś', 'š', 'ş', 'ș', 'S', 's'],
                't' or 'T': ['+', '7', 'ţ', 'ť', 'T', 't'],
                'u' or 'U': ['|_|', '\\_\\', 'ü', 'ú', 'ů', 'ű', 'U', 'u'],
                'v' or 'V': ['\\/', 'V', 'v'],
                'w' or 'W': ['\\/\\/', '|/\\|', 'ш', 'щ', 'uu', 'W', 'w'],
                'x' or 'X': ['><', '%', 'ж', 'X', 'x'],
                'y' or 'Y': ['`/', 'ý', 'ÿ', 'ŷ', 'y', 'Y'],
                'z' or 'Z': ['2', '7_', 'ž', 'ź', 'ż', 'z', 'Z'],
                '0': ['o', 'ð', 'ø'],
                '1': ['i', 'l', 'ł'],
                '2': ['z', 'ż', 'ź'],
                '3': ['e', 'ę', 'ė'],
                '4': ['a', 'å', 'ä', 'à', 'á', 'â'],
                '5': ['s', 'š', 'ş', 'ș', 'ś'],
                '6': ['g', 'ğ'],
                '7': ['t', 'ţ', 'ť'],
                '8': ['b', 'ß', 'ь'],
                '9': ['g', 'ğ', 'ĝ'],
            }
    def save_lockout_time(self):
        if self.lockout_time:
            lockout_data = {'lockout_time': self.lockout_time}
            with open(LOCKOUT_FILE, 'w') as lockout_file:
                json.dump(lockout_data, lockout_file)
    def load_lockout_time(self):
        try:
            with open(LOCKOUT_FILE, 'r') as lockout_file:
                lockout_data = json.load(lockout_file)
                self.lockout_time = lockout_data.get('lockout_time')
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    def increment_failed_attempts(self):
        if self.lockout_time and time.time() < self.lockout_time:
            print(colored(blehhh, "red"))
            print(colored(f"[-] Account locked. WE ALREADY TOLD YOU THAT WE DON'T ACCEPT BUGS HERE! If you are the real user, try again after {int(self.lockout_time - time.time())} seconds.", "red"))
            exit()
            return False
        self.failed_login_attempts += 1
        if self.failed_login_attempts >= self.MAX_LOGIN_ATTEMPTS:
            self.lockout_time = time.time() + self.LOCKOUT_DURATION_SECONDS
            self.save_lockout_time()
            print(colored(blehhh, "red"))
            print(colored(f"[-] Too many failed attempts. ARE YOU TRYING TO BRUTEFORCE THIS? WE DON'T ACCEPT SHITTY BUGS HERE! Account locked for {self.LOCKOUT_DURATION_SECONDS} seconds.", "red"))
            exit()
            return False
        return True
    def generate_password(self):
        while True:
            try:
                print(colored("[*] Choose Password Generation Method:", "yellow"))
                print(colored("1. Random by Length", "yellow"))
                print(colored("2. Custom Phrase", "yellow"))
                print(colored("3. Combination of Random and Phrase", "yellow"))
                print(colored("4. Multiple Phrase", "yellow"))
                print(colored("5. Pattern", "yellow"))
                choice = input(colored("MIRAPG ~> ", "yellow"))
                if choice == '1':
                    try:
                        length = int(input(colored("[*] Enter the desired password length: ", "yellow")))
                    except ValueError:
                        length = 30
                        print(colored(f"[**] No length provided!! (default: {length})", "magenta"))
                    password = self.generate_random_password(length)
                elif choice == '2':
                    phrase = input(colored("[*] Enter a custom phrase: ", "yellow"))
                    if not phrase:
                        print(colored("[**] No phrase provided!! using default phrase", "magenta"))
                        phrase = 'mirathebestpasswordmanager'
                    else:
                        phrase = str(phrase)
                    password = self.generate_password_from_phrase(phrase)
                elif choice == '3':
                    try:
                        length = int(input(colored("[*] Enter the desired password length: ", "yellow")))
                    except ValueError:
                        length = 30
                        print(colored(f"[**] No length provided!! (default: {length})", "magenta"))
                    phrase = input(colored("[*] Enter a custom phrase: ", "yellow"))
                    if not phrase:
                        print(colored("[**] No phrase provided, using default phrase!!", "magenta"))
                        phrase = 'mirathebestpasswordmanager'
                    else:
                        phrase = str(phrase)
                    password = self.generate_combined_password(length, phrase)
                elif choice == '4':
                    try:
                        num_phrases = int(input(colored("[*] Enter the number of phrases: ", "yellow")))
                    except ValueError:
                        num_phrases = 4
                        print(colored("[**] No number of phrases provided!! (default: {num_phrases})", "magenta"))
                    phrases = [input(colored(f"[*] Enter phrase {i + 1}: ", "yellow")) for i in range(num_phrases)]
                    password = self.generate_multi_phrase_password(phrases)
                elif choice == '5':
                    pattern = input(colored("[*] Enter the password pattern: ", "yellow"))
                    if not pattern:
                        pattern = 'ulsudauullddaassuldsa'
                        print(colored(f"[**] No pattern provided!! (default: {pattern})", "magenta"))
                    else:
                        pattern = str(pattern)
                    password = self.generate_pattern_password(pattern)
                else:
                    print(colored("[-] Invalid choice. Generating random password by length.", "red"))
                    try:
                        length = int(input(colored("[-] Enter the desired password length: ", "yellow")))
                    except ValueError:
                        length = 30
                        print(colored(f"[**] No length provided!! (default: {length}).", "magenta"))
                    password = self.generate_random_password(length)
                print(colored(f"[+] Generated Password: {password}", "green"))
                break
            except ValueError as e:
                print(colored(f"[-] an error occured: {e}", "red"))
    def generate_combined_password(self, length, phrase):
        position = random.choice(['beginning', 'middle', 'end'])
        if position == 'beginning':
            random_part_length = length - len(phrase)
            random_part = self.generate_random_password(random_part_length)
            transformed_phrase = ''.join([random.choice(self.replacements.get(char.lower(), [char])) for char in phrase])
            password = transformed_phrase + random_part
            return password
        elif position == 'middle':
            random_part1_length = (length - len(phrase)) // 2
            random_part2_length = length - len(phrase) - random_part1_length
            random_part1 = self.generate_random_password(random_part1_length)
            random_part2 = self.generate_random_password(random_part2_length)
            transformed_phrase = ''.join([random.choice(self.replacements.get(char.lower(), [char])) for char in phrase])
            password = random_part1 + transformed_phrase + random_part2
            return password
        elif position == 'end':
            random_part_length = length - len(phrase)
            random_part = self.generate_random_password(random_part_length)
            transformed_phrase = ''.join([random.choice(self.replacements.get(char.lower(), [char])) for char in phrase])
            password = random_part + transformed_phrase
            return password
    def generate_multi_phrase_password(self, phrases):
        transformed_phrases = [''.join([random.choice(self.replacements.get(char.lower(), [char])) for char in phrase]) for phrase in phrases]
        random.shuffle(transformed_phrases)
        password = ''.join(transformed_phrases)
        return password
    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    def generate_password_from_phrase(self, phrase):
        transformed_phrase = ''.join([random.choice(self.replacements.get(char.lower(), [char])) for char in phrase])
        password = ''.join([random.choice([char.upper(), char.lower()]) for char in transformed_phrase])
        return password
    def generate_pattern_password(self, pattern):
        characters = {
            'u': string.ascii_uppercase,
            'l': string.ascii_lowercase,
            'd': string.digits,
            's': string.punctuation,
            'a': string.ascii_letters + string.digits,
        }
        password = ''.join([random.choice(characters.get(char, char)) for char in pattern])
        return password
    def enable_2fa(self):
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        if user_data.get('2fa_enabled', False):
            print(colored("[-] 2FA is already enabled for this user.", "red"))
            return
        self.totp_secret_key = random_base32()
        key = self.encrypt_information(self.totp_secret_key)
        user_data['2fa_enabled'] = True
        user_data['key'] = key
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(user_data, file)
        totp = TOTP(self.totp_secret_key)
        accusn = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        print(colored(f"[+] 2FA Enabled. Now use the account name and the key to get the 6 digit code.\nAccount Name - {accusn}\nKey - {self.totp_secret_key}\nIssuer Name - MIRA (CyberGuard Innovations)", "green"))        
        print(colored("\n[*] Keep your Key secure all the time, it will be asked before you enter the 6-digit code for verification! Please handle your keys with care. It's not our fault if you lose it.", "yellow"))
    def verify_2fa(self, secret_key, code):
        totp = TOTP(secret_key)
        return totp.verify(code)
    def notify_expiry_background(self):
        while True:
            try:
                self.notify_expiry()
            except FileNotFoundError:
                pass
            time.sleep(86400)
    def notify_expiry(self):
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
            for entry in data:
                if 'expiry_at' in entry and entry['expiry_at']:
                    expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                    time_left = expiry_date - datetime.now()
                    if timedelta(days=1) <= time_left <= timedelta(days=7):
                        days_left = time_left.days
                        hours, remainder = divmod(time_left.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        print(colored(f"[!] Warning: Some of your passwords will expire in {days_left} days, {hours} hours, {minutes} minutes, and {seconds} seconds. Please update them!", 'yellow'))
                    elif time_left < timedelta(days=1) and time_left >= timedelta(seconds=0):
                        print(colored(f"[!] Alert: Some of your passwords will expired in any minute! Please update them!", 'red'))
                    elif time_left <= timedelta(seconds=0):
                        print(colored(f"[!] Alert: Some of your passwords has expired. Update is now mandatory for accessibility!", 'red'))
        except FileNotFoundError:
            pass
    def notify_pin_expiry_background(self):
        while True:
            try:
                self.notify_pin_expiry()
            except FileNotFoundError:
                pass
            time.sleep(86400)
    def notify_pin_expiry(self):
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
            for entry in data:
                if 'expiry_at' in entry and entry['expiry_at']:
                    expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                    time_left = expiry_date - datetime.now()
                    if timedelta(days=1) <= time_left <= timedelta(days=7):
                        days_left = time_left.days
                        hours, remainder = divmod(time_left.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        print(colored(f"[!] Warning: Some of your PINs will expire in {days_left} days, {hours} hours, {minutes} minutes, and {seconds} seconds. Please update them!", 'yellow'))
                    elif time_left < timedelta(days=1) and time_left >= timedelta(seconds=0):
                        print(colored(f"[!] Alert: Some of your PINs will expire in any minute! Please update them!", 'red'))
                    elif time_left <= timedelta(seconds=0):
                        print(colored(f"[!] Alert: Some of your PINs has expired. Update is now mandatory for accessibility!", 'red'))
        except FileNotFoundError:
            pass
    def load_encryption_key(self, encryption_key):
        self.cipher = self.initialize_cipher(encryption_key)
    def initialize_cipher(self, key):
        return Fernet(key)
    def check_master_password_strength(self, password):
        policy = PasswordPolicy.from_names(
            length=15,
            uppercase=1,
            numbers=1,
            special=4,
        )
        result = policy.test(password)
        if result:
            print(colored("[-] Master password is not strong enough (Not Added). Please follow our password policy for master password:", "red"))
            for violation in result:
                print(colored(f"    {violation}", "red"))   
            generate_strong_pass = input(colored("[*] Do you want Mira to generate a strong password for you? (y/N): ", "yellow"))
            if generate_strong_pass == 'y':
                self.generate_password()
                print(colored("[*] Now repeat the process and use that password instead.", "magenta"))
            else:
                print(colored("[-] Abort.", "red"))
            return False
        return True
    def check_password_strength(self, password):
        policy = PasswordPolicy.from_names(
            length=10,
            uppercase=1,
            numbers=1,
            special=1,
        )
        result = policy.test(password)
        if result:
            print(colored("[-] Password is not strong enough:", "red"))
            for violation in result:
                print(colored(f"    {violation}", "red"))
            user_choice = input(colored("[*] Do you want to use this password anyway? (y/N): ", "yellow"))
            if user_choice.lower() == 'y':
                return True
            else:
                generate_strong_pass = input(colored("[*] Do you want Mira to generate a strong password for you? (y/N): ", "yellow"))
                if generate_strong_pass.lower() == 'y':
                    self.generate_password()
                    print(colored("[*] Now repeat the process and use that password instead.", "magenta"))
                else:
                    print(colored("[-] Abort.", "red"))
                return False
        return True
    def register(self, username, master_password):
        if not self.check_master_password_strength(master_password):
            return
        if os.path.exists(USER_DATA_FILE) and os.path.getsize(USER_DATA_FILE) != 0:
            print(colored("[-] Master user already exists!!", "red"))
        else:
            self.master_password = master_password
            salt = token_bytes(100)
            salt_hex = salt.hex()
            saltier = token_bytes(300)
            saltier_hex = salt.hex()
            saltiest = token_bytes(1000)
            saltiest_hex = salt.hex()
            hashed_master_password = self.ph.hash(master_password + saltier_hex)
            hashed_username = self.ph.hash(username + salt_hex)
            encryption_key = Fernet.generate_key()
            fernet = Fernet(encryption_key) 
            encrypted_master_password = fernet.encrypt(hashed_master_password.encode())
            encrypted_username = fernet.encrypt(hashed_username.encode())
            encrypted_username_b64 = base64.b64encode(encrypted_username).decode()
            encrypted_master_password_b64 = base64.b64encode(encrypted_master_password).decode()
            ph = argon2.PasswordHasher()
            hashed_encryption_key = ph.hash(encryption_key.decode() + saltiest_hex)
            user_data = {
                '2328131181237': saltiest_hex,
                '3223245431342': encrypted_username_b64,
                '3543645771234': salt_hex,
                '9034374927023': encrypted_master_password_b64,
                '4017916987192': hashed_encryption_key,
                '2104941992374': saltier_hex
            }
            with open(USER_DATA_FILE, 'w') as file:
                json.dump(user_data, file)
                clear_terminal()
                print(colored(wolf, "blue"))
                print(colored("\n[+] Registration complete!!", "green"))
                print(colored(f"[+] Encryption key: {encryption_key.decode()}", "green"))
                print(colored("\n[*] Caution: Save your encryption key and store it somewhere safe Mira will never recover your encryption key once you forgot it!!! So please don't be stupid:)", "yellow"))
    def get_username_log(self, uname):
        return uname
    def log_login_attempt(self, login_status):
        try:
            with open(LOGS, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        log_entry = {
            'time': time.strftime("%Y-%m-%d %H:%M:%S"),
            'status': 'Success' if login_status else 'Failed',
            'entered_username': self.get_username_log(username)
        }
        if len(data)>= PasswordManager.MAX_LOGIN_STR:
            data = data[5:]
        data.append(log_entry)
        with open(LOGS, 'w') as file:
            json.dump(data, file, indent=4)
        if login_status:
            pass
        else:
            pass
    def login(self, username, entered_password, encryption_key):
        if not os.path.exists(USER_DATA_FILE):
            print(colored("\n[-] You have not registered. Do that first!", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        if self.lockout_time and time.time() < self.lockout_time:
            clear_terminal()
            print(colored(blehhh, "red"))
            print(colored(f"[-] Account locked. WE ALREADY TOLD YOU THAT WE DON'T ACCEPT SHITTY BUGS HERE! If you are the real user, try again after {int(self.lockout_time - time.time())} seconds.", "red"))
            exit()
            return
        stored_encryption_key = user_data.get('4017916987192', '')
        ph = PasswordHasher()
        try:
            if not ph.verify(stored_encryption_key, encryption_key + user_data.get('2328131181237', '')):
                raise VerifyMismatchError("Encryption key mismatch")
        except VerifyMismatchError:
            print(colored("[-] Invalid Login Credentials. Login Failed!", "red"))
            self.log_login_attempt(False)
            if self.increment_failed_attempts():
                return
            else:
                return
        self.load_encryption_key(encryption_key.encode())
        fernet = Fernet(encryption_key)
        decrypted_username = fernet.decrypt(base64.b64decode(user_data.get('3223245431342', ''))).decode()
        decrypted_master_password = fernet.decrypt(base64.b64decode(user_data.get('9034374927023', ''))).decode()
        try:
            self.ph.verify(decrypted_username, username + user_data.get('3543645771234', ''))
            self.ph.verify(decrypted_master_password, entered_password + user_data.get('2104941992374', ''))
            if '2fa_enabled' in user_data and user_data['2fa_enabled']:
                key = self.decrypt_information(user_data['key'])
                code = getpass.getpass(colored("[*] 6-DIgit Code (2FA): ", "yellow")) 
                if not self.verify_2fa(key, code):
                    print(colored("[-] Invalid 2FA Code. Login Failed!", "red"))
                    self.log_login_attempt(False)
                    if self.increment_failed_attempts():
                        return
                    else:
                        return
            print(colored("[+] Login Successful.. Please Wait....", "green"))
            self.log_login_attempt(True)
            time.sleep(10)
            clear_terminal()
            print(colored(wolf, "blue"))
            self.master_password = entered_password
            self.main_menu()
        except VerifyMismatchError:
            print(colored("[-] Invalid Login Credentials. Login Failed!", "red"))
            self.log_login_attempt(False)
            if self.increment_failed_attempts():
                return
            else:
                return
    def show_loggings(self):
        try:
            with open(LOGS, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    key_status = []
                    for entry in data:
                        key_status.append({
                            'time': entry['time'],
                            'status': entry['status'],
                            'username': entry['entered_username']
                        })
                elif isinstance(data, dict): 
                    key_status = [{
                        'time': data['time'],
                        'status': data['status'],
                        'username': data['entered_username']
                    }]
                else:
                    raise ValueError("Invalid JSON format")
                if key_status:
                    print(colored("[+] All Previous Logs:", "green"))
                    print(colored("\nTime Logged".ljust(31) + "Status".ljust(24) + "Entered Username", "cyan"))
                    print(colored("--------------------".ljust(30) + "-------------".ljust(24) + "--------------------", "cyan"))
                    for user_status in key_status:
                        if user_status['status'] == "Success":
                            status_color = 'green'
                        else:
                            status_color = 'red'
                        print(f"{colored(str(user_status['time']).ljust(30), 'cyan')}{colored(str(user_status['status']).ljust(24), status_color)}{colored(str(user_status['username']), 'cyan')}")
                else:
                    print(colored("[-] No Logs has been found.", "red"))
        except FileNotFoundError:
            print(colored("[-] No Logs has been found.", "red"))
    def show_ssh_key(self):
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
            key_id = input(colored("[*] Key ID: ", "yellow"))
            if key_id.isdigit():
                key_id = int(key_id)
            else:
                pass
            key_status = []
            for entry in data:
                if entry['key_id'] == key_id or (isinstance(key_id, str) and key_id.lower() == 'all'):
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    key_status.append({
                        'key_id': entry['key_id'],
                        'username': self.decrypt_information(entry['username']),
                        'key_name': self.decrypt_information(entry['key_name']),
                        'added_at': added_at
                    })
            if key_status:
                if key_id == 'all' or not key_id:
                    print(colored("[+] All Available SSH Keys:", "green"))
                    print(colored("\nKey ID".ljust(23) + "Username".ljust(30) + "SSH Key Name".ljust(30) + "Added At", "cyan"))
                    print(colored("----------".ljust(22) + "--------------------".ljust(30) + "--------------------".ljust(30) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['key_id']).ljust(22), 'cyan')}{colored(str(user_status['username']).ljust(30), 'cyan')}{colored(str(user_status['key_name']).ljust(30), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
                else:
                    print(colored(f"[+] Info about this Key ID {key_id}:", "green"))
                    print(colored("\nUsername".ljust(28) + "SSH Key Name".ljust(29) + "Added At", "cyan"))
                    print(colored("--------------------".ljust(27) + "--------------------".ljust(29) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['username']).ljust(27), 'cyan')}{colored(str(user_status['key_name']).ljust(29), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Key ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No SSH Key saved. Show SSH Keys failed!", "red"))
    def show_src_code_status(self):
        try:
            with open(SRCCODE, 'r') as file:
                data = json.load(file)
            code_id = input(colored("[*] Code ID: ", "yellow"))
            if code_id.isdigit():
                code_id = int(code_id)
            else:
                pass
            key_status = []
            for entry in data:
                if entry['code_id'] == code_id or (isinstance(code_id, str) and code_id.lower() == 'all'):
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    key_status.append({
                        'code_id': entry['code_id'],
                        'filename': self.decrypt_information(entry['filename']),
                        'added_at': added_at
                    })
            if key_status:
                if code_id == 'all' or not code_id:
                    print(colored("[+] All Available Source Codes:", "green"))
                    print(colored("\nCode ID".ljust(23) + "File Name".ljust(30) + "Added At", "cyan"))
                    print(colored("----------".ljust(22) + "--------------------".ljust(30) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['code_id']).ljust(22), 'cyan')}{colored(str(user_status['filename']).ljust(30), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
                else:
                    print(colored(f"[+] Info about this Code ID {code_id}:", "green"))
                    print(colored("\nFile Name".ljust(28) + "Added At", "cyan"))
                    print(colored("--------------------".ljust(27) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['filename']).ljust(27), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Code ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No Source Code saved. Show Source Code failed!", "red"))
    def show_api_key(self):
        try:
            with open(API, 'r') as file:
                data = json.load(file)
            acc_id = input(colored("[*] Account ID: ", "yellow"))
            if acc_id.isdigit():
                acc_id = int(acc_id)
            else:
                pass
            key_status = []
            for entry in data:
                if entry['unique_id'] == acc_id or (isinstance(acc_id, str) and acc_id.lower() == 'all'):
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    key_status.append({
                        'unique_id': entry['unique_id'],
                        'platform': entry['platform'],
                        'username': self.decrypt_information(entry['key_name']),
                        'added_at': added_at
                    })
            if key_status:
                if acc_id == 'all' or not acc_id:
                    print(colored("[+] All Available API Keys:", "green"))
                    print(colored("\nAccount ID".ljust(23) + "Platform".ljust(30) + "API Key Name".ljust(30) + "Added At", "cyan"))
                    print(colored("----------".ljust(22) + "--------------------".ljust(30) + "--------------------".ljust(30) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['unique_id']).ljust(22), 'cyan')}{colored(str(user_status['platform']).ljust(30), 'cyan')}{colored(str(user_status['username']).ljust(30), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
                else:
                    print(colored(f"[+] Info about this Account ID {acc_id}:", "green"))
                    print(colored("\nPlatform".ljust(28) + "API Key Name".ljust(30) + "Added At", "cyan"))
                    print(colored("--------------------".ljust(27) + "--------------------".ljust(30) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['platform']).ljust(27), 'cyan')}{colored(str(user_status['username']).ljust(30), 'cyan')}{colored(str(user_status['added_at'].ljust(25)), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Account ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No API Key saved. Show API Key failed!", "red"))
    def show_priv_note_status(self):
        try:
            with open(PRIVNOTE, 'r') as file:
                data = json.load(file)
            note_id = input(colored("[*] Note ID: ", "yellow"))
            if note_id.isdigit():
                note_id = int(note_id)
            else:
                pass
            key_status = []
            for entry in data:
                if entry['note_id'] == note_id or (isinstance(note_id, str) and note_id.lower() == 'all'):
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    key_status.append({
                        'note_id': entry['note_id'],
                        'title': self.decrypt_information(entry['title']),
                        'added_at': added_at
                    })
            if key_status:
                if note_id == 'all' or not note_id:
                    print(colored("[+] All Available Notes:", "green"))
                    print(colored("\nNote ID".ljust(23) + "Title".ljust(30) + "Added At", "cyan"))
                    print(colored("----------".ljust(22) + "--------------------".ljust(30) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['note_id']).ljust(22), 'cyan')}{colored(str(user_status['title']).ljust(30), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
                else:
                    print(colored(f"[+] Info about this Note ID {note_id}:", "green"))
                    print(colored("\nTitle".ljust(28) + "Added At", "cyan"))
                    print(colored("--------------------".ljust(27) + "-------------------", "cyan"))
                    for user_status in key_status:
                        print(f"{colored(str(user_status['title']).ljust(27), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Note ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No Private Notes saved. Show Private Notes failed!", "red"))
    def show_pin_expiry_status(self):
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
            card_id = input(colored("[*] Card ID: ", "yellow"))
            if card_id.isdigit():
                card_id = int(card_id)
            else:
                pass
            card_status = []
            for entry in data:
                if entry['card_id'] == card_id or (isinstance(card_id, str) and card_id.lower() == 'all'):
                    expiry_status, remaining_time = self.check_expiry_status(entry.get('expiry_at'))
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    expiry_at = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    card_status.append({
                        'card_id': entry['card_id'],
                        'card_type': entry['card_type'],
                        'card_number': self.decrypt_information(entry['card_number']),
                        'status': expiry_status,
                        'added_at': added_at,
                        'expiry_at': expiry_at,
                        'remaining_time': remaining_time
                    })
            if card_status:
                if card_id == 'all' or not card_id:
                    print(colored("[+] All Available Card IDs:", "green"))
                    print(colored("\nCard ID".ljust(22) + "Card Type".ljust(21) + "Card Number".ljust(30) + "Status".ljust(16) + "Added At".ljust(25) + "Expiry At".ljust(25) + "Remaining Time", "cyan"))
                    print(colored("----------".ljust(21) + "----------".ljust(21) + "--------------------".ljust(30) + "----------".ljust(16) + "-------------------".ljust(25) + "-------------------".ljust(25) + "------------------------", "cyan"))
                    for user_status in card_status:
                        print(f"{colored(str(user_status['card_id']).ljust(21), 'cyan')}{colored(str(user_status['card_type']).ljust(21), 'cyan')}{colored(str(user_status['card_number']).ljust(30), 'cyan')}{colored(str(user_status['status']).ljust(25), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}{colored(str(user_status['expiry_at']).ljust(25), 'cyan')}{colored(str(user_status['remaining_time']).ljust(30), 'cyan')}")
                else:
                    print(colored(f"[+] Status of this card ID {card_id}:", "green"))
                    print(colored("\nCard Type".ljust(23) + "Card Number".ljust(30) + "Status".ljust(24) + "Added At".ljust(25) + "Expiry At".ljust(25) + "Remaining Time", "cyan"))
                    print(colored("----------".ljust(22) + "--------------------".ljust(30) + "----------".ljust(24) + "-------------------".ljust(25) + "-------------------".ljust(25) + "------------------------", "cyan"))
                    for user_status in card_status:
                        print(f"{colored(str(user_status['card_type']).ljust(22), 'cyan')}{colored(str(user_status['card_number']).ljust(30), 'cyan')}{colored(str(user_status['status']).ljust(33), 'cyan')}{colored(str(user_status['added_at']).ljust(25), 'cyan')}{colored(str(user_status['expiry_at']).ljust(24), 'cyan')} {colored(str(user_status['remaining_time']).ljust(30), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Card ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No PIN saved. Show expiry status failed!", "red"))
    def show_passwd_strength(self):
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
            acc_id = input(colored("[*] Account ID: ", "yellow"))
            if acc_id.isdigit():
                acc_id = int(acc_id)
            else:
                pass
            passwd_strength = []
            for entry in data:
                if entry['account_id'] == acc_id or (isinstance(acc_id, str) and acc_id.lower() == 'all'):
                    password = self.decrypt_password(entry['password'])
                    strength = self.check_password_strngth(password)
                    passwd_strength.append({
                        'acc_id': entry['account_id'],
                        'website': self.decrypt_information(entry['website']),
                        'username': self.decrypt_information(entry['username']),
                        'strength': strength
                    })
            if passwd_strength:
                if acc_id == 'all' or not acc_id:
                    print(colored("[+] All Available Users:", "green"))
                    print(colored("\nAccount ID".ljust(25) + "Platform".ljust(31) + "Username".ljust(30) + "Strength", "cyan"))
                    print(colored("----------".ljust(24) + "--------------------".ljust(31) + "--------------------".ljust(30) + "----------", "cyan"))
                    for user_status in passwd_strength:
                        print(f"{colored(str(user_status['acc_id']).ljust(24), 'cyan')}{colored(str(user_status['website']).ljust(31), 'cyan')}{colored(str(user_status['username']).ljust(30), 'cyan')}{colored(str(user_status['strength']), 'cyan')}")
                else:
                    print(colored(f"[+] Password Strength of this Account ID {acc_id}:", "green"))
                    print(colored("\nPlatform".ljust(29) + "Username".ljust(31) + "Strength", "cyan"))
                    print(colored("--------------------".ljust(28) + "--------------------".ljust(31) + "----------", "cyan"))
                    for user_status in passwd_strength:
                        print(f"{colored(str(user_status['website']).ljust(28), 'cyan')}{colored(str(user_status['username']).ljust(31), 'cyan')}{str(user_status['strength'])}")
            else:
                print(colored("[-] No matching entries found for the specified Account ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No passwords saved. Show password strength failed!", "red"))
    def check_password_strngth(self, password):
        is_length_valid = len(password) > 10
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special_char = any(char.isalnum() == False for char in password)
        conditions_met = [is_length_valid, has_uppercase, has_lowercase, has_digit, has_special_char]
        num_conditions_met = sum(conditions_met)
        if num_conditions_met == 5:
            return colored("Strong", "green")
        elif num_conditions_met >= 3:
            return colored("Moderate", "yellow")
        else:
            return colored("Weak", "red")
    def show_expiry_status(self):
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
            acc_id = input(colored("[*] Account ID: ", "yellow"))
            if acc_id.isdigit():
                acc_id = int(acc_id)
            else:
                pass
            usernames_status = []
            for entry in data:
                if entry['account_id'] == acc_id or (isinstance(acc_id, str) and acc_id.lower() == 'all'):
                    expiry_status, remaining_time = self.check_expiry_status(entry.get('expiry_at'))
                    website = self.decrypt_information(entry['website'])
                    username = self.decrypt_information(entry['username'])
                    added_at = datetime.strptime(entry['added_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    expiry_at = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                    usernames_status.append({
                        'account_id': entry['account_id'],
                        'website': website,
                        'username': username,
                        'status': expiry_status,
                        'added_at': added_at,
                        'expiry_at': f"{expiry_at}",
                        'remaining_time': remaining_time
                    })
            if usernames_status:
                if acc_id == 'all' or not acc_id:
                    print(colored("[+] All Available Platforms:", "green"))
                    print(colored("\nAccount ID".ljust(15) + "Platform".ljust(25) + "Username".ljust(25) + "Status".ljust(16) + "Added At".ljust(25) + "Expiry At".ljust(25) + "Remaining Time", "cyan"))
                    print(colored("----------".ljust(14) + "--------------------".ljust(25) + "--------------------".ljust(25) + "----------".ljust(16) + "-------------------".ljust(25) + "-------------------".ljust(25) + "------------------------", "cyan"))
                    for user_status in usernames_status:
                        print(f"{colored(str(user_status['account_id']).ljust(14), 'cyan')}{colored(str(user_status['website']).ljust(25), 'cyan')}{colored(str(user_status['username']).ljust(25), 'cyan')}{str(user_status['status']).ljust(25)}{colored(str(user_status['added_at']).ljust(25), 'cyan')}{colored(str(user_status['expiry_at']).ljust(24), 'cyan')} {colored(str(user_status['remaining_time']).ljust(30), 'cyan')}")
                else:
                    print(colored(f"[+] Status of this Account ID {acc_id}:", "green"))
                    print(colored("\nPlatform".ljust(26) + "Username".ljust(24) + "Status".ljust(14) + "Added At".ljust(25) + "Expiry At".ljust(25) + "Remaining Time", "cyan"))
                    print(colored("--------------------".ljust(25) + "--------------------".ljust(24) + "----------".ljust(14) + "-------------------".ljust(25) + "-------------------".ljust(25) + "------------------------", "cyan"))
                    for user_status in usernames_status:
                        print(f"{colored(user_status['website'].ljust(25), 'cyan')}{colored(user_status['username'].ljust(24), 'cyan')}{user_status['status'].ljust(23)}{colored(user_status['added_at'].ljust(25), 'cyan')}{colored(user_status['expiry_at'].ljust(24), 'cyan')} {colored(user_status['remaining_time'].ljust(30), 'cyan')}")
            else:
                print(colored("[-] No matching entries found for the specified Account ID.", "red"))
        except FileNotFoundError:
            print(colored("[-] No passwords saved. Show expiry status failed!", "red"))
    def check_expiry_status(self, expiry_date):
        if expiry_date:
            expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d %H:%M:%S")
            time_left = expiry_date - datetime.now()
            if timedelta(days=1) <= time_left <= timedelta(days=7):
                return colored("Nearly Expired", "yellow"), str(time_left)
            elif time_left < timedelta(days=1) and time_left >= timedelta(seconds=0):
                return colored("About to Expire", "magenta"), str(time_left)
            elif time_left <= timedelta(seconds=0):
                return colored("Expired", "red"), colored("0 days, 0 hours, 0 minutes, 0 seconds", "red")
            else:
                days_left = time_left.days
                hours, remainder = divmod(time_left.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                remaining_time = f"{days_left} days, {hours} hours, {minutes} minutes, {seconds} seconds"
                return colored("Updated", "green"), str(time_left)
        return "OK", "N/A"
    def main_menu(self):
        prompt = True
        while prompt:
            prompt = HTML(f"<ansiblue>MIRA@MaiN ~> </ansiblue>")
            choice = self.session.prompt(prompt)
            if choice == "":
                continue
            elif choice == 'add_platform_passwd':
                website = input(colored("[*] Platform: ", "yellow"))
                if not validators.url(website):
                    print(colored("[-] The Platform you've entered is Invalid! Please make sure that it's in URL form.", "red"))
                    continue
                email_or_phone = input(colored("[*] Email Address/Phone(CC): ", "yellow"))
                if not (validators.email(email_or_phone) or self.validate_phone_number(email_or_phone)):
                    print(colored("[-] The Email/Phone you've entered is Invalid!", "red"))
                    continue
                username = input(colored("[*] Username: ", "yellow"))
                password = getpass.getpass(colored("[*] Password: ", "yellow"))
                re_enter = getpass.getpass(colored("[*] Re-Enter Password: ", "yellow"))
                if re_enter != password:
                    print(colored("[-] Password did not match! QUITTING!", "red"))
                else:
                    self.add_password(website, email_or_phone, username, password)
                    self.notify_expiry()
                    self.notify_pin_expiry()
            elif choice == 'get_platform_passwd':
                try:
                    acc_id = int(input(colored("[*] Account ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid account ID.", "red"))
                    continue
                decrypted_password = self.get_password(acc_id)
                try:
                    with open(PASSFILE, 'r') as file:
                        data = json.load(file)
                    if acc_id not in [entry['account_id'] for entry in data]:
                        print(colored(f"[-] This ID {acc_id} doesn't exist", "red"))
                    for entry in data:
                        if entry['account_id'] == acc_id and 'expiry_at' in entry and entry['expiry_at']:
                            expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                            if datetime.now() > expiry_date:
                                response = input(colored("[*] Password has expired. Do you want to update the password or delete the account for this platform? (U/D): ", "yellow")).lower()
                                if response == 'u':
                                    new_password = getpass.getpass(colored("[*] New Password: ", "yellow"))
                                    re_enter = getpass.getpass(colored("[*] Re-Enter New Password: ", "yellow"))
                                    if any(self.decrypt_password(entry['password']) == new_password for entry in data):
                                        print(colored("[-] Password has been used, avoid reusing passwords. QUITTING!!", "red"))
                                        continue
                                    if re_enter != new_password:
                                        print(colored("[-] Password did not match! QUITTING!", "red"))
                                        continue
                                    if self.check_password_reuse(new_password, data):
                                        print(colored("[-] Password has been used on other platforms. Avoid using the same password on other platforms!!", "red"))
                                        continue
                                    if not self.check_password_strength(new_password):
                                        continue
                                    entry['password'] = self.encrypt_password(new_password)
                                    entry['expiry_at'] = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
                                    with open(PASSFILE, 'w') as file:
                                        json.dump(data, file, indent=4)
                                    decrypted_password = self.decrypt_password(entry['password'])
                                    if decrypted_password:
                                        print(colored(f"[+] Password updated successfully.", "green"))
                                        continue
                                    else:
                                        print(colored("[-] Password has expired. Please update your password.", "red"))
                                    continue
                                elif response == 'd':
                                    caution = input(colored("[*] Caution: Once you remove it, it will be permanently deleted from your system. Are you sure you want to proceed? (y/N): ", "yellow"))
                                    if caution == 'n':
                                        print(colored("[-] Abort.", "red"))
                                        continue
                                    elif caution == 'y':
                                        data = [e for e in data if not (e['account_id'] == acc_id)]
                                        with open(self.PASSFILE, 'w') as file:
                                            json.dump(data, file, indent=4)
                                        print(colored("[-] Website permanently deleted.", "red"))
                                        continue
                            else:
                                email_phone = self.decrypt_information(entry['email_address/phone'])
                                if email_phone.lstrip('+').isdigit():
                                    parsed_phone = phonenumbers.parse(email_phone, None)
                                    if phonenumbers.is_valid_number(parsed_phone):
                                        carrier_name = carrier.name_for_number(parsed_phone, "en")
                                        email_phone = f"{email_phone} ({carrier_name})"
                                if decrypted_password is not None:
                                    print(colored(f"[+] Platform: {self.decrypt_information(entry['website'])}\n[+] Email/Phone: {email_phone}\n[+] Username: {self.decrypt_information(entry['username'])}\n[+] Key Content: {decrypted_password}", "green"))
                                    self.notify_expiry()
                                    self.notify_pin_expiry()
                                else:
                                    print(colored("[-] Password not found! Did you save the password?", "red"))
                except FileNotFoundError:
                    print(colored("[-] No passwords have been saved yet. Retrieve passwords failed!", "red"))
            elif choice == 'changemaster':
                self.change_master_password()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'genpasswd':
                self.generate_password()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'del_platform_passwd':
                self.delete_password()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'del_card_pin':
                self.delete_card_pin()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'del_api_key':
                self.delete_key()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'show_api_key':
                self.show_api_key()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'add_priv_note':
                title = input(colored("[*] Title: ", "yellow"))
                print(colored("[*] Paste your Note (Type 'END' on a new line to finish):", "yellow"))
                note_lines = []
                try:
                    while True:
                        line = input()
                        note_lines.append(line)
                        if line.upper() == "END":
                            if not note_lines:
                                print(colored("[-] Editor is empty. Nothing to save.", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                                break
                            note = '\n'.join(note_lines[:-1])
                            self.add_private_note(title, note)
                            self.notify_expiry()
                            self.notify_pin_expiry()
                            break
                except Exception as e:
                    print("Error:", e)
                    continue
            elif choice == 'get_priv_note':
                try:
                    try:
                        note_id = int(input(colored("[*] Note ID: ", "yellow")))
                    except ValueError:
                        print(colored("[-] Invalid Note ID", "red"))
                        continue
                    with open(PRIVNOTE, 'r') as file:
                        data = json.load(file)
                    decrypted_note = self.get_private_note(note_id)
                    key_found = False
                    for entry in data:
                        if entry['note_id'] == note_id:
                            key_found = True
                            if decrypted_note is not None:
                                print(colored(f"[+] Title: {colored(self.decrypt_information(entry.get('title')), 'green')}", "yellow"))
                                print(colored(f"[+] Note:", "yellow"))
                                formatted_note = ''.join(decrypted_note)
                                print(colored(formatted_note, "green"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                            else:
                                print(colored("[-] Private Note not found. QUITTING!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                except FileNotFoundError:
                    print(colored("[-] Private Note not found. QUITTING!", "red"))
                    continue
            elif choice == 'del_priv_note':
                self.delete_private_note()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'ch_priv_note':
                try:
                    note_id = int(input(colored("[*] Note ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid Note ID", "red"))
                    return
                try:
                    with open(PRIVNOTE, 'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    print(colored("[-] Private Note not found. QUITTING!", "red"))
                    return
                index = -1
                for i, entry in enumerate(data):
                    if entry['note_id'] == note_id:
                        index = i
                        break
                if index == -1:
                    print(colored("[-] Note ID not found. QUITTING!", "red"))
                    return
                existing_content = self.decrypt_information(data[index]['note'])
                print(colored("[*] Current Note Content:", "yellow"))
                print(existing_content)
                additional_content = []
                print(colored("[*] Paste New Content, type 'END' in a new line to finish:", "yellow"))
                try:
                    while True:
                        line = input()
                        additional_content.append(line)
                        if line.upper() == "END":
                            break
                except Exception as e:
                    print("Error:", e)
                    continue
                new_content = '\n'.join(additional_content[:-1])
                data[index]['note'] = self.encrypt_information(new_content)
                with open(PRIVNOTE, 'w') as file:
                    json.dump(data, file, indent=4)
                print(colored("[+] New content added to the Private Note successfully!", "green"))
            elif choice == 'add_src_code':
                filename = input(colored("[*] File Name: ", "yellow"))
                if not filename:
                    print(colored("[-] No filename provided! QUITTING!", "red"))
                    continue
                print(colored("[*] Paste the Source Code Below (Type 'END' on a new line to finish):", "yellow"))
                source_code_lines = []
                try:
                    while True:
                        code = input()
                        source_code_lines.append(code)
                        if code.upper() == "END":
                            source_code = '\n'.join(source_code_lines[:-1])
                            self.add_source_code(filename, source_code)
                            self.notify_expiry()
                            self.notify_pin_expiry()
                            break
                except Exception as e:
                    print("Error:", e)
                    continue
            elif choice == 'get_src_code':
                try:
                    try:
                        code_id = int(input(colored("[*] Code ID: ", "yellow")))
                    except ValueError:
                        print(colored("[-] Invalid Code ID", "red"))
                        continue
                    with open(SRCCODE, 'r') as file:
                        data = json.load(file)
                    decrypted_code = self.get_source_code(code_id)
                    key_found = False
                    for entry in data:
                        if entry['code_id'] == code_id:
                            key_found = True
                            if decrypted_code is not None:
                                print(colored(f"[+] File Name: {colored(self.decrypt_information(entry.get('filename')), 'green')}", "yellow"))
                                print(colored(f"[+] Source Code:", "yellow"))
                                formatted_code = ''.join(decrypted_code)
                                print(colored(formatted_code, "green"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                            else:
                                print(colored("[-] Source Code not found. QUITTING!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                except FileNotFoundError:
                    print(colored("[-] Source Code not found. QUITTING!", "red"))
                    continue
            elif choice == 'del_src_code':                                        
                self.delete_source_code()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'ch_src_code':
                try:
                    code_id = int(input(colored("[*] Code ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid Code ID", "red"))
                    return
                updated_source_code = []
                try:
                    with open(SRCCODE, 'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    print(colored("[-] Source Code not found. QUITTING!", "red"))
                    return
                index = -1
                for i, entry in enumerate(data):
                    if entry['code_id'] == code_id:
                        index = i
                        break
                if index == -1:
                    print(colored("[-] Code ID not found. QUITTING!", "red"))
                    return
                print(colored("[*] Paste Updated Source Code Below (Type 'END' on a new line to finish):", "yellow"))
                try:
                    while True:
                        line = input()
                        updated_source_code.append(line)
                        if line.upper() == "END":
                            break
                except Exception as e:
                    print("Error:", e)
                    continue
                source_code = '\n'.join(updated_source_code[:-1])
                try:
                    with open(SRCCODE, 'r') as file:
                        data = json.load(file)
                except json.JSONDecodeError:
                    data = []
                for entry in data:
                    if entry['code_id'] == code_id:                        
                        entry['code'] = self.encrypt_information(source_code)
                        with open(SRCCODE, 'w') as file:           
                            json.dump(data, file, indent=4)               
                            decrypted_code = self.decrypt_information(entry['code'])
                        if decrypted_code:
                            print(colored("[+] Source Code updated successfully!", "green"))
                            self.notify_expiry()
                            self.notify_pin_expiry()
                        else:
                            print(colored("[-] Source Code update failed.", "red")) 
                            self.notify_expiry()
                            self.notify_pin_expiry()
            elif choice == 'add_ssh_key':
                username = input(colored("[*] Username: ", "yellow"))
                if not username:
                    print(colored("[-] No username provided! QUITTING!", "red"))
                    continue
                key_name = input(colored("[*] Key Name: ", "yellow"))
                if not key_name:
                    print(colored("[-] No key name provided! QUITTING!", "red"))
                    continue
                print(colored("[*] Paste the Private Key Below (Type 'END' on a new line to finish):", "yellow"))
                private_key_lines = []
                try:
                    while True:
                        line = input()
                        private_key_lines.append(line)
                        if line.upper() == "END":
                            break
                except Exception as e:
                    print("Error:", e)
                    continue
                print(colored("[*] Paste the Public Key Below (Type 'END' on a new line to finish):", "yellow"))
                public_key_lines = []
                try:
                    while True:
                        line = input()
                        public_key_lines.append(line)
                        if line.upper() == "END":
                            break
                except Exception as e:
                    print("Error:", e)
                    continue
                private_key = '\n'.join(private_key_lines[:-1])
                public_key = '\n'.join(public_key_lines[:-1])
                is_password_protected = False
                passphrase = None
                try:
                    key = paramiko.RSAKey(file_obj=io.StringIO(private_key))
                    self.add_ssh_key(username, key_name, private_key, public_key)
                    self.notify_expiry()
                    self.notify_pin_expiry()
                except paramiko.ssh_exception.PasswordRequiredException:
                    is_password_protected = True
                    try:
                        if is_password_protected:
                            print(colored("[*] The private key is Password-Protected!", "magenta"))
                            passphrase = getpass.getpass(colored("[*] Private key passphrase: ", "yellow"))
                            re_enter = getpass.getpass(colored("[*] Re-Enter passphrase: ", "yellow"))
                            if re_enter != passphrase:
                                print(colored("[-] Passphrase did not match! QUITTING!", "red"))
                                continue
                            else:
                                key = paramiko.RSAKey(file_obj=io.StringIO(private_key), password=passphrase)
                        else:
                            key = paramiko.RSAKey(file_obj=io.StringIO(private_key))
                    except Exception as e:
                        print(colored(f"[-] Error: {e}", "red"))
                    else:
                        self.add_ssh_key(username, key_name, private_key, public_key, passphrase)
                        self.notify_expiry()
                        self.notify_pin_expiry()
            elif choice == 'get_ssh_key':
                try:
                    try:
                        key_id = int(input(colored("[*] Key ID: ", "yellow")))
                    except ValueError:
                        print(colored("[-] Invalid Key ID", "red"))
                        continue
                    with open(SSH, 'r') as file:
                        data = json.load(file)
                    key_found = False
                    for entry in data:
                        if entry['key_id'] == key_id:
                            key_found = True
                            print(colored(f"[+] Username: {colored(self.decrypt_information(entry.get('username')), 'green')}", "yellow"))
                            print(colored(f"[+] Key Name: {colored(self.decrypt_information(entry.get('key_name')), 'green')}", "yellow"))
                            private_key_lines = self.get_private_ssh_key(key_id)
                            if private_key_lines is not None:
                                print(colored("[+] Private Key:", "yellow"))
                                formatted_private_key = ''.join(private_key_lines)
                                print(colored(formatted_private_key, "green"))
                            else:
                                print(colored("[-] Private Key not found!", "red"))
                            public_key_lines = self.get_public_ssh_key(key_id)
                            if public_key_lines is not None:
                                print(colored("\n[+] Public Key:", "yellow"))
                                formatted_public_key = ''.join(public_key_lines)
                                print(colored(formatted_public_key, "green"))
                            else:
                                print(colored("[-] Public Key not found!", "red"))
                            decrypted_passphrase = self.get_passphrase_private_ssh_key(key_id)
                            if decrypted_passphrase is not None:
                                print(colored(f"\n[+] Passphrase: {colored(decrypted_passphrase, 'green')}", "yellow"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                            else:
                                print(colored("[-] Passphrase not found!", "red"))
                                self.notify_expiry()
                                self.notify_pin_expiry()
                    if not key_found:
                        print(colored(f"[-] This Key ID {key_id} is not available in your vault.", "red"))
                except FileNotFoundError:
                    print(colored("[-] No SSH Key have been saved. Retrieve SSH Key failed!", "red"))
            elif choice == 'del_ssh_key':
                self.delete_ssh_key()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'ch_platform_passwd':
                try:
                    acc_id = int(input(colored("[*] Account ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid Account ID", "red"))
                    continue
                self.change_password(acc_id)
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'ch_card_pin':
                try:
                    card_id = int(input(colored("[*] Card ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid Card ID!", "red"))
                    continue
                self.change_pin(card_id)
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'ch_ssh_key':
                try:
                    key_id = int(input(colored("[*] Key ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid Key ID", "red"))
                    continue
                self.change_ssh_key(key_id)
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'enable2fa':
                with open(USER_DATA_FILE, 'r') as file:
                    user_data = json.load(file)
                if user_data.get('2fa_enabled', False):
                    print(colored("[-] 2FA is already enabled for this user.", "red"))
                    continue
                verify = input(colored("[*] After this, you will need to provide the 6-digit code before you can successfully logged in to your vault. Are you sure you want to proceed? (y/N): ", "yellow"))
                if verify == 'y':
                    self.enable_2fa()
                    self.notify_expiry()
                    self.notify_pin_expiry()
                else:
                    print(colored("[-] Abort!", "red"))
            elif choice == 'show_passwd_exp':
                self.show_expiry_status()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'show_pin_exp':
                self.show_pin_expiry_status()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'show_priv_note':
                self.show_priv_note_status()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'show_src_code':
                self.show_src_code_status()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'show_ssh_key':
                self.show_ssh_key()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'show_passwd_strength':
                self.show_passwd_strength()
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'reset':
                caution = input(colored("[*] Caution: After attempting to do reset, all of the data including your passwords and your master user in mira will be deleted permanently! Are you sure that you want to proceed? (y/N): ", "yellow"))
                if caution == 'y':
                    master_password = getpass.getpass(colored("Master Password: ", "yellow"))
                    if master_password is None:
                        print(colored("[-] Incorrect current master password. Reset procedure failed!", "red"))
                        continue
                    with open(USER_DATA_FILE, 'r') as file:
                        user_data = json.load(file)
                    stored_master_password = self.decrypt_password((base64.b64decode(user_data.get('9034374927023', ''))).decode())
                    try:
                        self.ph.verify(stored_master_password, master_password + user_data.get('2104941992374', ''))
                    except VerifyMismatchError:
                        print(colored("[-] Incorrect current master password. Reset procedure failed!", "red"))
                        continue
                    if os.path.exists(LOCKOUT_FILE):
                        os.remove(LOCKOUT_FILE)
                    else:
                        pass
                    if os.path.exists(PASSFILE):
                        os.remove(PASSFILE)
                    else:
                        pass
                    if os.path.exists(CARD_PIN_FILE):
                        os.remove(CARD_PIN_FILE)
                    else:
                        pass
                    if os.path.exists(API):
                        os.remove(API)
                    else:
                        pass
                    if os.path.exists(PRIVNOTE):
                        os.remove(PRIVNOTE)
                    else:
                        pass
                    if os.path.exists(SSH):
                        os.remove(SSH)
                    else:
                        pass
                    os.remove(USER_DATA_FILE)
                    print(colored("[+] All data has been successfully removed.", "green"))
                    start_again = input(colored("[*] Do you want to start a new account? (y/N): ", "yellow"))
                    if start_again == 'y':
                        username = input(colored("[*] New Username: ", "yellow"))
                        registration = True
                        while registration:
                            master_password = getpass.getpass(colored("[*] New Master Password: ", "yellow"))
                            re_enter = getpass.getpass(colored("[*] Re-enter Master Password: ", "yellow"))
                            if re_enter != master_password:
                                print(colored("[-] Master Password Did Not Match! Please try again!", "red"))
                                continue
                            else:
                                show_password_option = input(colored("[*] Do you want to show the master password? (y/N): ", "yellow"))
                                if show_password_option.lower() == 'y':
                                    print(colored(f"[**] Master Password: {master_password}", "magenta"))
                                    confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "yellow"))
                                    if confirm_password_option.lower() == 'n':
                                        print(colored("[**] Please enter a new master password.", "magenta"))
                                        continue
                                    elif confirm_password_option.lower() == 'y':
                                        self.register(username, master_password)
                                        registration = False
                                        prompt = False
                                    else:
                                        print(colored("[-] Invalid Option!", "red"))
                                        registration = False
                                        prompt = False
                                elif show_password_option.lower() == 'n':
                                    self.register(username, master_password)
                                    registration = False
                                    prompt = False
                                else:
                                    print(colored("[-] Invalid Option!", "red"))
                                    registration = False
                                    prompt = False
                    else:
                        print(colored("[-] Abort.", "red"))
                        break
                else:
                    print(colored("[-] Abort.", "red"))
                    continue
            elif choice == 'add_api_key':
                platform = input(colored("[*] Platform: ", "yellow"))
                if not validators.url(platform):
                    print(colored("[-] The platform you've entered is Invalid! Please make sure that it's in URL form.", "red"))
                    continue
                key_name = input(colored("[*] Key Name: " , "yellow"))
                if not key_name:
                    print(colored("[-] No key name provided! QUITTING!", "red"))
                    continue
                key = getpass.getpass(colored("[*] API Key: ", "yellow"))
                if not key:
                    print(colored("[-] No key provided! QUITTING!", "red"))
                    continue
                self.add_key(platform, key_name, key)
                self.notify_expiry()
                self.notify_pin_expiry()
            elif choice == 'add_card_pin':
                card_type = input(colored("[*] Card Type: ", "yellow")).lower()
                if card_type != 'debit' and card_type != 'credit':
                    print(colored("[-] Please specify if Debit or Credit.", "red"))
                    continue
                try:
                    card_number = input(colored("[*] Card Number: ", "yellow"))
                    if not card_number:
                        print(colored("[-] No card number provided! QUITTING!", "red"))
                        continue
                    if card_number.isdigit() and len(card_number) == 16:
                        pin = getpass.getpass(colored("[*] Card PIN: ", "yellow"))
                        if not pin:
                            print(colored("[-] No PIN provided! QUITTING!", "red"))
                            continue
                        digits = [char for char in pin if char.isdigit()]
                        num_digits = len(digits)
                        if pin.isdigit() and len(pin) in (4, 6):
                            re_enter = getpass.getpass(colored("[*] Re-Enter Card PIN: ", "yellow"))
                            if not re_enter:
                                print(colored("[-] Re-Enter your PIN! QUITTING!", "red"))
                                continue
                            if re_enter != pin:
                                print(colored("[-] PIN did not match. QUITTING!", "red"))
                                continue
                            self.add_card_pin(card_type, card_number, pin)
                            self.notify_expiry()
                            self.notify_pin_expiry()
                        else:
                            print(colored(f"[-] Typical length of PINs ranges from 4 to 6 digits, the length of the PIN that you've entered has {num_digits} digits.", "red"))
                    else:
                        print(colored("[-] Invalid Account Number! Account Numbers should be 16-digits", "red"))
                except ValueError:
                    print(colored("[-] No Account Number provided. QUTTING!", "red"))
                    continue
            elif choice == 'show_loggings':
                self.show_loggings()
            elif choice == 'get_api_key':
                try:
                    acc_id = int(input(colored("[*] Account ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid Account ID.", "red"))
                    continue
                decrypted_key = self.get_key(acc_id)
                try:
                    with open(API, 'r') as file:
                        data = json.load(file)
                    for entry in data:
                        if decrypted_key is not None:
                            print(colored(f"[+] Platform: {entry.get('platform')}", "green"))
                            print(colored(f"[+] Keyname: {self.decrypt_information(entry.get('key_name'))}", "green"))
                            print(colored(f"[+] API Key: {decrypted_key}", "green"))
                        else:
                            print(colored("[-] API Key not found. QUITTING!", "red"))
                except FileNotFoundError:
                    print(colored("[-] API Key not found. QUITTING!", "red"))
                    continue
            elif choice == 'get_card_pin':
                try:
                    card_id = int(input(colored("[*] Card ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid Card ID!", "red"))
                    continue
                decrypted_pin = self.get_card_pin(card_id)
                try:
                    with open(CARD_PIN_FILE, 'r') as file:
                        data = json.load(file)
                    if card_id not in [entry['card_id'] for entry in data]:
                        print(colored(f"f[-] This card type {card_id} is not available in your vault.", "red"))
                    else:
                        for entry in data:
                            if entry['card_id'] == card_id:
                                expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S") if 'expiry_at' in entry else None
                                if expiry_date and datetime.now() > expiry_date:
                                    response = input(colored("[*] Card PIN has expired. Do you want to update the PIN or delete the card details? (U/D): ", "yellow")).lower()
                                    if response == 'u':
                                        new_pin = getpass.getpass(colored("[*] New Card PIN: ", "yellow"))
                                        re_enter = getpass.getpass(colored("[*] Re-Enter New Card PIN: ", "yellow"))
                                        if re_enter != new_pin:
                                            print(colored("[-] PIN did not match. QUITTING!", "red"))
                                            continue
                                        if any(self.decrypt_information(entry['pin']) == new_pin for entry in data):
                                            print(colored("[-] Card PIN has been used, avoid reusing PINs. QUITTING!!", "red"))
                                            continue
                                        entry['pin'] = self.encrypt_information(new_pin)
                                        entry['expiry_at'] = (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d %H:%M:%S')
                                        with open(CARD_PIN_FILE, 'w') as file:
                                            json.dump(data, file, indent=4)
                                        decrypted_pin = self.decrypt_information(entry['pin'])
                                        if decrypted_pin:
                                            print(colored("[+] Card PIN Update Successfully!", "green"))
                                        else:
                                            print(colored("[-] Card PIN update failed.", "red"))
                                        continue
                                    elif response == 'd':
                                        caution = input(colored("[*] Caution: Once you remove it, it will be permanently deleted from your system. Are you sure you want to proceed? (y/N): ", "yellow"))
                                        if caution == 'n':
                                            print(colored("[-] Abort.", "red"))
                                            continue
                                        elif caution == 'y':
                                            data = [e for e in data if not (e['card_id'] == card_id)]
                                            with open(CARD_PIN_FILE, 'w') as file:
                                                json.dump(data, file, indent=4)
                                            print(colored("[+] Card details permanently deleted.", "green"))
                                        continue
                                else:
                                    if decrypted_pin is not None:
                                        print(colored(f"[+] Card Type: {entry.get('card_type')}", "green"))
                                        print(colored(f"[+] Card Number: {self.decrypt_information(entry.get('card_number'))}", "green"))
                                        print(colored(f"[+] Card PIN: {decrypted_pin}", "green"))
                                    else:
                                        print(colored("[-] Card PIN not found. QUITTING!", "red"))
                except FileNotFoundError:
                    print(colored("[-] No card details have been saved. ", "red"))
            elif choice == 'ch_api_key':
                try:
                    acc_id = int(input(colored("[*] Account ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid Account ID!", "red"))
                    continue
                self.change_key(acc_id)
            elif choice == 'mnemonic_enc_key':
                encryption_key = input(colored("[*] Key: ", "yellow"))
                if not encryption_key:
                    print("[-] No encryption key provided!", "red")
                    continue
                try:
                    encryption_key = encryption_key.replace('-', '+').replace('_', '/')
                    key = base64.b64decode(encryption_key)
                    hex_key = key.hex()
                    mnemonic = Mnemonic("english")
                    mnemonic_phrase = mnemonic.to_mnemonic(bytes.fromhex(hex_key))
                    print(colored(f"[+] Mnemonic Phrase: {mnemonic_phrase}", "green"))
                    print(colored(f"[*] It's advisable to write this phrases on a paper or memorize it if you can.", "yellow"))
                    continue
                except ValueError:
                    print(colored("[-] The key you provided is not acceptable. Make sure that it's in the correct format.", "red"))
            elif choice == 'dec_mnemonic':
                mnemonic_phrase = input(colored("[*] Mnemonic Phrase: ", "yellow"))
                if not mnemonic_phrase:
                    print(colored("[-] No mnemonic phrase provided!", "red"))
                    continue
                try:
                    mnemonic = Mnemonic("english")
                    key_bytes = mnemonic.to_entropy(mnemonic_phrase)
                    key_base64 = base64.b64encode(key_bytes).decode()
                    encryption_key = key_base64.replace('+', '-').replace('/', '_')
                    print(colored(f"[+] Encryption Key: {encryption_key}", "green"))
                    continue
                except ValueError:
                    print(colored("[-] Insufficient number of words!", "red"))
                    continue
            elif choice == 'lout':
                self.logout()
                break
            elif choice == 'h' or choice == 'help':
                print(colored("""[**] Available Commands:
1. Adding Credentials
    'add_platform_passwd' - Add a new password
    'add_api_key' - Add a new API key
    'add_card_pin' - Add a new PIN
    'add_ssh_key' - Add a new SSH Key
    'add_src_code' - Add a new Source Code
    'add_priv_note' - Add a new Private Note
2. Retrieving Credentials
    'get_platform_passwd' - Retrieve the plaintext version of the password for the desired account ID
    'get_api_key' - Retrieve the plaintext version of the key of the desired account ID
    'get_card_pin' - Retrieve the plaintext version of the PIN for the desired card ID
    'get_ssh_key' - Retrieve the plaintext version of the SSH Key for the desired key ID
    'get_src_code' - Retrieve the plaintext version of the Source Code for the desired code ID
    'get_priv_note' - Retrieve the plaintext version of the Private Note for the desired note ID
3. Deleting Credentials
    'del_platform_passwd' - Delete a saved password according to your desired account ID
    'del_api_key' - Delete key according to your desired account ID
    'del_card_pin' - Delete a saved PIN according to your desired card ID
    'del_ssh_key' - Delete a saved SSH Key according to your desired key ID
    'del_src_code' - Delete a saved Source Code according to your desired code ID
    'del_priv_note' - Delete a saved Private Note according to your desired note ID
4. Changing Credentials
    'ch_platform_pass' - Change the password for the desired account ID
    'ch_card_pin' - Change the password for the desired pin ID
    'ch_api_key' - Change the API Key for the desired account ID
    'ch_ssh_key' - Chabge the SSH Key for the desired key ID
    'ch_src_code' - Change the Source Code for the desired code ID
    'ch_priv_note' - Change the Private Note for the desired note ID
5. Security and Configuration
    'enable2fa' - Enable Two-Factor Authentication for added security
    'genpasswd' - Generate a strong password
    'changemaster' - Change the masterkey
6. Listing and Analysis
    'show_passwd_exp' - List the usernames and their status on a specific platform or all
    'show_pin_exp' - List the card numbers and their status on a specific card type or all
    'show_api_key' - List the available API Key with their Key ID, Platform, Key Name, and their date when they were added (No Expiry when it comes to API Keys)
    'show_ssh_key' - List the available SSH Key with their Key ID, Username, Key Name and their date when they were added (No Expiry when it comes to SSH Keys)
    'show_src_code' - List the available Source Code with their Code ID, File Name, and their date when they were added (No Expiry when it comes to Source Code)
    'show_priv_note' - List the available Private Note with their note ID, Title, and when they were added (No Expiry when it comes to Private Notes)
    'show_passwd_strength' - List the strength of the password of a username on a specific platform
    'show_loggings' - List all the previous logins.
7. Securing Encryption Key
    'mnemonic_enc_key' - Convert the encryption key to a mnemonic phrase (Only applicable for encryption key that has no underscore and hyphen).
    'dec_mnemonic' - Decode a mnemonic phrase to the original encryption key
8. User Actions
    'lout' - Logout
    'exit' - Terminate MIRA
    'reset' - Delete all data, including the user account permanently (Be cautious with this command! It can result in permanent data loss!)

[**] Security Recommendations: 
- Regularly check for password expiration using the Listing and Analysis commands above.
- Keep your master password and encryption key secure.
- Enable Two-Factor Authentication for an additional layer of security.
- Mira operates on a Zero-Knowledge basis, which means that the security of your account relies solely on the strength and secrecy of your master password, without any involvement from the service provider. So, it's essential not to compromise your account's security with careless actions. Don't be a bitch!

[**] Note: Master Password strength policy requires at least 15 characters with uppercase, numbers, and special characters. (Mandatory).
[**] Note: Password strength policy for platforms requires at least 10 characters with uppercase, numbers, and special characters also. (Optional, but we recommend you to follow our password policy.) """, "cyan"))
            elif choice == 'exit':
                print(colored("[*] MIRA Terminated!", "red"))
                sys.exit()
            elif choice == 'clear':
                clear_terminal()
            elif choice == 'about':
                clear_terminal()
                print(colored(wolf, "blue"))
                print(colored(about, "cyan"))
            else:
                print(colored("[-] Invalid Option", "red"))
    def check_username_reuse(self, new_website, new_username, existing_data):
        for entry in existing_data:
            existing_website = entry['website']
            existing_username = self.decrypt_information(entry['username'])
            if existing_website == new_website and existing_username == new_username:
                return True
        return False
    def check_email_reuse(self, new_email, existing_data):
        for entry in existing_data:
            decrypted_email = self.decrypt_information(entry['email_address'])
            if decrypted_email == new_email:
                user_input = input(colored(f"[*] The email '{new_email}' already exists. Do you want to proceed? (y/N): ", "yellow"))
                if user_input.lower() == 'y':
                    return True
                else:
                    return False
        return False
    def check_password_reuse(self, new_password, existing_data):
        for entry in existing_data:
            decrypted_password = self.decrypt_password(entry['password'])
            if decrypted_password == new_password:
                return True
        return False
    def validate_phone_number(self, phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number)
            return phonenumbers.is_valid_number(parsed_number)
        except phonenumbers.phonenumberutil.NumberParseException:
            return False
    def add_password(self, website, email_address, username, password):
        if not os.path.exists(PASSFILE):
            data = []
        else:
            try:
                with open(PASSFILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        for entry in data:
            decrypted_email = self.decrypt_information(entry['email_address/phone'])
            if decrypted_email == email_address:
                user_input = input(colored(f"[*] The email/phone {email_address} already exists. Do you want to proceed? (y/N): ", "yellow")).lower()
                if user_input == 'y':
                    print(colored("[**] It's advisable not to use the same email/phone for another account.", "cyan"))
                    pass
                else:
                    return
        if self.check_username_reuse(website, username, data):
            print(colored(f"[-] The username {username} already exists for this platform!", "red"))
            return
        if self.check_password_reuse(password, data):
            print(colored("[-] Password has been used to other platforms. (Password not added) Avoid using the same password on other platforms!!", "red"))
            return
        salt = token_bytes(16)
        if self.check_password_strength(password):
            unique_id = int(uuid.uuid4().hex[:4],  16)
            encrypted_website = self.encrypt_information(website)
            encrypted_password = self.encrypt_password(password)
            encrypted_email = self.encrypt_information(email_address)
            encrypted_username = self.encrypt_information(username)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            password_entry = {
                'account_id': unique_id,
                'website': encrypted_website,
                'email_address/phone': encrypted_email,
                'username': encrypted_username,
                'password': encrypted_password,
                'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'expiry_at': (datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')

            }
            data.append(password_entry)
            with open(PASSFILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored(f"[+] Password added! Account ID for this account: {unique_id}", "green"))
        else:
            print(colored("[-] Password not added. Please choose a stronger password.", "red"))
    def get_password(self, i_d):
        if not os.path.exists(PASSFILE):
            return None
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
        for entry in data:
            if entry['account_id'] == i_d and entry.get('email_address/phone') and entry.get('username'):
                decrypted_website = self.decrypt_information(entry['website'])
                decrypted_email = self.decrypt_information(entry['email_address/phone'])
                decrypted_username = self.decrypt_information(entry['username'])
                if 'expiry_at' in entry and entry['expiry_at']:
                    expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                    if datetime.now() > expiry_date:
                        return None
                decrypted_password = self.decrypt_password(entry['password'])
                return decrypted_password
        return None
    def delete_password(self):
        try:
            acc_id = int(input(colored("[*] Account ID: ", "yellow")))
        except ValueError:
            print(colored("[-] Invalid Account ID", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "yellow"))
        if not os.path.exists(PASSFILE):
            print(colored("[-] No passwords saved. Deletion failed!", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        stored_master_password = user_data['master_password']
        salt = user_data['salt']
        try:
            self.ph.verify(stored_master_password, master_pass + salt)
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Delete password failed!", "red"))
            return
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['account_id'] == acc_id and entry.get('email_address/phone') and entry.get('username')), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(PASSFILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] Password deleted successfully!", "green"))
            if not data:
                os.remove(PASSFILE)
                return
        else:
            print(colored("[-] Password not found! Deletion failed!", "red"))
    def change_password(self, acc_id):
        data = []
        if not os.path.exists(PASSFILE):
            print(colored("[-] No passwords saved!", "red"))
            return
        try:
            with open(PASSFILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            pass
        account_entry = next((entry for entry in data if entry['account_id'] == acc_id), None)
        if account_entry:
            username = self.decrypt_information(account_entry['username'])
            current_password = getpass.getpass(colored(f"[*] Current password for the given account ID (Usn: {username}): ", "yellow"))
        else:
            print(colored("[-] This account ID is not available in your vault.", "red"))
            return
        decrypted_password = self.get_password(acc_id)
        if decrypted_password is not None and current_password == decrypted_password:
            new_password = getpass.getpass(colored("[*] New Password: ", "yellow"))
            re_enter = getpass.getpass(colored("[*] Re-Enter New Password: ", "yellow"))
            if not self.check_password_strength(new_password):
                return
            if new_password != re_enter:
                print(colored("[-] New Passwords Did Not Match! Change password failed!", "red"))
                return
            encrypted_new_password = self.encrypt_password(new_password)
            if any(self.decrypt_password(entry['password']) == new_password for entry in data):
                print(colored("[-] Password has been used. (Change password failed) Avoid reusing passwords!", "red"))
                return
            try:
                with open(PASSFILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            for entry in data:
                if entry['account_id'] == acc_id:
                    entry['password'] = encrypted_new_password
                    entry['expiry_at'] = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
                    with open(PASSFILE, 'w') as file:
                        json.dump(data, file, indent=4)
                    decrypted_password = self.decrypt_password(entry['password'])
                    if decrypted_password:
                        print(colored("[+] Password updated successfully!", "green"))
                    else:
                        print(colored("[-] Password update failed.", "red"))
                    return
        else:
            print(colored("[-] Incorrect current password. Change password failed!", "red"))
    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode()).decode()
    def decrypt_password(self, encrypted_password):
        return self.cipher.decrypt(encrypted_password.encode()).decode()
    def change_master_password(self):
        current_password = getpass.getpass(colored("[*] Current Master Password: ", "yellow"))
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        stored_master_password = self.decrypt_password((base64.b64decode(user_data.get('9034374927023', ''))).decode())
        try:
            self.ph.verify(stored_master_password, current_password + user_data.get('2104941992374', ''))
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Change password failed!", "red"))
            return
        while True:
            new_password = getpass.getpass(colored("[*] New Master Password: ", "yellow"))
            re_enter = getpass.getpass(colored("[*] Re-Enter Master Password: ", "yellow"))
            if new_password != re_enter:
                print(colored("[-] New Master Password Did Not Match! Please try again!", "red"))
                continue
            else:
                show_password_option = input(colored("[*] Do you want to show the new master password for verification? (y/N): ", "yellow"))
                if show_password_option.lower() == 'y':
                    print(colored(f"[**] New Master Password: {new_password}", "magenta"))
                    confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "yellow"))
                    if confirm_password_option.lower() == 'n':
                        print(colored("[**] Please enter a new master password.", "magenta"))
                        continue
                    elif confirm_password_option.lower() == 'y':
                        if not self.check_master_password_strength(new_password):
                            break
                        fernet = Fernet(encryption_key) 
                        salt = user_data['2104941992374']
                        hashed_new_master_password = self.ph.hash(new_password + salt)
                        encrypted_master_password = fernet.encrypt(hashed_new_master_password.encode())
                        encrypted_new_master_password_b64 = base64.b64encode(encrypted_master_password).decode()
                        user_data['9034374927023'] = encrypted_new_master_password_b64
                        with open(USER_DATA_FILE, 'w') as file:
                            json.dump(user_data, file)
                        self.master_password = new_password
                        print(colored("[+] Master Password changed successfully!", "green"))
                        break
                    else:
                        print(colored("[-] Invalid Option!", "red"))
                        break
                elif show_password_option.lower() == 'n':
                    if not self.check_master_password_strength(new_password):
                        break
                    fernet = Fernet(encryption_key) 
                    salt = user_data['2104941992374']
                    hashed_new_master_password = self.ph.hash(new_password + salt)
                    encrypted_master_password = fernet.encrypt(hashed_new_master_password.encode())
                    encrypted_new_master_password_b64 = base64.b64encode(encrypted_master_password).decode()
                    user_data['9034374927023'] = encrypted_new_master_password_b64
                    with open(USER_DATA_FILE, 'w') as file:
                        json.dump(user_data, file)
                    self.master_password = new_password
                    print(colored("[+] Master Password changed successfully!", "green"))
                    break
                else:
                    print(colored("[-] Invalid Option!", "red"))
                    break
    def check_keyname_reuse(self, new_platform, new_key_name, existing_data):
        for entry in existing_data:
            existing_platform = entry['platform']
            existing_key_name = self.decrypt_information(entry['key_name'])
            if existing_platform == new_platform and existing_key_name == new_key_name:
                return True
        return False
    def check_key_reuse(self, new_key, existing_data):
        for entry in existing_data:
            decrypted_key = self.decrypt_information(entry['key'])
            if decrypted_key == new_key:
                return True
        return False
    def add_key(self, platform, key_name, key):
        if not os.path.exists(API):
            data = []
        else:
            try:
                with open(API, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_keyname_reuse(platform, key_name, data):
            print(colored(f"[-] The key name {key_name} already exists for this Platform!", "red"))
            return
        if self.check_key_reuse(key, data):
            print(colored("[-] API Key has been used to other Key Name. (API Key not added) Avoid using the same API on other Key Name!!", "red"))
            return
        unique_id = int(uuid.uuid4().hex[:4],  16)
        api_key_entry = {
            'unique_id': unique_id,
            'platform': platform,
            'key_name': self.encrypt_information(key_name),
            'key': self.encrypt_information(key),
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(api_key_entry)
        with open(API, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] API Key added! Account ID for this API Key: {unique_id}", "green"))
    def check_cardnumber_reuse(self, new_card_type, new_card_number, existing_data):
        for entry in existing_data:
            existing_card_type = entry['card_type']
            existing_card_number = self.decrypt_information(entry['card_number'])
            if existing_card_type == new_card_type and existing_card_number == new_card_number:
                return True
        return False
    def check_pin_reuse(self, new_pin, existing_data):
        for entry in existing_data:
            decrypted_pin = self.decrypt_information(entry['pin'])
            if decrypted_pin == new_pin:
                return True
        return False
    def add_card_pin(self, card_type, card_number, pin):
        if not os.path.exists(CARD_PIN_FILE):
            data = []
        else:
            try:
                with open(CARD_PIN_FILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_cardnumber_reuse(card_type, card_number, data):
            print(colored(f"[-] The card number {card_number} already exists for this card type!", "red"))
            return
        if self.check_pin_reuse(pin, data):
            print(colored("[-] PIN has been used to other card number. (PIN not added) Avoid using the same PIN on other card numbers!!", "red"))
            return
        unique_id = int(uuid.uuid4().hex[:4],  16)
        card_pin_entry = {
            'card_id': unique_id,
            'card_type': card_type,
            'card_number': self.encrypt_information(card_number),
            'pin': self.encrypt_information(pin),
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'expiry_at': (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(card_pin_entry)
        with open(CARD_PIN_FILE, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] Card PIN added! Card ID for this PIN: {unique_id}", "green"))
    def get_key(self, acc_id):
        if not os.path.exists(API):
            return None
        try:
            with open(API, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['unique_id'] == acc_id:
                decrypted_key_name = self.decrypt_information(entry['key_name'])
                decrypted_key = self.decrypt_information(entry['key'])
                return decrypted_key
        return None
    def get_card_pin(self, card_id):
        if not os.path.exists(CARD_PIN_FILE):
            return None
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['card_id'] == card_id:
                decrypted_pin = self.decrypt_information(entry['pin'])
                return decrypted_pin
        return None
    def delete_card_pin(self):
        try:
            card_id = int(input(colored("[*] Card ID: ", "yellow")))
        except ValueError:
            print(colored("[-] Invalid Card ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "yellow"))
        if not os.path.exists(CARD_PIN_FILE):
            print(colored("[-] No PIN saved. Deletion failed!", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        stored_master_password = user_data['master_password']
        salt = user_data['salt']
        try:
            self.ph.verify(stored_master_password, master_pass + salt)
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            return
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['card_id'] == card_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(CARD_PIN_FILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] Card PIN deleted successfully!", "green"))
            if not data:
                os.remove(CARD_PIN_FILE)
                return
        else:
            print(colored("[-] PIN not found! Deletion failed!", "red"))
    def delete_key(self):
        try:
            acc_id = int(input(colored("[*] Account ID: ", "yellow")))
        except ValueError:
            print(colored("[-] Invalid Account ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "yellow"))
        if not os.path.exists(API):
            print(colored("[-] No API Keys saved. Deletion failed", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        stored_master_password = user_data['master_password']
        salt = user_data['salt']
        try:
            self.ph.verify(stored_master_password, master_pass + salt)
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            return
        try:
            with open(API, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['unique_id'] == acc_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(API, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] API Key successfully deleted!", "green"))
            if not data:
                os.remove(API)
                return
        else:
            print(colored("[-] API Key not found! Deletion failed!", "red"))
    def change_pin(self, card_id):
        data = []
        if not os.path.exists(CARD_PIN_FILE):
            print(colored("[-] No PIN saved!", "red"))
            return
        try:
            with open(CARD_PIN_FILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            pass
        pin_entry = next((entry for entry in data if entry['card_id'] == card_id), None)
        if pin_entry:
            card_number = self.decrypt_information(pin_entry['card_number'])
            current_pin = getpass.getpass(colored(f"[*] Current PIN for the given card ID (No: {card_number}): ", "yellow"))
        else:
            print(colored(f"[-] This Card ID {card_id} is not available on your PIN vault.", "red"))
            return
        decrypted_pin = self.get_card_pin(card_id)
        if decrypted_pin is not None and current_pin == decrypted_pin:
            try:
                new_pin = getpass.getpass(colored("[*] New PIN: ", "yellow"))
                digits = [char for char in new_pin if char.isdigit()]
                num_digits = len(digits)
                if new_pin.isdigit() and len(new_pin) not in (4, 6):
                    print(colored(f"[-] Typical length of PINs ranges from 4 to 6 digits! The PIN you've entered has {num_digits} digits.", "red"))
                    return
                if not new_pin:
                    print(colored("[-] No PIN provided! Changing process failed.", "red"))
                    return
                new_pin_input = int(new_pin)
                re_enter = getpass.getpass(colored("[*] Re-Enter New PIN: ", "yellow"))
                if not re_enter:
                    print(colored("[-] Please Re-Enter your new PIN! QUITTING!", "red"))
                    return
                re_enter_input = int(re_enter)
            except ValueError:
                print(colored("[-] Please provide a PIN", "red"))
                return
            if new_pin_input != re_enter_input:
                print(colored("[-] New PINs Did Not Match! Change PIN failed!", "red"))
                return
            encrypted_new_pin = self.encrypt_information(new_pin)
            if any(self.decrypt_information(entry['pin']) == new_pin for entry in data):
                print(colored("[-] PIN has been used. (Change PIN failed) Avoid reusing PINs!", "red"))
                return
            try:
                with open(CARD_PIN_FILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            for entry in data:
                if entry['card_id'] == card_id:
                    entry['pin'] = encrypted_new_pin
                    entry['expiry_at'] = (datetime.now() + timedelta(days=60)).strftime('%Y-%m-%d %H:%M:%S')
                    with open(CARD_PIN_FILE, 'w') as file:
                        json.dump(data, file, indent=4)
                    decrypted_pin = self.decrypt_information(entry['pin'])
                    if decrypted_pin:
                        print(colored("[+] PIN updated successfully!", "green"))
                    else:
                        print(colored("[-] PIN update failed.", "red"))
                    return
        else:
            print(colored("[-] Incorrect current PIN. Change PIN failed!", "red"))
    def change_key(self, acc_id):
        data = []
        if not os.path.exists(API):
            print(colored("[-] No KEYS saved!", "red"))
            return
        try:
            with open(API, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            pass
        account_entry = next((entry for entry in data if entry['account_id'] == acc_id), None)
        if account_entry:
            keyname = self.decrypt_information(account_entry['key_name'])
            current_key = getpass.getpass(colored(f"[*] Current key for the given account ID (Usn: {keyname}): ", "yellow"))
        else:
            print(colored(f"[-] This account ID {acc_id} is not available in your vault.", "red"))
            return
        decrypted_key = self.get_key(acc_id)
        if decrypted_key is not None and current_key == decrypted_key:
            new_key = getpass.getpass(colored("[*] New API Key: ", "yellow"))
            re_enter = getpass.getpass(colored("[*] Re-Enter New API Key: ", "yellow"))
            if new_key != re_enter:
                print(colored("[-] New API Key Did Not Match! Change Key failed!", "red"))
                return
            encrypted_new_key = self.encrypt_information(new_key)
            if any(self.decrypt_information(entry['key']) == new_key for entry in data):
                print(colored("[-] API Key has been used. (Change Key failed) Avoid reusing Keys!", "red"))
                return
            try:
                with open(API, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            for entry in data:
                if entry['unique_id'] == acc_id:
                    entry['key'] = encrypted_new_key
                    with open(API, 'w') as file:
                        json.dump(data, file, indent=4)
                    decrypted_key = self.decrypt_information(entry['key'])
                    if decrypted_key:
                        print(colored("[+] API Key updated successfully!", "green"))
                    else:
                        print(colored("[-] API Key update failed.", "red"))
                    return
        else:
            print(colored("[-] Incorrect current API Key. Change Key failed!", "red"))
    def check_ssh_keyname_reuse(self, new_username, new_key_name, existing_data):
        for entry in existing_data:
            existing_username = entry['username']
            existing_key_name = entry['key_name']
            if existing_username == new_username and existing_key_name == new_key_name:
                return True
        return False
    def check_ssh_key_reuse(self, public_key, private_key, existing_data):
        for entry in existing_data:
            decrypted_pub_key = self.decrypt_information(entry['public_key'])
            decrypted_priv_key = self.decrypt_information(entry['private_key'])
            if decrypted_pub_key == public_key and decrypted_priv_key == private_key:
                return True
        return False
    def is_valid_ssh_private_key(self, private_key):
        if not private_key.startswith("-----BEGIN OPENSSH PRIVATE KEY-----"):
            return False
    def is_valid_ssh_public_key(self, public_key):
        if not public_key.startswith("ssh-rsa"):
            return False
    def add_ssh_key(self, username, key_name, private_key, public_key, passphrase=None):
        if not os.path.exists(SSH):
            data = []
        else:
            try:
                with open(SSH, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_ssh_keyname_reuse(username, key_name, data):
            print(colored(f"[-] The key name {key_name} already exists for this username!", "red"))
            return
        if self.check_ssh_key_reuse(public_key, private_key, data):
            print(colored("[-] The key has been used to other Key Name. (Both Key not added) Avoid using the same Key on other Key Name!!", "red"))
            return
        unique_id = int(uuid.uuid4().hex[:4],  16)
        ssh_key_entry = {
            'key_id': unique_id,
            'username': self.encrypt_information(username),
            'key_name': self.encrypt_information(key_name),
            'public_key': self.encrypt_information(public_key),
            'private_key': self.encrypt_information(private_key),
            'passphrase': self.encrypt_information(passphrase) if passphrase else 'null',
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(ssh_key_entry)
        with open(SSH, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] SSH Key added! Key ID for that Key: {unique_id}", "green"))
    def get_private_ssh_key(self, key_id):
        if not os.path.exists(SSH):
            return None
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['key_id'] == key_id:
                decrypted_priv_key = self.decrypt_information(entry['private_key'])
                return decrypted_priv_key
        return None
    def get_public_ssh_key(self, key_id):
        if not os.path.exists(SSH):
            return None
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['key_id'] == key_id:
                decrypted_pub_key = self.decrypt_information(entry['public_key'])
                return decrypted_pub_key
        return None
    def get_passphrase_private_ssh_key(self, key_id):
        if not os.path.exists(SSH):
            return None
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['key_id'] == key_id:
                encrypted_passphrase = entry['passphrase']
                if encrypted_passphrase.lower() == 'null':
                    return colored("null", "red")
                else:
                    passphrase = self.decrypt_information(encrypted_passphrase)
                    return passphrase.lower() if passphrase else None
        return None
    def delete_ssh_key(self):
        try:
            key_id = int(input(colored("[*] Key ID: ", "yellow")))
        except ValueError:
            print(colored("[-] Invalid Key ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "yellow"))
        if not os.path.exists(SSH):
            print(colored("[-] No SSH Keys saved. Deletion failed", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        stored_master_password = user_data['master_password']
        salt = user_data['salt']
        try:
            self.ph.verify(stored_master_password, master_pass + salt)
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            return
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['key_id'] == key_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(SSH, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] SSH Key successfully deleted!", "green"))
            if not data:
                os.remove(SSH)
                return
        else:
            print(colored("[-] SSH Key not found! Deletion failed!", "red"))
    def change_ssh_key(self, key_id):
        data = []
        if not os.path.exists(SSH):
            print(colored("[-] No SSH Keys saved!", "red"))
            return
        try:
            with open(SSH, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            pass
        for entry in data:
            if key_id not in [entry['key_id'] for entry in data]:
                print(colored(f"[-] This username {key_id} is not available on your SSH Key vault.", "red"))
                return
        for entry in data:
            if entry['passphrase'] == 'null':
                print(colored(f"[**] This key name '{self.decrypt_information(entry.get('key_name'))}' has no passphrase!", "magenta"))
                pass
            else:
                current_passphrase = getpass.getpass(colored(f"[*] Current Passphrase for verification (Kname: {self.decrypt_information(entry.get('key_name'))}): ", "yellow"))
                decrypted_passphrase = self.decrypt_information(entry['passphrase'])
                if current_passphrase != decrypted_passphrase:
                    print(colored("[-] Incorrect current passphrase!", "red"))
                    return
        try:
            print(colored("[*] Paste the New Private Key Below (Type 'END' on a new line to finish):", "yellow"))
            new_private_key_lines = []
            try:
                while True:
                    line = input()
                    new_private_key_lines.append(line)
                    if line.upper() == "END":
                        break
            except Exception as e:
                print("Error: ", e)
                return
            print(colored("[*] Paste the New Public Key Below (Type 'END' on a new line to finish):", "yellow"))
            new_public_key_lines = []
            try:
                while True:
                    line = input()
                    new_public_key_lines.append(line)
                    if line.upper() == "END":
                        break
            except Exception as e:
                print("Error: ", e)
                return
        except paramiko.ssh_exception.SSHException:
            print(colored("[-] Invalid OpenSSH private key", "red"))
            return
        new_private_key = '\n'.join(new_private_key_lines[:-1])
        new_public_key = '\n'.join(new_public_key_lines[:-1])
        if not new_private_key.startswith("-----BEGIN OPENSSH PRIVATE KEY-----"):
            print(colored("[-] Invalid SSH Private Key!", "red"))
            return
        if not new_public_key.startswith("ssh-rsa"):
            print(colored("[-] Invalid SSH Public Key!", "red"))
            return
        is_password_protected = False
        passphrase = None
        try:
            new_key = paramiko.RSAKey(file_obj=io.StringIO(new_private_key))
            for entry in data:
                if entry['key_id'] == key_id:
                    entry['private_key'] = self.encrypt_information(new_private_key)
                    entry['public_key'] = self.encrypt_information(new_public_key)
                    entry['passphrase'] = 'null'
            with open(SSH, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] SSH Key updated successfully!", "green"))
        except paramiko.ssh_exception.PasswordRequiredException:
            is_password_protected = True
            try:
                if is_password_protected:
                    print(colored("[*] The new private key is Password-Protected!", "magenta"))
                    new_passphrase = getpass.getpass(colored("[*] Enter the new private key passphrase: ", "yellow"))
                    re_enter = getpass.getpass(colored("[*] Re-Enter new private key passphrase: ", "yellow"))
                    if re_enter != new_passphrase:
                        print(colored("[-] New Password did not match. QUITTING!"))
                        return
                    new_key = paramiko.RSAKey(file_obj=io.StringIO(new_private_key), password=new_passphrase)
                else:
                    new_key = paramiko.RSAKey(file_obj=io.StringIO(new_private_key))
            except Exception as e:
                print(colored(f"[-] Error: {e}", "red"))
            except paramiko.ssh_exception.SSHException:
                print(colored("[-] Error: Invalid Private Key!", "red"))
            else:
                for entry in data:
                    if entry['key_id'] == key_id:
                        entry['private_key'] = self.encrypt_information(new_private_key)
                        entry['public_key'] = self.encrypt_information(new_public_key)
                        entry['passphrase'] = self.encrypt_information(new_passphrase)
                with open(SSH, 'w') as file:
                    json.dump(data, file, indent=4)
                print(colored("[+] SSH Key updated successfully!", "green"))
    def check_title_reuse(self, title, existing_data):
        for entry in existing_data:
            decrypted_title = self.decrypt_information(entry['title'])
            if decrypted_title == title:
                return True
        return False
    def add_private_note(self, title, note):
        if not os.path.exists(PRIVNOTE):
            data = []
        else:
            try:
                with open(PRIVNOTE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_title_reuse(title, data):
            print(colored(f"[-] The title {title} already exists", "red"))
            return
        unique_id = int(uuid.uuid4().hex[:4],  16)
        priv_note_entry = {
            'note_id': unique_id,
            'title': self.encrypt_information(title),
            'note': self.encrypt_information(note),
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(priv_note_entry)
        with open(PRIVNOTE, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] Private Note added! Note ID for that Note: {unique_id}", "green"))
    def get_private_note(self, note_id):
        if not os.path.exists(PRIVNOTE):
            return None
        try:
            with open(PRIVNOTE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['note_id'] == note_id:
                decrypted_title = self.decrypt_information(entry['title'])
                decrypted_note = self.decrypt_information(entry['note'])
                return decrypted_note
        return None
    def delete_private_note(self):
        try:
            note_id = int(input(colored("[*] Note ID: ", "yellow")))
        except ValueError:
            print(colored("[-] Invalid Note ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "yellow"))
        if not os.path.exists(PRIVNOTE):
            print(colored("[-] No Private Note saved. Deletion failed", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        stored_master_password = user_data['master_password']
        salt = user_data['salt']
        try:
            self.ph.verify(stored_master_password, master_pass + salt)
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            return
        try:
            with open(PRIVNOTE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['note_id'] == note_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(PRIVNOTE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] Private Note successfully deleted!", "green"))
            if not data:
                os.remove(PRIVNOTE)
                return
        else:
            print(colored("[-] Private Note not found! Deletion failed!", "red"))
    def check_filename_reuse(self, filename, existing_data):
        for entry in existing_data:
            decrypted_filename = self.decrypt_information(entry['filename'])
            if decrypted_filename == filename:
                return True
        return False
    def add_source_code(self, filename, code):
        if not os.path.exists(SRCCODE):
            data = []
        else:
            try:
                with open(SRCCODE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if self.check_filename_reuse(filename, data):
            print(colored(f"[-] The filename {filename} already exists", "red"))
            return
        unique_id = int(uuid.uuid4().hex[:4],  16)
        source_code_entry = {                                                  
            'code_id': unique_id,
            'filename': self.encrypt_information(filename),
            'code': self.encrypt_information(code),
            'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        data.append(source_code_entry)
        with open(SRCCODE, 'w') as file:
            json.dump(data, file, indent=4)
        print(colored(f"[+] Source Code added! Code ID for that Code: {unique_id}", "green"))
    def get_source_code(self, code_id):
        if not os.path.exists(SRCCODE):
            return None
        try:
            with open(SRCCODE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return None
        for entry in data:
            if entry['code_id'] == code_id:
                decrypted_filename = self.decrypt_information(entry['filename'])
                decrypted_code = self.decrypt_information(entry['code'])
                return decrypted_code
        return None
    def delete_source_code(self):
        try:
            code_id = int(input(colored("[*] Code ID: ", "yellow")))
        except ValueError:                                     
            print(colored("[-] Invalid Code ID!", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "yellow"))
        if not os.path.exists(SRCCODE):
            print(colored("[-] No Source Code saved. Deletion failed", "red"))
            return
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        stored_master_password = user_data['master_password']
        salt = user_data['salt']
        try:
            self.ph.verify(stored_master_password, master_pass + salt)
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Deletion failed!", "red"))
            return
        try:
            with open(SRCCODE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['code_id'] == code_id), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(SRCCODE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] Source Code successfully deleted!", "green"))
            if not data:
                os.remove(SRCCODE)
                return
        else:
            print(colored("[-] Source Code not found! Deletion failed!", "red"))
    def encrypt_information(self, information):
        return self.cipher.encrypt(information.encode()).decode()
    def decrypt_information(self, encrypted_information):
        return self.cipher.decrypt(encrypted_information.encode()).decode()
    def logout(self):
        self.master_password = None
        self.cipher = None
        print(colored("[+] Logged out!", "cyan"))
if __name__ == '__main__':
    if platform.system() == 'Linux':
        if not check_linux_privileges():
            print(colored("[-] Mira requires elevated privileges on Linux. QUITTING!", "red"))
            exit()
        else:
            try:
                clear_terminal()
                current_datetime_info = get_current_datetime()
                os_distribution_info = get_os_distribution()
                print(colored(os_distribution_info, "blue"))
                time.sleep(2)
                print(colored(get_python_version(), "blue"))
                time.sleep(2)
                print(colored(current_datetime_info, "blue"))
                time.sleep(2)
                print(colored("[+] Starting Mira Password Manager.....", "blue"))
                password_manager = PasswordManager()
                time.sleep(20)
                if password_manager.lockout_time and time.time() < password_manager.lockout_time:                                         
                    clear_terminal()
                    print(colored(blehhh, "red"))
                    print(colored(f"[-] Account locked. WE'VE ALREADY TOLD YOU THAT WE DON'T ACCEPT SHITTY BUGS HERE! If you are the real user, try again after {int(password_manager.lockout_time - time.time())} seconds.", "red")) 
                    exit()
                clear_terminal()
                print(colored(wolf, "blue"))
                while True:
                    prompt = HTML("<ansiblue>MIRA ~> </ansiblue>")
                    choice = password_manager.session.prompt(prompt)
                    if choice == "":
                        continue
                    elif choice == 'regis':
                        if os.path.exists(USER_DATA_FILE) and os.path.getsize(USER_DATA_FILE) != 0:
                            print(colored("[-] Master user already exists!!", "red"))                                                         
                        else:
                            username = input(colored("[*] New Username: ", "yellow"))
                            registration_successful = False
                            registration_failed = False
                            while not registration_successful and not registration_failed:
                                master_password = getpass.getpass(colored("[*] New Master Password: ", "yellow"))                                     
                                re_enter = getpass.getpass(colored("[*] Re-Enter Master Password: ", "yellow"))                                       
                                if re_enter != master_password:
                                    print(colored("[-] Master Password Did Not Match! Please try again!", "red"))
                                    continue
                                else:
                                    show_password_option = input(colored("[*] Do you want to show the master password? (y/N): ", "yellow"))
                                    if show_password_option.lower() == 'y':
                                        print(colored(f"[**] Master Password: {master_password}", "magenta"))
                                        confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "yellow"))
                                        if confirm_password_option.lower() == 'n':
                                            print(colored("[**] Please enter a new master password.", "magenta"))
                                            continue
                                        elif confirm_password_option.lower() == 'y':
                                            password_manager.register(username, master_password)
                                            registration_successful = True
                                        else:
                                            print(colored("[-] Invalid Option!", "red"))
                                            registration_failed = True
                                    elif show_password_option.lower() == 'n':
                                        password_manager.register(username, master_password)
                                        registration_successful = True
                                    else:
                                        print(colored("[-] Invalid Option!", "red"))
                                        registration_failed = True
                    elif choice == 'log':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. WE'VE ALREADY TOLD YOU THAT WE DON'T ACCEPT SHITTY BUGS HERE! If you are the real user, try again after {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            exit()
                        if os.path.exists(USER_DATA_FILE):
                            username = input(colored("[*] Username: ", "yellow"))
                            master_password = getpass.getpass(colored("[*] Master password: ", "yellow"))
                            encryption_key = getpass.getpass(colored("[*] Encryption key: ", "yellow"))
                            password_manager.login(username, master_password, encryption_key)
                        else:
                            print(colored("[-] You have not registered. Please do that.", "red"))
                    elif choice == 'help' or choice == 'h':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. WE'VE ALREADY TOLD YOU THAT WE DON'T ACCEPT SHITTY BUGS HERE! If you are the real user, try again after {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            exit()
                        print(colored(""""[**] Available Commands:
'log' - Login (Make sure you're registered before attempt to login)
'regis' - Register for new user (Only one user!)
'quit' - Terminate MIRA
'about' - More information about MIRA
'dec_mnemonic' - Decode a mnemonic phrase 
'h' - Help""", "cyan"))
                    elif choice == 'dec_mnemonic':                                                                                                                   
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))                                                                                                                
                            print(colored(f"[-] Account locked. WE'VE ALREADY TOLD YOU THAT WE DON'T ACCEPT SHITTY BUGS HERE! If you are the real user, try again after {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            exit()
                        mnemonic_phrase = input(colored("[*] Mnemonic Phrase: ", "yellow"))
                        if not mnemonic_phrase:
                            print(colored("[-] No mnemomic phrase provided", "red"))
                            continue
                        try:
                            mnemonic = Mnemonic("english")
                            key_bytes = mnemonic.to_entropy(mnemonic_phrase)
                            key_base64 = base64.b64encode(key_bytes).decode()                                                                                            
                            encryption_key = key_base64.replace('+', '-').replace('/', '_')
                            print(colored(f"[+] Encryption Key: {encryption_key}", "green"))
                        except ValueError:
                            print(colored("[-] Insufficient number of words", "red"))
                            continue
                    elif choice == 'quit':
                        print(colored("\n[-] Exiting Mira.....", "red"))
                        time.sleep(3)
                        clear_terminal()
                        print(colored(remember, "cyan"))
                        print(colored("Creating a password is like crafting a witty joke: it should be unique, memorable, and leave hackers scratching their heads. So, don't be shy to sprinkle a dash of humor into your password game – after all, laughter is the best encryption!", "cyan"))
                        sys.exit()
                    elif choice == 'about':
                        clear_terminal()
                        print(colored(wolf, "cyan"))
                        print(colored(about, "cyan"))
                    elif choice == 'clear':
                        clear_terminal()
                    else:
                        print(colored("[-] Invalid Option", "red"))
            except (KeyboardInterrupt, EOFError):
                print(colored("[-] Exiting Mira.....", "red"))
                time.sleep(3)
                clear_terminal()
                print(colored(remember, "cyan"))
                print(colored("Creating a password is like crafting a witty joke: it should be unique, memorable, and leave hackers scratching their heads. So, don't be shy to sprinkle a dash of humor into your password game – after all, laughter is the best encryption!", "cyan"))
                sys.exit()
    elif platform.system() == 'Windows':
        if not check_windows_privileges():
            print(colored("[-] Mira requires elevated privileges on Windows. QUITTING!", "red"))
            exit()
        else:
            try:
                clear_terminal()
                current_datetime_info = get_current_datetime()
                os_distribution_info = get_os_distribution()
                print(colored(os_distribution_info, "blue"))
                time.sleep(2)
                print(colored(get_python_version(), "blue"))
                time.sleep(2)
                print(colored(current_datetime_info, "blue"))
                time.sleep(2)
                print(colored("[+] Starting Mira Password Manager.....", "blue"))
                password_manager = PasswordManager()
                time.sleep(20)
                if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                    clear_terminal()
                    print(colored(blehhh, "red"))
                    print(colored(f"[-] Account locked. WE'VE ALREADY TOLD YOU THAT WE DON'T ACCEPT SHITTY BUGS HERE! If you are the real user, try again after {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                    exit()
                clear_terminal()
                print(colored(wolf, "blue"))
                while True:
                    prompt = HTML("<ansiblue>MIRA ~> </ansiblue>")
                    choice = password_manager.session.prompt(prompt)
                    if choice == "":
                        continue
                    elif choice == 'regis':
                        if os.path.exists(USER_DATA_FILE) and os.path.getsize(USER_DATA_FILE) != 0:
                            print(colored("[-] Master user already exists!!", "red"))
                        else:
                            username = input(colored("[*] New Username: ", "yellow"))
                            registration_successful = False
                            registration_failed = False
                            while not registration_successful and not registration_failed:
                                master_password = getpass.getpass(colored("[*] New Master Password: ", "yellow"))                            
                                re_enter = getpass.getpass(colored("[*] Re-Enter Master Password: ", "yellow"))                              
                                if re_enter != master_password:
                                    print(colored("[-] Master Password Did Not Match! Please try again!", "red"))
                                    continue
                                else:
                                    show_password_option = input(colored("[*] Do you want to show the master password? (y/N): ", "yellow"))
                                    if show_password_option.lower() == 'y':
                                        print(colored(f"[**] Master Password: {master_password}", "magenta"))
                                        confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "yellow"))
                                        if confirm_password_option.lower() == 'n':
                                            print(colored("[**] Please enter a new master password.", "magenta"))
                                            continue
                                        elif confirm_password_option.lower() == 'y':
                                            password_manager.register(username, master_password)
                                            registration_successful = True
                                        else:
                                            print(colored("[-] Invalid Option!", "red"))
                                            registration_failed = True
                                    elif show_password_option.lower() == 'n':
                                        password_manager.register(username, master_password)
                                        registration_successful = True
                                    else:
                                        print(colored("[-] Invalid Option!", "red"))
                                        registration_failed = True
                    elif choice == 'log':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. WE'VE ALREADY TOLD YOU THAT WE DON'T ACCEPT SHITTY BUGS HERE! If you are the real user, try again after {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            exit()
                        if os.path.exists(USER_DATA_FILE):
                            username = input(colored("[*] Username: ", "yellow"))
                            master_password = getpass.getpass(colored("[*] Master password: ", "yellow"))
                            encryption_key = getpass.getpass(colored("[*] Encryption key: ", "yellow"))
                            password_manager.login(username, master_password, encryption_key)
                            password_manager.get_username_log(username)
                        else:
                            print(colored("[-] You have not registered. Please do that.", "red"))
                    elif choice == 'help' or choice == 'h':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. WE'VE ALREADY TOLD YOU THAT WE DON'T ACCEPT SHITTY BUGS HERE! If you are the real user, try again after {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            exit()
                        print(colored(""""[**] Available Commands:
'log' - Login (Make sure you're registered before attempt to login)
'regis' - Register for new user (Only one user!)
'about' - More information about MIRA
'dec_mnemonic' - Decode a mnemonic phrase
'quit' - Terminate MIRA
'h' - Help""", "cyan"))
                    elif choice == 'dec_mnemonic':
                        if password_manager.lockout_time and time.time() < password_manager.lockout_time:
                            clear_terminal()
                            print(colored(blehhh, "red"))
                            print(colored(f"[-] Account locked. WE'VE ALREADY TOLD YOU THAT WE DON'T ACCEPT SHITTY BUGS HERE! If you are the real user, try again after {int(password_manager.lockout_time - time.time())} seconds.", "red"))
                            exit()
                        mnemonic_phrase = input(colored("[*] Mnemonic Phrase: ", "yellow"))
                        if not mnemonic_phrase:
                            print(colored("[-] No mnemonic phrase provided!", "red"))
                            continue
                        try:
                            mnemonic = Mnemonic("english")
                            key_bytes = mnemonic.to_entropy(mnemonic_phrase)
                            key_base64 = base64.b64encode(key_bytes).decode()
                            encryption_key = key_base64.replace('+', '-').replace('/', '_')
                            print(colored(f"[+] Encryption Key: {encryption_key}", "green"))
                        except ValueError:
                            print(colored("[-] Insufficient number of words", "red"))
                            continue
                    elif choice == 'quit':
                        print(colored("[-] Exiting Mira.....", "red"))
                        time.sleep(3)
                        clear_terminal()
                        print(colored(remember, "cyan"))
                        print(colored("Creating a password is like crafting a witty joke: it should be unique, memorable, and leave hackers scratching their heads. So, don't be shy to sprinkle a dash of humor into your password game – after all, laughter is the best encryption!", "cyan"))
                        sys.exit()
                    elif choice == 'about':
                        clear_terminal()
                        print(colored(wolf, "blue"))
                        print(colored(about, "cyan"))
                    elif choice == 'clear':
                        clear_terminal()
                    else:
                        print(colored("[-] Invalid Option", "red"))
            except (KeyboardInterrupt, EOFError):
                print(colored("[-] Exiting Mira.....", "red"))
                time.sleep(3)
                clear_terminal()
                print(colored(remember, "cyan"))
                print(colored("Creating a password is like crafting a witty joke: it should be unique, memorable, and leave hackers scratching their heads. So, don't be shy to sprinkle a dash of humor into your password game – after all, laughter is the best encryption!", "cyan"))
                sys.exit()

