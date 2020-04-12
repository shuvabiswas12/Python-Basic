
# --------------- URL slicing --------------- #
sample_url = "http://coreyms.com"
print(sample_url)

# reverse the url
print(sample_url[::-1])

# get the top level domain
print(sample_url[-4:])

# print the http:// without url
print(sample_url[:7])

# print the domain without http:// and .com
print(sample_url[7:-4])


# --------------- List slicing --------------- #
myList = [10,11,12,13,14,15,16,17,18,19]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# Rules:-->    list [start:end:step]

print(myList[2:-4:2])

# reverse the list
print(myList[::-1])

