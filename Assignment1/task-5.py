import os
import time

def cpu_task(i):
    for _ in range(5_000_000):
        pass
    print("Task", i, "done, PID:", os.getpid())

tasks = [5, 10, 15]  

for i, nice_value in enumerate(tasks):
    pid = os.fork()
    if pid == 0:
        os.nice(nice_value)  
        cpu_task(i+1)
        os._exit(0)

for _ in tasks:
    os.wait()

print("All CPU tasks finished.")
