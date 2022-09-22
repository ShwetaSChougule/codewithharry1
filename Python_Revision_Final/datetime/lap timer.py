#Modules related are Datetime
#classes - Date,time,datetime,timedelta

import time             #This module provides various functions to manipulate time values.
starttime= time.time()      #time when timer starts for new lap
lasttime = starttime        #time when last lap over
lapnum=1
print("Press Enter to start laps")
# when Enter laps will be occuring and when CTRL+C
try:                     #erronous code
    while True:
        input()     #to take input
        laptime = round((time.time()-lasttime),2)        #last lap time
        totaltime =round((starttime-time.time()),2)
#         print
        print("Lap time required",laptime)
        print("lapnumber",lapnum)
        print("*" * 20)
        lapnum+=1
        lasttime=time.time()

except KeyboardInterrupt:                     # fallback code
    print("done")
# Exceptions are something that interrupts normal flow of program
# KeyboardInterrupt occurs when user interrupts normal execution of program
# interpreters in python regularly checks for any interrupts while executing code.
# In python interpreter throws KeyboardInterrupt when user presses ctrl+c or del













