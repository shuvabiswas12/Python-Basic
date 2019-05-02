
# list in python -------- >>
# ------------------------------

# this is a list
saarc = ["Bangladesh", "Pakistan", "Nepal", "India", "Bhutan", 'Sri Lanka']
print(saarc)


# this [2] is the position of list
print(['Nabil', 'Java', 'Corey', 'Python', 'USA', 'C++'] [2])


# now i want to add an element in list. so i use append() method.
saarc.append("Afganistan") # this element is will added at the order of last
print(saarc)

# now i want to add an element in any position. so i use insert() method.
# This method takes two parameter, one is position and another is element.
saarc.insert(0, "UK")   # this element will be added at position 0
print(saarc)

saarc.insert(3, "Germany")   # this element will be added at position 3
print(saarc)


# now i want to sort the list . So is have to use sort() method.
saarc.sort() # this is an acending order sort
print(saarc)

# now i want to reverse the list. so i have to use reverse() method.
saarc.reverse() #  this is a decending order sort
print(saarc)

# now i want to remove element from the list
saarc.remove("UK")
print(saarc)

# program - 01
item = "Germany"
if item in saarc:
    saarc.remove(item)

else:
    print(item, " is not exist in list")

print("\n\tProgram Terminated\t\n")

#-------------------------------------------------------------------------------------#

# pop() method is list
# this method delete an element from a list and reurn that value
fruits = ["mango", 'banana', 'apple', 'orange']
print(fruits)

item = fruits.pop() # pop() method delete an element an order of last
print(item)
print(fruits)

# we can delete an element using this pop() function
# this pop() function take a parameter that contains position
item = fruits.pop(1) # this pop method delete an element of position 1
print(item)
print(fruits)

# extend() function
li_1 = [1,2,3]
li_2 = [4,5,6]
li_1.extend(li_2) # this extend() method add a list with another list
print(li_1)

li_3 = [3,2,5,6,7,8,4,5,6]
print(li_3)

li_1.extend(li_3)
print(li_1)
print(li_1.count(2))
li_1.sort()
print(li_1)


# we can create a empty list ---- >>
li_new = []
print(li_new)
for i in list(range(1, 21)):
    li_new.append(i)

print(li_new)

# list in mathmatics
# 1 --- >>
list = list(range(1, 6))
list_2 = list*2
print(list_2)

# 2 --- >>
list_3 = list + list_2
print(list_3)

# calculation in list as string --- >>
# in this way i can make a string from a list which is contains some string type of elements
str = ['a', 'b', 'c']
print(str)

str_1 = "".join(str) # example 01
print(str_1)

str_2 = ",".join(str) # example 02
print(str_2)

str_3 = "-".join(str) # example 03
print(str_3)




# del() method --- >>
li_4 = list(range(30, 200, 5))
print(li_4)
del(li_4[0]) # here i use del() method and give an arguments for deleting elements from List
print(li_4)

# it can use as this --- >>
# it can be use to delete the full List
del(li_4)
print(li_4) # now delete that list. so when i run this then it shows an error because
# after using del() function it has been deleted with all elements
