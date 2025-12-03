import os
import time

pid = os.fork()

if pid == 0:
    print(f"Child PID: {os.getpid()} exiting immediately")
    os._exit(0)
else:
    print(f"Parent PID: {os.getpid()} sleeping to create zombie")
    time.sleep(20)  
    print("Parent now exiting")

# orphan:
import os
import time

pid = os.fork()

if pid == 0:
    print(f"Child PID: {os.getpid()} starting, original parent PID: {os.getppid()}")
    time.sleep(25) 
    print(f"Child PID: {os.getpid()} now has new parent PID: {os.getppid()}")
    os._exit(0)
else:
    print(f"Parent PID: {os.getpid()} exiting immediately")
    os._exit(0)
