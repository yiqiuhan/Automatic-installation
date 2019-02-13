import os

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
  print (b)


  def localversion (self):
   return b
c = versioncampare() 
c.webversion("//panda/BRE_MASTERS_MFG/INV/R24-Senna/px64")

 



   

 
