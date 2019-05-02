from bs4 import BeautifulSoup
import requests

search = input("Enter Search Term:")
params = {'q': search}
r = requests.get("https://www.bing.com", params=params)
soup = BeautifulSoup(r.text, "html.parser")


# here the first parameter is looking for element and
# the 2nd parameter is looking for attributes
result = soup.find("ol", {"id": "b_results"}) 
links = soup.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text # looking for elements like <a></a>
    item_href = item.find("a").attrs["href"] # looking for attributes like 'href'

    if item_text and item_href:
        print(item_text)
        print(item_href)




'''

NOTE:- Here the program find all the links and their anchor text which is first page ...

'''


        
