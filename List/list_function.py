# some function for list ...

lst = ['cat', 'bat', 'mango', 'dog', 'apple']

# It returns the index value of an element
value = lst.index('cat')
print(value)

#...
lst.sort() # sorting in accesding order
print(lst)

lst.sort(reverse=True) # sorting in decending order
print(lst)

alphabet = ['a', 'A', 'x', 'X']
alphabet.sort(key=str.lower) # this can sort a list in ASCII-betical order ...
print(alphabet)



