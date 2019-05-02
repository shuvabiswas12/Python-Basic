
# waling on a directory tree ...using ' os.walk() ' method ... 

import os

for folderName, subFolderName, fileName in os.walk('D:/Python Learning Basic/Folder1'):
    print('The Folder Is: '+str(folderName))
    print('The Sub Folder Name: '+str(subFolderName))
    print('The file is: '+str(fileName))
    print()

    

