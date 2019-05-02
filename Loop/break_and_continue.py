# program 1
while True:
    n = input("Please, enter any number : ")
    n = int(n)
    if n == 0:
        print ("Unexpected Value. Try again...\n")
        continue
    else:
        print ("The square root of ", n ," = ", n*n)
        break;
print ("\n\t Program Terminated\t\n")

# --------------------------------------------------------------------------------------- #

# program 2
while True:
    n = input("Please, enter the positive value : ")
    n = int(n)
    if n > 0:
        print ("The square root of ", n ," = ", n*n)
        break
    elif n == 0:
        print ("Unexpected Value. Try again...\n")
        continue
    else:
        print ("Not granted negative value\n")
        continue

print ("\n\t Program Terminated\t\n")


# ----------------------------------------------------------------- #

# program 3
program_terminated = False
while not program_terminated:
    n1 = input("Please, enter the first number : ")
    n1 = int(n1)
    n2 = input("Please, enter the second number : ")
    n2 = int(n2)

    while True:
        task = input("Please, enter the add/sub or quit as task: ")

        if task == "quit":
            program_terminated = True
            break
        elif task not in ["add", 'sub', "quit"]:
            print ("Task can not recognize, try again...")
            continue
        elif task == "add":
            print ("Addition of ", n1, " and ", n2, " is ", n1+n2)
            break
        elif task == "sub":
            print ("Subtraction of ", n1, " and ", n2, " is ", n1-n2)
            break

print ("\n\t Program Terminated\t\n")
