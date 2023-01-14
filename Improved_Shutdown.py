import subprocess
import time
import os
x = 1

for x in range(4):
    if x < 4:
        x+1
        time.sleep(1)
        print("på tide og sova {}".format(x))
        subprocess.run(["powershell.exe", "-File", "FunShutdown\playsound.ps1"])

os.system("shutdown /s")