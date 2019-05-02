# dictionary in python
# ---------------------------------

dictionary = {} # empty dictionary
print(type(dictionary))
print("\n")


# example 01
dictionary = {"English": 64, "Bangla": 90, "Math": 87, "Science": 65}
print(dictionary["English"])
print("\n")


# example 02
dictionary = {1: 90, 2: 80, 3: 33, 4: 76}
print(dictionary[1])
print("\n")


# I want to create an empty dictionary and after that i will added value in dictionary
dt = {}
print(dt)
print('\n')

dt[1] = "one"
dt[2] = "two"
dt[3] = "three"
dt[4] = "four"
dt[5] = "five"
print(dt)
print("\n")

for item in dt:
    print(dt[item])

print("Program Terminated\n")

# example 03
dt = {"a":"A", "b":"B", "c":"C", "d":"D"}
dt[(1,2,3)] = "tupple"
print(dt)


# example 04
marks = {"CSE101": {"Bangla": 74, "English": 73}, "EEE1002":{"Bangla": 70, "English": 87}}
print(marks)
print(marks["CSE101"])
print(marks["EEE1002"])
print(marks["CSE101"]["Bangla"])

# example 05
bd_division_info = {}
bd_division_info["Barishal"] = {"district": 11, "upazila": 97, "union": 222}
bd_division_info["Dhaka"] = {"district": 10, "upazila": 40, "union": 89}
bd_division_info["Khulna"] = {"district": 45, "upazila": 45, "union": 220}

print(bd_division_info)

# if i want to print only district from a dictionary
div = bd_division_info.keys()
print(div)

div1 = bd_division_info["Barishal"].keys()
print(div1)

for division in div:
    print(division, " upazila ")
    print(bd_division_info[division]["upazila"])


# ....
for key in bd_division_info:
    print(key)
    print(bd_division_info[key])

print("program terminated")
print("\n")

# ....
for key, value in bd_division_info.items():
    print(key)
    print(value)

print("progrm Terminated")
print("\n")

# ....
print( bd_division_info.items())
print("\n")


# note -->> mutable component like list or set can not add in dictionary.
