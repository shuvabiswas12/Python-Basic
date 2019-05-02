import requests

my_data = {"name":"Nick", "email":"nick@example.com"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data = my_data)

f = open("form.html", "w+")
f.write(r.text) # return the code of that url

f.close()


