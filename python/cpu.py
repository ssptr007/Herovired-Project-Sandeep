##Auther : Sandeep R
#Description : This python script is used to check the cpu utilization if cpu utilization reached 80%, It will alert saying reached 80%.

import psutil
cpu_limit=0.0
limit=80.0
try:
    while True: # This is infinate loop, it will continue executing still user interupts.
        cpu_limit = psutil.cpu_percent(interval=1) #psutil.cpu_percent() it will check the cpu utilization every 1 second
        if (cpu_limit >= limit): # This condition is used to check the current cpu utilization limit reached above or equal 80% or not 
            print("Cpu limit above 80%!!!!!!!!! values is:",cpu_limit)
        else:
            print("CPU Limit is normal, The value is:",cpu_limit)

except KeyboardInterrupt: # This will accept the Interrption from the user. CTRL+C is the interruption
    print("Interpted by the user!!!!!")


        
