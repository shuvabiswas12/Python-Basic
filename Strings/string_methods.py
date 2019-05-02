
# String methods ...

spam = 'Hello World'
print(spam)



# upper() & lower() method ...
spam = spam.upper()
print(spam)

print(spam.isupper())

spam = spam.lower()
print(spam)

print(spam.islower())




# PROGRAM   01 ...
# --------------------


myText = input("Type 'yes' or 'YES'\n")
if myText.islower():
    print('True')
else:
    print('False')







# isalpha() & isalnum() & isdecimal() & isspace() & istitle() .... methods

# isalpha() - letter only
# isalnum() - letter and number
# isdecimal() - numbers only
# isspace() - whitespace only
# istitle() - title case only
# title() - make a string to title
# -----------------------------------


# join() method ---
spam = ['bat', 'cat', 'mango']
spam = ','.join(spam)
print(spam)

spam = ' '.join(['bat', 'cat', 'mango'])
print(spam)



# title() & istitle() method ...
spam = 'This is a world'
print('Is Title: ', spam.istitle())

print('Is title: ',spam.title().istitle())
print('The title is: '+spam.title())





# split() method ...
ls = 'This is new era'.split()
print(ls)

ls = 'This is new era'.split('i') # split where found 'i' and after spliting 'i' will vanished
print(ls)





# rjust() & ljust() & center() ...
text = 'hello'.rjust(10, '*')
print(text)

text = 'hello'.ljust(20, '=')
print(text)

text = 'End'.center(10, '*')
print(text)


# replace() method ...



