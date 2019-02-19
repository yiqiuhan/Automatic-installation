from winreg import *
try:
    registryKey = OpenKey(HKEY_CURRENT_USER, r'Software\Autodesk\Inventor\RegistryVersion24.0\System')
    a = (EnumValue(registryKey,0))
    print(a)
     
except:
    print ('it does not exists')
