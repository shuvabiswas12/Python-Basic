# List in python
# this is another lecture for list

spam = []
print(spam)


spam = ['cat', 'bat', 'coconut']
print(spam)

value = len(spam)
print(value)


# this means some value added at value position 2 and then it added to last...
spam[2:] = [10, 20, 30, 40, 50]
print(spam)


# this will print the value form position 1 to and less than 3 position
print(spam[1:3])

print(spam[-2]) # this is print the value from last

print(spam[-4])

print(spam[1:]) # this will print the value from position 1

spam[2] = ['Mango', 'apple', 'orange']
print(spam)



# adding two list ...
spam = spam + [1, 2, 3, 4, 5]
print(spam)




# this is the another way of adding two list ...
spam.extend([100, 200, 300])
print(spam)




# i can delete a value from a list
del spam[10]
print(spam)



# i can convert a string to a list ...
lst = list('hello')
print(lst)



# find an element from a list ...

print('Hello' in spam)

print('Shuva' not in spam)

print('Biswas' in spam)

# i can print a list value like this ...
print([1, 2, 3, 4, 5][1])



