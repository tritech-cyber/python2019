add this code to your ~/bash/ directory on your localhost machine to test crontab calling a sh and py script

this is the crontab -e code:

*/10 * * * * /home/cwc/bash/ping1.sh

ping1.sh

#!/bin/bash
/usr/bin/python3 /home/cwc/bash/ping-subprocess.py  >> /home/cwc/https/logs/ping1.txt


# python ping-subprocess.py (save in ~/bash for crontab -)
import subprocess

for ping in range(1,255):
    address = "10.183.1." + str(ping)
    res = subprocess.call(['ping', '-c', '3  ', address],stdout=subprocess.PIPE)
    if res == 0:
        print (address, "OK")
   
