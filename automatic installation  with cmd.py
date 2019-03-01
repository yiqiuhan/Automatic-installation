import os
from winreg import *
from subprocess import Popen
import subprocess
import time

class versioncampare:
 def webversion (self,path):
  
     generallist = []
     qalist = []
     for name in os.listdir(path) :
         generallist.append(name)
         generallist.reverse()
         a = (generallist[0])

        #the last RTM check can be removed to exclude RTM versions
         if 'srv' not in a and 'dev' not in a and 'QA' in a :
          qalist.append(a)

     b = (max(qalist))
     global d
     d = b[4:7]
     global web 
     web = int(d)
     print (web)
     print(type(web))

 def localversion (self,path):
     try:   
         registryKey = OpenKey(HKEY_CURRENT_USER, path)
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

 def campare(self, ww, ll):
     if ww < ll or ww == ll:
         print ('you have already installed latest version ', local)
     else:
         print ('the web version is',web, 'which is higher than your local version')

         a= "\\\\panda\BRE_MASTERS_MFG\INV\R24-Senna\px64\M24_"
         b="_x64_QA\Setup\Setup.exe /qb /LANG en-US /c INSTALLDIR=\"C:\Program Files\Autodesk\Inventor 2020\\\" ACADSERIALPREFIX=399 ACADSERIALNUMBER=99999966 ACADSTANDALONENETWORKTYPE=3 ACADSERVERPATH=\"CADQASERVER2 000000000000\" ACADLICENSESERVERTYPE=\"Single Server License\" ACADLICENSETYPE=\"Network License\" ACADFIRSTNAME=autodesk ACADLASTNAME=inc  ADLM_CONFIG_FILE=InventorCombinedConfig.pit ADLM_DEF_PRODKEY=797L1 PRODUCTEDITION=INVPROSA ADSK_EULA_STATUS=#1 ADSK_SOURCE_ROOT=\"M:\" FILESINUSETEXT="" REBOOT=ReallySuppress ADSK_SETUP_EXE=1"

         installcmd = a + d + b
         print (installcmd)

         cmd = "Msiexec.exe /X {7F4DD591-2464-0001-0000-7107D70F3DB4} /passive"
         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         cmd = "Msiexec.exe /X {28B89EEF-3028-0409-0100-CF3F3A09B77D} /passive"
         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         cmd = "Msiexec.exe /X {B9312A51-41B5-479D-9F72-E7448A2D89AF} /passive"
         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         cmd = "Msiexec.exe /X {B46DECD1-2464-4EF1-0000-22D71E81877C} /passive"
         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         cmd = "Msiexec.exe /X {7F4DD591-2464-0001-1033-7107D70F3DB4} /passive"
         p = subprocess.Popen(cmd, shell=True)
         p.wait()

         cmd = installcmd

         p = subprocess.Popen(cmd, shell=True)
         p.wait()
         
         #f = open("C:/Users/uninstall.bat", "w")

         #f.write( \n\n\nMsiexec.exe /X {7F4DD591-2464-0001-1033-7107D70F3DB4} /passive" )

         #f = open("C:/Users/uninstall.bat", "a+")

         #f.write("\n\\\\panda\BRE_MASTERS_MFG\INV\R24-Senna\px64\M24_" )

         #f.write( d )

         #f.write( " " )

         # 关闭打开的文件
         #f.close()

         #p = Popen("uninstall.bat", cwd=r"C:/Users")
         #stdout, stderr = p.communicate()
   
c = versioncampare()
while True:
    c.webversion("//panda/BRE_MASTERS_MFG/INV/R24-Senna/px64")
    c.localversion(r'Software\Autodesk\Inventor\RegistryVersion24.0\System')
    c.campare(web,local)
    time.sleep(7200)
