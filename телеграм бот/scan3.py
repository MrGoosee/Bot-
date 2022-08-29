from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com/'
page = requests.get(url)

filteredimg = []
allimg = []


soup = BeautifulSoup(page.text, "html.parser")

allimg = soup.findAll('img')
for data in allimg:
    filteredimg.append(data['data-src'])
print(allimg)
