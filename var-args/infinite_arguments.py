## Infinite arguments in python ...


def print_names(*peoples):  ## this is called infinte arguments
    ## which is called variable arguments in java
    
    for name in peoples:
        print(name)
        print()


print_names('jhon', 'mike', 'smiley', 'paulo')
