
#from winreg import *
import winreg
ob = OpenKey(HKEY_CURRENT_USER, r'Software\Autodesk\Inventor\RegistryVersion24.0\System')
t = (EnumValue(ob,0))
print(t)
print(type(t))
