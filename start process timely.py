import time, os 
    
def re_exe(cmd, inc ): 
    while True: 
        os.system(cmd); 
        time.sleep(inc) 
    
re_exe("Msiexec.exe /X {7F4DD591-2464-0001-0000-7107D70F3DB4} /passive", 3)
