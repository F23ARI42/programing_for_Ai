import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(".titleline > a")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)
table = PrettyTable()
table.field_names = ["Title", "Link"]
for i in range(len(article_texts)):
    table.add_row([article_texts[i], article_links[i]])
table.align["Title"] = "l"
table.align["Link"] = "l"
print(table)