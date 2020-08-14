import os

#/Users/liuduwei/Downloads/0015.ts
"""file1 = r'//combination.ts'
if not os.path.exists(file1):
    os.mknod(file1)
file2 = 'd0015.ts'
os.mknod(file2)
file3 = 'd0108.ts'
os.mknod(file3)"""

with open('//Users//liuduwei//Downloads//0015.ts' ,'rb') as ts1:
    content1 = ts1.read()
ts1.close()
with open('//Users//liuduwei//Downloads//0108.ts', 'rb') as ts2:
    content2 = ts2.read()
ts1.close()
with open('/Users/liuduwei/Downloads/0018.ts','rb') as ts3:
    content3 = ts3.read()
ts3.close()
combinationfile = open('combination.ts','ab')
dts1 = open('doo15.ts', 'wb')
dts2 = open('d0108.ts', 'wb')
combinationfile.write(content1)
combinationfile.close()
combinationfile = open('combination.ts','ab')
combinationfile.write(content2)
combinationfile.close()
dts1.write(content1)
dts1.close()
dts2.write(content2)
dts2.close()


