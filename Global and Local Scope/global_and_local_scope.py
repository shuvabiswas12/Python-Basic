
# Python local scope or variable ...

def show():
    egg = "Hello"  # This is called local scope pr variable 
    print(egg)

egg = 42
show()
print(egg)



# Global scope or varibale ...


def display():
    global mind # This is called a global scope or variable
    mind = 'Shuva'
    print(mind)

mind = 'Your mind'
display()
print(mind)




