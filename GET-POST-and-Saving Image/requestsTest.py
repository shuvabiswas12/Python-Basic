import requests

r = requests.get("http://google.com")
print("Status: ", r.status_code) # return the status code for more details to know about
# about status please, visit 'https://restapitutorial.com'

print(r.url) # return the url 
print(r.text) # return code of that page...

f = open("./open.html", "w+") # create a html file in write mode
f.write(r.text) # save that page code into the html file 
