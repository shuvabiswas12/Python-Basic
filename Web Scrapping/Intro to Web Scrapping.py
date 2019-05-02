
# For web scrapping task we need to insatall bs4 module
# For install that module type "pip.exe install bs4" command line into cmd
# After that import BeautifulSoup from bs4 module


from bs4 import BeautifulSoup
import requests

search = input('Enter search Term:')
params = {"q": search}
# url = {"https://www.bing.com/search"}
r = requests.get("https://www.bing.com/search", params = params)

soup = BeautifulSoup(r.text)
print(soup.prettify())



