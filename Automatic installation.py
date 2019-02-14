import os
from winreg import *


class versioncampare:
 def webversion (self,path):
  #path = "//panda/BRE_MASTERS_MFG/INV/R24-Senna/px64"
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
    #qalist.reverse()
    #b = (qalist[0])

  c = b[4:7]
  global web 
  web = int(c)
  print (web)
  print(type(web))

 def localversion (self,path):
  registryKey = OpenKey(HKEY_CURRENT_USER, path)
  a = (EnumValue(registryKey,0))
  b = str(a[1])
  c = int(b[3:6])
  global local 
  local = c
  print(local)
  print(type(local))

 def campare(self, ww, ll):
  if ww < ll:
    print ('you have already installed latest version ', local)
  else:
    print ('the web version is',web, 'which is higher than your local version')
  
   
c = versioncampare() 
c.webversion("//panda/BRE_MASTERS_MFG/INV/R24-Senna/px64")
c.localversion(r'Software\Autodesk\Inventor\RegistryVersion24.0\System')
c.campare(web,local)

 



   

 
