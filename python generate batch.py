
# 打开一个文件

a = str(160)
f = open("C:/Users/itools/Desktop/uninstall.bat", "w")

f.write( "Msiexec.exe /X {7F4DD591-2464-0001-0000-7107D70F3DB4} /passive\nMsiexec.exe /X {28B89EEF-3028-0409-0100-CF3F3A09B77D} /passive\nMsiexec.exe /X {B9312A51-41B5-479D-9F72-E7448A2D89AF} /passive\nMsiexec.exe /X {B46DECD1-2464-4EF1-0000-22D71E81877C} /passive\nMsiexec.exe /X {7F4DD591-2464-0001-1033-7107D70F3DB4} /passive" )

f = open("C:/Users/itools/Desktop/uninstall.bat", "a+")

f.write("\n\\\\beaver\BRE_MASTERS_MFG\INV\R24-Senna\px64\M24_" )

f.write( a )

f.write( "_x64_QA\Setup\Setup.exe /qb /LANG en-US /c INSTALLDIR=\"C:\Program Files\Autodesk\Inventor 2020\\\" ACADSERIALPREFIX=399 ACADSERIALNUMBER=99999966 ACADSTANDALONENETWORKTYPE=3 ACADSERVERPATH=\"CADQASERVER2 000000000000\" ACADLICENSESERVERTYPE=\"Single Server License\" ACADLICENSETYPE=\"Network License\" ACADFIRSTNAME=autodesk ACADLASTNAME=inc  ADLM_CONFIG_FILE=InventorCombinedConfig.pit ADLM_DEF_PRODKEY=797L1 PRODUCTEDITION=INVPROSA ADSK_EULA_STATUS=#1 ADSK_SOURCE_ROOT=\"M:\" FILESINUSETEXT="" REBOOT=ReallySuppress ADSK_SETUP_EXE=1 " )

# 关闭打开的文件
f.close()

