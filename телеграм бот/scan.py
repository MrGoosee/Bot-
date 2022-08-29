from bs4 import BeautifulSoup
import requests

url = 'https://habr.com/ru/news/'
page = requests.get(url)

filteredNews = []
allNews = []
filteredhref = []

soup = BeautifulSoup(page.text, "html.parser")

allNews = soup.findAll('a', class_='tm-article-snippet__title-link')
for data in allNews:
    if data.find('span') is not None:
        filteredNews.append(data.text)
        filteredhref.append("https://habr.com"+data['href'])
# c = 0
# for data in filteredNews:
#     c += 1
#     print(f"{c}) {data}")


