from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO


def searchFor():
    search = input('Type Search Term: ')
    param = {"q": search} # 'q' is an parameter for search query in bing.com

    r = requests.get("https://www.bing.com/images/search", params=param)

    # diclare parser must. here, html.parser is a default parser
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class":"thumb"}) # here, 1st parameter is elements and 2md parameter is attributes

    count = 1
    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting ", item.attrs["href"])
            
			
			# it returns the last name after spliting url by '/'
			# for example: 'www.google.com/wallpaper.jpeg'
			# Then its split the url by '/' and then it returns last string called 'wallpaper.jpeg'
            title = item.attrs["href"].split("/")[-1] 
            
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./scraped_images/" + title, img.format)
                print("saved ", count)
                count = count + 1
                
            except:
                print("Could't Save")

        except:
            print("Connection not stablished")

    searchFor()

searchFor()




