
# tupple
# ---------------------- >>

x = 1, 2, 3 # tupple
print(type(x))
print(x)

x = (1, 2, 3) # tupple
print(type(x))
print(x)

y = 1 # this is int type
print(type(y))

y = 1, # this is tupple type
print(type(y))

t = () # empty tupple
print("empty tupple: ", type(t))

tpl = (1, 2, 3)
print(tpl[0])
print(tpl[1])
print(tpl[2])

# we can do unpack a tupples element into some variable
tpl = (1, 2, 3, 4)
n1, n2, n3, n4 = tpl  # unpacking element
print(n1, n2, n3, n4)

tp = n2, n4  # packing elements
print(tp)


# we can keep some data into a tupple like below --- >>
tl = (1, 2, 3, [4, 5, 6], 3.5, "Shuva Biswas", ('ctg', 'dhaka', 'bangladesh'))
for item in tl:
    print(type(item))

print(tl[3][0]) # printing the element
print(tl[6][2]) # printing the element


# note:  tupple is immutable



#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)


#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple


tuplex = tuplex + (9,)
print(tuplex)


#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)


#converting the tuple to list
listx = list(tuplex)


#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)  # converting a list into a tuple
print(tuplex)

