# Try except block ...


# program 01
# ----------------------------------------

def divideBy(div):
    return 42/div

try:
    print(divideBy(0))

except:
    print('You can\'t be divided by zero')



# program 02
# ---------------------------------------

def test2(value):
    try:
        return 30/value
    except:
        print('You can not divided by zero')

print(test2(0))




# program 03
# ---------------------------------------

print('Enter a number: ')
number = input()
try:
    if int(number) >= 4:
        print('Largest number')
    else:
        print('Smallest number')
except:
    print('You do not enter number')





    
