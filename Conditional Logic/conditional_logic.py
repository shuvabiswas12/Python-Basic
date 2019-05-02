# list in Python
number_list = [1,2,3,4,5,6,7,8,9,10]
print(number_list)

# I can see the element of list one by one
print(number_list[0])
print(number_list[1])
print(number_list[2])

# if i want to see an index like number_list[10] than it showing an error named Index_Error -->>
# for example:  print(number_list[10])

# I can see the length of list using len() function
print("Length  = ", len(number_list))

# list of SAARC country
saarc = ["Bangladesh", "India", "Nepal", "Bhutan", "Sri Lanka", "Afghanistan", "Pakistan"]
print(saarc)

print(saarc[0]) # print the value of 1st element of saarc list
print(saarc[3]) # print the value of 4th element of saarc list

print("Length of Saarc : ",saarc.__len__()) # I can find out the lengh of list as __len__() function


# I can justify if a country is in SAARC or NOT

#Example 01
if "USA" in saarc:
    print("True")
else:
    print("False")

#Example 02
if "Bangladesh" in saarc:
    print("True")
else:
    print("False")

# Now I check a country weather it is in saarc or not
country = input("Enter a name of country: ");
if country in saarc:
    print(country + " is a membar of SAARC")
else:
    print(country + " is not membar of SAARC")

print("\n\t********** Program terminated **********\n\t")


# now write a program about grading system -->>
marks = input("Enter your obtained marks: ")
marks = int(marks)
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
elif marks >= 40:
    print("C")
elif marks >= 33:
    print("D")
else:
    print("Failed! Try again ...")

print("\n\t********** program terminated **********\n\t")



# write a program that find out plus or odd minus number
number = input("Enter the number which you want to check : ")
number = int(number)
if number >= 0:
    print("plus number")
else:
    print("minus number")

print("\n\t********** program terminated **********\n\t")




# now write a program that check weather it is even or not
new_number = input("Enter the number : ")
new_number = int(new_number)
if (new_number % 2) == 0:
    print("even")88
else:
    print("odd")


print("\n\t********** program terminated **********\n\t")
