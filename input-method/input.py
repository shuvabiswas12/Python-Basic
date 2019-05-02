
# input function to take something as input from keyboard or user
# int function to take an integer value from keyboard
# float function to take an floating value form keyboard


name = input("What is your name ?") # Here input() function is return a string
print("My name is : ",name)


num_1 = input("Please type an integer and press type an enter: ")
num_1 = int(num_1) # Here int() function return an integer value

num_2 = input("Please type an float and type an enter :  ")
num_2 = float(num_2) # Here float() function return an floating value

print("You enter ", num_1, num_2, "result of (",num_1,"*",num_2,") = ", num_1 * num_2)

# ------------------------------------ #
print("\n\tThank You\t")
