# this is test code v 203659.658*5

import pyautogui as pag
import subprocess
import time

# start the application to do some stuff and manage any files 
exe_path = "vpnplanet.exe"


# Run the executable and make shure it containcs the teest og sadofa sdf ao jjhaf 
subprocess.Popen([exe_path])

# action that play more roled infoe and test ebvsdf
actions = [
    (611,528,4),
    (611,528,2),
    (611,528,2),
    (611,528,2),
    (611,528,2),
    (611,528,2),
    (625,371,36),
    (626,531,5),
    (500,531,26),
    (427,479,12),
    (629,434,6),
    (856,156,36),
]

#final loop to prevent ant mistake s 

for x, y, duration in actions:
    pag.click(x, y, duration=duration)


#finnaly why we do it againn
