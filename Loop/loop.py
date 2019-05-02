
# loop in Python
# ------------------------------------------------------- >>

# for loop
for i in range(10):
    print("I want to be a great programmer")

print("\n\tProgram terminated\t\n")


# now write a program to sum 1 to 50
result = 0
for i in range(51):
    result += i
print(result)

print("\n\tProgram terminated\t\n")


# we write that program as bellow
result = 0
for i in range(1, 51): # that means the value of i start form 1 and end in 50
    result += i
print(result)

print("\n\tProgram terminated\t\n")


# we write that program as bellow
result = 0
for i in range(1, 51, 5):  # that means the value of i is starts from 1 and its increasing value is 5 and its end in 51
    result += i
print(result)

print("\n\tProgram terminated\t\n")

# now write a program that print the sum of 1 to 50 which is divided by 5
result = 0
for i in range(1, 51):
    if (i % 5) == 0:
        result += i
        print(i)
print("\n",result)
print("\n\tProgram terminated\t\n")

# we write that program as bellow
result = 0
for i in range(1, 51, 5):
        result += i
        print(i)

print("\n",result)
print("\n\tProgram terminated\t\n")

# ------------------------------------------------------------------------------------------------- #

## List in loop
country = ["Bangladesh", "India", "Pakistan", "Japan", "Sri Lanka", "Bhutan", "Afganistan"]
for item in country:
    print (item + " is a membar of saarc")

print("\n\tProgram terminated\t\n")


# we can build a list as using range() function. For this we can use list() function, So lets see thats ---- >>
ls = list(range(11))
print(ls)

##
ls = list(range(1, 20))
print(ls)

##
ls = list(range(1, 100, 5))
print(ls)


##
# while loop in Python
## ------------------------------------------ >>

n = input("Please, enter a positive integer: ")
n = int(n)
i = 1
while i in range(11):
    print (n," * ",i," = ",(n*i))
    i += 1
print("\n\tProgram terminated\t\n")
