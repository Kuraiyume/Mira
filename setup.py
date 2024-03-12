import os
import sys
import subprocess
import shutil
import datetime
def log(message):
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}")
def check_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
def check_disk_space():
    required_space = 1000000  # 1GB
    disk_stat = shutil.disk_usage('/')
    if disk_stat.free < required_space:
        print("Insufficient space")
        sys.exit(1)
def check_resources():
    mem_stat = shutil.disk_usage('/')
    cpu_cores = os.cpu_count()
    if mem_stat.total < 2048 or cpu_cores < 2:
        print("Insufficient resources")
        sys.exit(1)
def delete_files():
    files_to_delete = [os.path.join("C:\\", "Program Files", "Mira", f) for f in ["user_data", "pass", "ssh", "api", "card", "lockout", "notes", "srccode"]]
    for file_path in files_to_delete:
        if os.path.exists(file_path):
            os.remove(file_path)
def check_python_libs():
    required_libs = ["cryptography", "termcolor", "mnemonic", "argon2-cffi", "prompt-toolkit", "password-strength", "pyotp", "paramiko", "validators", "phonenumbers"]
    log("Installing Python libs...")
    for lib in required_libs:
        subprocess.run(['pip', 'install', lib], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        log(f"Installed {lib}")
def main():
    try:
        log("System Info:")
        log("-------------------")
        log(f"Disk Space: {shutil.disk_usage('C:').free}")
        log(f"Total Memory: {shutil.disk_usage('C:').total} MB")
        log(f"CPU Cores: {os.cpu_count()}")
        log(f"Admin: {'Yes' if check_admin() else 'No'}")
        log("-------------------")
        if not check_admin():
            print("Must be run as administrator")
            sys.exit(1)
        check_disk_space()
        check_resources()
        delete_files()
        check_python_libs()
        log("Installation completed! Type 'python3 MIRA.py' to start.")
    except KeyboardInterrupt:
        print("Interrupted.")
if __name__ == "__main__":
    main()
