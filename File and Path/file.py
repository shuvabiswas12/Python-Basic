
# file in python

file = "test.txt" # this is file name

# opening file in write mode ...
fp = open(file, 'w') # this is mode for file such w mode means write mode
fp

fp.write("This is first line...") # writing line into file
fp.close() # closing file

print(fp)


# opening file again in read mode ...
fp = open(file, 'r')
fl = fp.read()
print(fl)

fp.close() # file closing again...


# opening file in append mode ...
fp = open(file, 'a')
fp.write("This is second line ... ")
fp.close()

print(fp)



fp = open(file, 'r') # opening file in read mode ...
print(fp.read())
fp.close()


fp = open(file, 'w')
fp.write("\nThis is new line\n this is another line ...")
fp.close()
# -----------------------------------------------



fp = open(file, 'r')
fp.read()
fp.seek(0) # this method helps to point line or string from 0 position/index
# if i start the seek() positon form 1 "such seek(1)" then its start to point at 1 index

ls = fp.readlines() # this method returns a list from a text file
# fp.close()


# if i work as a big file then ...
for line in ls:
    print(line)

fp.close()




# ---------------------------------------------



# this is an another way for file, by which the file automaticaly closed
# ...
with open(file, 'r') as fp:
    print(fp.read())
