from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable
request = requests.get('https://news.ycombinator.com/news')
response=request.text
soup=BeautifulSoup(response,'html.parser')
article=soup.find_all('title>a')
article_texts = []
article_links = []
for article in article:
    text = article.getText()
    link = article.get("href")
    article_texts.append(text)
    article_links.append(link)
table = PrettyTable()
table.field_names = ["Title", "Link"]
for i in range(len(article_texts)):
    table.add_row([article_texts[i], article_links[i]])
table.align["Title"] = "l"
table.align["Link"] = "l"
print(table)

