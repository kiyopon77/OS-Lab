# task 1
import os

n = int(input("Enter number of child processes: "))
print("Parent PID:", os.getpid())

for i in range(n):
    pid = os.fork()
    if pid == 0:
        print("Child", i+1, "PID:", os.getpid(), "Parent PID:", os.getppid())
        print("Hello from child", i+1)
        os._exit(0)  

for _ in range(n):
    os.wait()

print("All child processes finished.")