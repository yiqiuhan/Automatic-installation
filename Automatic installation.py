import os
path = "//panda/BRE_MASTERS_MFG/INV/R24-Senna/px64"
generallist = []
qalist = []
for name in os.listdir(path):
 generallist.append(name)
 generallist.reverse()
 a = (generallist[0])
 
 if 'srv' not in a and 'dev' not in a:
   qalist.append(a)
   
   qalist.reverse()
   b = (qalist[0])
    
 else:
  print ('c')
   
print (qalist)
 



   

 
