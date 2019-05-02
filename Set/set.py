
# set in pyhton
# ------------------------------------------ >>

# 1
st=  {1, 2, 3}
print(st)
print(type(st))

#2 union set
st2 = {1, 2, 4, 6}
st_new = st & st2
print(st_new)
print(type(st_new))


# intersection set
st4 = st | st2
print(st4)
print(type(st4))


# 2 if we see the st element which is not present in st2
st5 = st - st2
print(st5)

# 3 if we see the st2 element which is not present in st
st6 = st2 - st
print(st6)

# if we see the element of st and st2 set which is not duplicate between that two set
st7 = st ^ st2
print(st7)

# if we want to find an elemt in a set
print( 1 in st)

print(7 in st2)

# we can create a set using list and tuple also
li = [3, 6, 2]
new_set = set(li)
print(new_set)
print(type(new_set))

tpl = (6, 3, 8)
new_set = set(tpl)
print(new_set)
print(type(new_set))


# in string the set become like below  - >
print(set("Bangladesh"))

# ending set ----------------------- >>
