# function in Python
# ----------------------------------

def print_name(name):  ## Here 'def' means definition.
    print("My name is ", name)

name = "Python 3.6.4"
print_name(name)

# program 2
def add_list(ls):
    result = 0
    for item in ls:
        result += item
    return result

list = [2,3,4,5,6,7]
res = add_list(list)
print(res)


# Note 1: in function definition there is not require to add data type as C or Java language ...
# Note 2: function in Python can return None if there is absent return statement.
# Note 3: in function declaration time there must be write 'def' keyword before the function name. Here 'def' means definition that indicates -
# - the python that this is a function.


# program 3
def myFun(x, y = 6, z = 0):
    print("x = ", x, "y = ", y, "z = ", z)

a = 2
b = 3
c = 4
myFun(a, b, c)

# program 3.1
def myFun(x, y = 6, z = 0):
    print("x = ", x, "y = ", y, "z = ", z)

a = 2
b = 3
c = 4
myFun(a, c) # Now I want to see Y = 6 . So, how is this possible ?
# Note : In python, this is not necessary to pass all the required arguments in a function.
# Note: In python, in method perameter i can initialize any parameter in a default value like myFun(x, y=6, z=0). Here the default value of y and
# - z is 6 and 0.

# program 3.2
def myFun(x, y = 6, z = 0):
    print("x = ", x, "y = ", y, "z = ", z)

a = 2
b = 3
c = 4
myFun(x = a, z = b) # this is possible in Python


# program 4
def addValue(ls):
    return sum(ls) # Here sun() is a built-in fuction in python that calculate and return the total of values of a list

list = [2,4,6,4,89, 6]
result = addValue(list)
print(result)


# program 5
# write a program to find average of the elements of list
def avg(ls):
    result = sum(ls)
    result = result / len(ls)
    return result

list = [1,2,3,4,5,6,7,8,9,10]
print(avg(list))



# program 6
# write a program to print a multiplicaton table
def multiplication_table(num = 1):
    for item in range(1, 11):
        print(num," * ", item, " = ", (item*num))

number = input("Please enter a positive number for multiplication table : ")
number  = int(number)

if (number < 0):
    print("Negative number is not allowed\n")
elif number == 0:
    print("0 is not allowed\n")
else:
    multiplication_table(number)

print("\n\tProgram Terminated\n\t")
