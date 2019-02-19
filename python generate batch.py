

# 打开一个文件
f = open("C:/Users/itools/Desktop/uninstall.bat", "w")

f.write( "Msiexec.exe /X {7F4DD591-2464-0001-0000-7107D70F3DB4} /passive\nMsiexec.exe /X {28B89EEF-3028-0409-0100-CF3F3A09B77D} /passive\nMsiexec.exe /X {B9312A51-41B5-479D-9F72-E7448A2D89AF} /passive\nMsiexec.exe /X {B46DECD1-2464-4EF1-0000-22D71E81877C} /passive\nMsiexec.exe /X {7F4DD591-2464-0001-1033-7107D70F3DB4} /passive" )

# 关闭打开的文件
f.close()
