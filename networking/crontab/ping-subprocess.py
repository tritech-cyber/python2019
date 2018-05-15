# python ping-subprocess.py (save in ~/bash for crontab -)
import subprocess

for ping in range(1,255):
    address = "10.183.1." + str(ping)
    res = subprocess.call(['ping', '-c', '3  ', address],stdout=subprocess.PIPE)
    if res == 0:
        print (address, "OK")
   
