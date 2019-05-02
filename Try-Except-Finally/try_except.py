
# This is called "try-except" in python which is called in java is "try-catch" block

# function 1
def divide(a, b):
    try:
        return a/b
    except:
        print('You can\'t divide by zero')
    finally:
        print('Inside finally block')


# function 2
def calculate(a, b):
    try:
        result = a/b
    except:
        print("Problem found")
    else:
        print("else block works")
        return result
    finally:
        print("Inside finally block")



print(divide(1, 0))
print(calculate(1, 2))
