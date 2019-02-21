import os
print  os.popen('tasklist /FI "IMAGENAME eq Calculator.exe"').read().decode('cp936')
