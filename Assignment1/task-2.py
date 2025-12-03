import os

commands = ["ls", "date", "ps"]  
print("Parent PID:", os.getpid())

for i, cmd in enumerate(commands):
    pid = os.fork()
    if pid == 0:
        os.execvp(cmd, [cmd]) 
        os._exit(0)

for _ in commands:
    os.wait()

print("All child commands executed.")
