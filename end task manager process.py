
import os
os.system('taskkill /f /im %s' % 'acad.exe')
os.system('taskkill /f /im %s' % 'dwgviewr.exe')
os.system('taskkill /f /im %s' % 'InvRO.exe')
os.system('taskkill /f /im %s' % 'acad.exe')
os.system('taskkill /f /im %s' % 'AddInMgr.exe')
os.system('taskkill /f /im %s' % 'DtDv.exe')
os.system('taskkill /f /im %s' % 'AddInMgr.exe')

#import psutil, os
#pids = psutil.pids()
#for pid in pids:
#        p = psutil.Process(pid)
#        print('pid-%s,pname-%s' % (pid, p.name()))
#        if p.name() == 'dllhost.exe':
#            cmd = 'taskkill /F /IM dllhost.exe'
#            os.system(cmd)
