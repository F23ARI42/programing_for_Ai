import requests
from bs4 import BeautifulSoup
response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.select(".titleline > a")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))
tags = soup.select(".score")
article = []
for tag in tags:
    vote = int(tag.getText().replace(" points",""))
    article.append(vote)
if article:
    max_index = article.index(max(article))
    print("name",article_texts[max_index])
    print("score",max(article))
else:
    print(" not vote")




