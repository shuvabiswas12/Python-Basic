
# list comprehensions exmaple
# ------------------------------------------------

# program 1
li = [1,2,3,4]
new_li = []
for i in li:
    new_li.append(2*i)

print(new_li)
print("program terminated\n\n")

## we can write this program as below using list comprehensions -- >>
new_li = [2*i for i in li]
print(new_li)
print("program terminated\n\n")





# program 2
li = list(range(1, 11))
even = []
for item in li:
    if item % 2 == 0:
        even.append(item)

print(even)
print("program terminated\n\n")

## we can write this program as below using list comprehensions --- >>
lst = list(range(1, 11))
even = [item for item in lst if item % 2 == 0]
print(even)
print("program terminated\n\n")





# program 3
# write a program to create a list of square of element of another list
new_lst = list(range(1, 20, 2))
print(new_lst)
square_lst = [x*x for x in new_lst]
print(square_lst)
print("program terminated\n\n")
