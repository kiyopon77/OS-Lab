#!/bin/bash

#echo "----- SYSTEM INFORMATION -----"
#echo "Kernel Version:"
#uname -r
#
#echo ""
#echo "User:"
#whoami
#
#echo ""
#echo "Hardware Info (Checking Virtualization Support):"
#lscpu | grep 'Virtualization'
#IN LINUX

import subprocess

def check_vm():
    try:
        result = subprocess.check_output("systemd-detect-virt", shell=True).decode().strip()
        
        if result == "none":
            print("This system is running on REAL hardware.")
        else:
            print(f"This system is running inside a Virtual Machine: {result}")
    except:
        print("Could not detect virtualization environment.")

check_vm()
