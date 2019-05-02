
# shelve module ...

import shelve
shelveFile = shelve.open('mydata')
shelveFile['cats'] = ['mango', 'apple', 'banana', 'coconut']
shelveFile.close()



shelveFile = shelve.open('mydata')
print(shelveFile.keys())
print(list(shelveFile.keys())) # this line returns the key of my data file ...
print(list(shelveFile.values())) # this line returns the value of my data file ...


''' note: - the shelve module create '.bak', '.dat', '.dir' file '''

''' The shleve module can store python object in a binary file... '''

''' shelve.open() function can returns a dictionary like shleve value ... '''


