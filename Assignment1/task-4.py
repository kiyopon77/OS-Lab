import os
import time

pid = os.fork()

if pid == 0:
    print(f"Child PID: {os.getpid()} running...")
    time.sleep(10)  
    os._exit(0)
else:
    print(f"Parent PID: {os.getpid()}, Child PID: {pid}")

    pid_to_inspect = pid  
    with open(f"/proc/{pid_to_inspect}/status") as f:
        for line in f:
            if line.startswith(("Name:", "State:", "VmSize:", "VmRSS:")):
                print(line.strip())

    try:
        print("Executable:", os.readlink(f"/proc/{pid_to_inspect}/exe"))
    except:
        print("No access to executable")

    try:
        fds = os.listdir(f"/proc/{pid_to_inspect}/fd")
        print("Open FDs:", fds)
    except:
        print("No access to fd directory")

    time.sleep(10)  