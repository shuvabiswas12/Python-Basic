
# file in python ...

import os
print(os.path.join('folder1', 'folder2', 'actress.jpg'))

print(os.sep) # in os module there has a seo variable which contains '\'

print(os.getcwd()) # get current working directory


print(os.chdir('C:\\')) # change file directory ...

print(os.getcwd())

os.chdir('D:\Python Learning Basic\Folder1\Folder2')

print(os.path.abspath('actress.jpg'))
print(os.path.relpath('actress.jpg'))
print(os.path.abspath('..//..//actress.jpg')) # this return abs path of two folder before


print(os.path.basename('D:\Python Learning Basic\Folder1\Folder2'))

print(os.path.basename('D:\Python Learning Basic\Folder1\Folder2/actress.jpg'))

print(os.path.dirname('D:\Python Learning Basic\Folder1\Folder2'))


# this return true or false if the file is exists ... 
print(os.path.exists('D:\Python Learning Basic\Folder1\Folder2/actress.jpg'))


# this return true or false if the file is or not ...
print(os.path.isfile('D:\Python Learning Basic\Folder1\Folder2/actress.jpg'))


# get size of specific file ...
print(os.path.getsize('D:\Python Learning Basic\Folder1\Folder2/actress.jpg'))


# this return a list of total file or directory from inside a folder ...
print(os.listdir('D:\Python Learning Basic'))


# this is create a directory
os.makedirs('D:\\Python Learning Basic\\Folder1\\myFolder')






