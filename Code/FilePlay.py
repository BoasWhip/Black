'''
The shutil (or shell utilities) module has utility functions 
for copy, move, rename and delete files.
'''

import os
import shutil

# os.path.join('usr', 'bin', 'spam')
'''
    'usr\\bin\\spam' or 'usr/bin/spam'
'''
# location = 'A:\eBooks\Python\edX\Notes\Handouts'
os.chdir('A:\\eBooks\\Python\edX\\Notes\\Handouts')
location = os.getcwd() # :: gets current working directory
filename = ''
print(os.path.join(location, filename))

'''
os.makedirs('.\\Files') # :: create folder in current directory
os.makedirs('.\\Files') # :: create folder in parent directory
os.makedirs('.\\Archive')
shutil.copytree('.', '.\\Archive') # :: one-step folder copy

print(os.path.abspath('.'))
print(os.listdir())
'''

filelist = os.listdir()

count = 0
for filename in filelist:
    if '_L' in filename:
        filechange = filename.replace('_Lecture','')
        filechange = filechange.replace(' -- ',' ')
        print(filename, filechange, sep=' :: ')
        count += 1
        if count > 0:
            shutil.move(os.path.join(location, filename), os.path.join(location, filechange))

'''
        filechange = filename.replace("-","_")
'''
print('Renamed:',count)
