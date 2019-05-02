# This is a Magical Calculator in python ...

import re

print("Our Magical Calculator")
print("Type 'exit' to Quit !!")

previous = 0
run = True

def performMath():

    global previous

    ## we can write 'nonlocal' instead of global in here ...
    
    print('In first: ', previous)

    equation = ''

    if previous == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input('2nd stage: '+str(previous))


    if equation == 'exit':
        run = False

    else:
        equation = re.sub('[a-zA-Z],.:()" "]', '', equation)
        print(equation)

        print('3rd Stage: ', previous)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


        print("You typed: ", previous)



while run:
    performMath()
        
        
