
# deep copy module

import copy
spam = [1, 2, 3, 4]
chesse = copy.deepcopy(spam)
chesse[1] = 43
print(chesse)
print(spam)

print('Four square is six'+\
      'teen. ok?')

# The \ line continuation caracter can be used to stretch
# python instruction across miltiple line 


# string and tupple is immutable ...



# note:- deepcopy() method copy a list to an anther list
#        and that list is a new list...
#        for understanding deepcopy() please see the example below ... 
