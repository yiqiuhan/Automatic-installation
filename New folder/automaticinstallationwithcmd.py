import os
from winreg import *
from subprocess import Popen
import subprocess
import time
from PyQt5.QtCore import QThread, pyqtSignal


class versioncampare(QThread):
 updateRunImmediate = pyqtSignal(bool)
 textone = pyqtSignal(str)
 texttwo = pyqtSignal(str)
 
 def __init__(self, netdisk):
     super(versioncampare, self).__init__()
     self.netdisk = netdisk
 def webversion (self):
     
     
     generallist = []
     qalist = []
     
     uppath = "/BRE_MASTERS_MFG/INV/R24-Senna/px64"
     path = self.netdisk + uppath
     for name in os.listdir(path) :
         generallist.append(name)
         generallist.reverse()
         a = (generallist[0])

        #the last RTM check can be removed to exclude RTM versions
         if 'srv' not in a and 'dev' not in a and 'QA' in a :
          qalist.append(a)

     b = (max(qalist))
     global d
     #HERE NEEDS EXTRA TRY DOR NUMBER IF BUILDS ON FUTURE RELEASES
     d = b[4:7]
     global web 
     web = int(d)
     print (web)
     print(type(web))

 def localversion (self):
     try:   
         registryKey = OpenKey(HKEY_CURRENT_USER, r'Software\Autodesk\Inventor\RegistryVersion24.0\System')
         a = (EnumValue(registryKey,0))
         b = str(a[1])
         c = int(b[3:6])
         global local 
         local = c
         print(local)
         print(type(local))
     except:
         local = 0
         print ('you have not installed Inventor at local')

 def run(self):
     self.webversion()
     self.localversion()
     self.campare()
     
 def campare(self):
     if web < local or web == local:
         print ('you have already installed latest version ', local)
         text = 'the web version is' +" "+ str(web) +" "+ 'which is equal to your local version' +" "+ str(local) +"  "+ str(time.strftime("%H:%M:%S"))
         self.textone.emit(text)
     else:
         print ('the web version is',web, 'which is higher than your local version')
         text = 'the web version is' +" "+ str(web) +" "+ 'which is higher than your local version' +" "+ str(local) +"  "+ str(time.strftime("%H:%M:%S"))
         self.textone.emit(text)
         os.system('taskkill /f /im %s' % 'inventor.exe')
         os.system('taskkill /f /im %s' % 'acad.exe')
         os.system('taskkill /f /im %s' % 'dwgviewr.exe')
         os.system('taskkill /f /im %s' % 'InvRO.exe')
         os.system('taskkill /f /im %s' % 'acad.exe')
         os.system('taskkill /f /im %s' % 'AddInMgr.exe')
         os.system('taskkill /f /im %s' % 'DtDv.exe')
         os.system('taskkill /f /im %s' % 'AddInMgr.exe')
         os.system('taskkill /f /im %s' % '3dsmax.exe')
         
         a= "\BRE_MASTERS_MFG\INV\R24-Senna\px64\M24_"
         b="_x64_QA\Setup\Setup.exe /qb /LANG en-US /c INSTALLDIR=\"C:\Program Files\Autodesk\Inventor 2020\\\" ACADSERIALPREFIX=399 ACADSERIALNUMBER=99999966 ACADSTANDALONENETWORKTYPE=3 ACADSERVERPATH=\"CADQASERVER2 000000000000\" ACADLICENSESERVERTYPE=\"Single Server License\" ACADLICENSETYPE=\"Network License\" ACADFIRSTNAME=autodesk ACADLASTNAME=inc  ADLM_CONFIG_FILE=InventorCombinedConfig.pit ADLM_DEF_PRODKEY=797L1 PRODUCTEDITION=INVPROSA ADSK_EULA_STATUS=#1 ADSK_SOURCE_ROOT=\"M:\" FILESINUSETEXT="" REBOOT=ReallySuppress ADSK_SETUP_EXE=1"

         installcmd = self.netdisk + a + str(web) + b
         print (installcmd)

         cmd = "Msiexec.exe /X {7F4DD591-2464-0001-0000-7107D70F3DB4} /passive"
         self.texttwo.emit(cmd)
         #return
         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         
         cmd = "Msiexec.exe /X {28B89EEF-3028-0409-0100-CF3F3A09B77D} /passive"
         self.texttwo.emit(cmd)         
         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         cmd = "Msiexec.exe /X {B9312A51-41B5-479D-9F72-E7448A2D89AF} /passive"
         self.texttwo.emit(cmd)
         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         cmd = "Msiexec.exe /X {B46DECD1-2464-4EF1-0000-22D71E81877C} /passive"
         self.texttwo.emit(cmd)
         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         cmd = "Msiexec.exe /X {7F4DD591-2464-0001-1033-7107D70F3DB4} /passive"
         self.texttwo.emit(cmd)
         p = subprocess.Popen(cmd, shell=True)
         p.wait()

         cmd = installcmd
         self.texttwo.emit(cmd)
         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         
         self.updateRunImmediate.emit(True)
         
         
   
#c = versioncampare()
#while True:
   # c.webversion("//panda/BRE_MASTERS_MFG/INV/R24-Senna/px64")
   # c.localversion(r'Software\Autodesk\Inventor\RegistryVersion24.0\System')
   # c.campare(web,local)
   # time.sleep(7200)
#
