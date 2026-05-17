#!/usr/bin/env python3
# System Info Script
# Shows basic information about your Linux system

import os
import socket
import shutil
from datetime import datetime

# Get system information
username = os.environ.get("USER")
hostname = socket.gethostname()
current_dir = os.getcwd()
now = datetime.now().strftime("%A, %d %B %Y — %H:%M")

# Get disk information
disk = shutil.disk_usage("/")
disk_total = disk.total // (1024 ** 3)
disk_used = disk.used // (1024 ** 3)
disk_free = disk.free // (1024 ** 3)

 # Print the information
print("===== System Information =====")
print(f"User:        {username}")
print(f"Hostname:    {hostname}")
print(f"Location:    {current_dir}")
print("--- Disk Usage ---")
print(f"Total:       {disk_total} GB")
print(f"Used:        {disk_used} GB")
print(f"Free:        {disk_free} GB")
print(f"Date/Time:   {now}")
print("==============================")

