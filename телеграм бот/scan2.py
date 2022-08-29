from bs4 import BeautifulSoup
import requests

url = 'https://wallpapers.99px.ru/wallpapers/tags/anime/gorod/'
page = requests.get(url)

filteredimg = []
allimg = []


soup = BeautifulSoup(page.text, "html.parser")

allimg = soup.findAll('img', class_="photo2_tmb_img c4_fadeIn")
for data in allimg:
    filteredimg.append(data['data-src'])
print(allimg)
