
# note:- the shutil module is for both copy, paste, move file and folder
# ---------------------------------------------------------------------- # 


import shutil as st


# this line can copy the file to destination folder
st.copy('D:/Python Learning Basic/Folder1/mydocument.txt', 'D:/Python Learning Basic/Folder1/Folder2')



# this line can copy the file to destinaton folder with a new name
st.copy('D:/Python Learning Basic/Folder1/mydocument.txt', 'D:/Python Learning Basic/Folder1/Folder2/newDocument.txt')




''' This line can copy the whole folder to a new folder with a name'''
# st.copytree('D:/Python Learning Basic/practice python 15.08.2018', 'D:/Python Learning Basic/Folder1/Folder2/backup')




# this line can move a file to a destination folder
# it can be rename with same time also ...
st.move('D:/Python Learning Basic/Folder1/newDoc.txt', 'D:/Python Learning Basic/Folder1/myFolder')
