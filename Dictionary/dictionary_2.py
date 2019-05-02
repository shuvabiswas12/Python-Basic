# dictionary in python ...

dit = {} # this is an empty dictionary
print(dit)

# ....................



man = {'name': 'pythonLearner', 'age': 24, 'birthday': '12-09-2007'}
print(man)

# ....................



print(list(man.keys())) # this will print all keys from man dictionary as a list

print(list(man.values())) # this will print all values from man dictionary as a list

print(list(man.items()))

      
# but this will be show key and values as a list ...
print(man.keys()) 
print(man.values())
print(man.items())


# printing the keys from man dictionary using a for loop
for key in man.keys():
    print(key)

# printing the values from man dictionary using a for loop
for value in man.values():
    print(value)

# printing the items from man dictionary using a for loop
for item in man.items():
    print(item)


# printing the keys and values form man dictionary using a for loop
for keys, values in man.items():
    print(keys, values)




# check the two dictionary if they are equal or not ...
woman = {'age': 20, 'name': 'HP', 'birthday': '07 Decembar'}
print(man == woman)



# check if a value is in present in a dictionary ... now i consider 'man' dictionary in here
print('24' in man.values())



# get() method is dictionary ...
# get() method takes two parameters one is key and another is interger value or a string
# thats return if key is not found

print(man.get('age', 0)) # it returns the value of age
print(man.get('color' '')) # it returns None



# setdefault() method ...
# this method create e key with value thats is a default value
man.setdefault('color', 'black')
print(man)

# if i wanna to change that value after creating than it will not be change ...

man['color'] = 20 # it will not be change ...
print(man)



# ..................................













