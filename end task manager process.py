
import os
os.system('taskkill /f /im %s' % 'InvRO.exe')
os.system('taskkill /f /im %s' % 'acad.exe')

#import psutil, os
#pids = psutil.pids()
#for pid in pids:
#        p = psutil.Process(pid)
#        print('pid-%s,pname-%s' % (pid, p.name()))
#        if p.name() == 'dllhost.exe':
#            cmd = 'taskkill /F /IM dllhost.exe'
#            os.system(cmd)
