
# string program for practice

# program 1
# -------------------------------  >>
import turtle
name = turtle.textinput("name", "Whats your name?") # this is another way to input text or string
name = name.lower() # this method is convert upper case to lower case text

if name.startswith("mr"): # this method check text in during start text
    name = name.replace("mr", "Hello Sir") # this method replace text
    name = name.capitalize() # this method capitalize the text
    print(name)
else:
    name = name.capitalize()
    name = "Hi "+ name +" How are you !\n"
    print(name)

print("\n\tProgram Complete\t\n")

turtle.exitonclick()

print("\n\tProgram terminated\t\n")


# program 2
# --------------------------------- >>
str1 = input("Please type a string: ")
str2 = input("Please type an another string: ")
str3 = input("Please type other string as number like 12353: ")
