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
  web = int(c) 
  print (web)
  print(type(web))

 def localversion (self,path):
  registryKey = OpenKey(HKEY_CURRENT_USER, path)
  c = (EnumValue(registryKey,0))
  local = c[1]
  
  print(local)
  print(type(local))

 def campare(self, web, local):
  if web < local:
    print ('ccc')
  else:
    print ('ddd')
  
   
c = versioncampare() 
c.webversion("//panda/BRE_MASTERS_MFG/INV/R24-Senna/px64")
c.localversion(r'Software\Autodesk\Inventor\RegistryVersion24.0\System')
c.campare

 



   

 
