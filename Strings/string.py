
# string in python
# Note: In python there is no character type. Instead of this there has string type

str = "Bangladesh"
print(str)

str = 'Bangladesh'
print(str)

# str = 'Bangladesh's' # here is show an error because of apostropi(')
str = "Bangladesh's" # now its ok
print(str)

str = 'Bangladesh\'s' # an apostropi can be written as this
print(str)

# string can be access by this way in bellow ...
print(str[0])
print(str[1])
print(str[2]) # ....

print("\n")

# string can be access by loop by this way ...
for c in str:
    print(c)


# the way that can remove the space after the string ...
str = "Bangladesh                          "
l = len(str)
print("Len before the operation: ", l)
str = str.rstrip()
l = len(str)
print("Len after the operation: ", l)

print("\n\tProgram Terminated\t\n")

# the way that can remove the space before string ...
str = "                         Bangladesh"
l = len(str)
print("Len before the operation: ", l)
str = str.lstrip()
l = len(str)
print("Len after the operation: ", l)

print("\n\tProgram Terminated\t\n")

# the way that can remove the space in string both after and before ...
str = "                         Bangladesh                          "
l = len(str)
print("Len before the operation: ", l)
str = str.strip()
l = len(str)
print("Len after the operation: ", l)

print("\n\tProgram Terminated\t\n")

str = "Bangladesh is my county. I am in now 24 years old. This years is 2018"
print(str.find("is")) # for finding any sub-string in a string we use find() method.
# if the sub string is found then that method is return the position if not found than its return -1 .

print("\n\tProgram Terminated\t\n")

# replace a string using replace() method
str  = "this is county. this is country. this is country"
str = str.replace("this", "This")  # this method return a new string after replace any string
print(str)

print("\n\tProgram Terminated\t\n")

str = "Bangladesh is my county. I am in now 24 years old. This years is 2018"
print(str.count("is")) # count function return the value of matching string
print("\n\tProgram terminated\t\n")




# string concat ...
print("<-------------> 4 <---------->")
name = 'My name is ' + 'Hello:Nick:World'.split(':')[1]
print(name)

# ---------------------------------------------------------------
