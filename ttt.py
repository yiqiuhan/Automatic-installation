import _thread
import time

def aaa(delay):
    #time.sleep(delay)
    print('sds')

try:
    _thread.start_new_thread( aaa,(1))
    _thread.start_new_thread( aaa,(2))

except:
    print('ccc') 
