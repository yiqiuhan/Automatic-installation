from subprocess import Popen
p = Popen("New Text Document.bat", cwd=r"C:\Users\itools\Desktop")
stdout, stderr = p.communicate()
