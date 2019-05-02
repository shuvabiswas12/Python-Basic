# writing json ...


import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+") # open the json file
    data = json.loads(old_file.read()) # lode the convert the python object and read that
    print("Current age is ", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1 # here the age increase one by one 
    print("new age is ", data["age"])

else:
    old_file = open("./ages.json", "w+")
    data = {"name":"Shuva Biswas", "age": 24}
    print("No file found, setting default age to ", data["age"])


old_file.seek(0) # the pointer of json point the position at 0 and through this the json pointer
# saves json object the position at 0
# for example: {"name": "Shuva Biswas", "age": 27}

# if i not set position at 0 then  the json pointer indicates the pointer at the end of file
# and after that it set a new dictionary or json object in that file ...
# for example: {"name": "Shuva Biswas", "age": 27} {"name": "Shuva Biswas", "age": 28}



old_file.write(json.dumps(data)) # saving json object into file named 'ages.json'

old_file.close()





