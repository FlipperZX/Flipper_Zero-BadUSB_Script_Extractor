import subprocess
import time

exe_name = "duckhunt.0.9.blacklist.exe"
path = r"C:\Users\BadUSB_Logger\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\duckhunt.0.9.blacklist.exe"

subprocess.run(["taskkill", "/f", "/im", exe_name])