import os
import shutil 

os.chdir(r'Y:\DESKTOOLS\USD Trading\sTeve\\futures data')
filelist = os.listdir(os.getcwd())
print(type(filelist), len(filelist))

count = 0
total = 0
datafile = []
datapack = []

for filename in filelist:
    if filename[-4:] == '.csv':
        datafile.append(filename)

for filename in datafile:
    datasource = open(filename).read()
    for datapoint in datafile:
        datapack.append(datapoint)
        count +=1

print(datapack)

'''
    count += len(datasource)
    for datapoint in datasource:
#        print(datapoint)
        total = 0
    #filename.
    #shutil.move(os.path.join('.',filename), os.path.join('.','archive',filename))
'''

print(count)
