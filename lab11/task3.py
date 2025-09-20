from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable
request=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web_page=request.text
soup=BeautifulSoup(web_page,"html.parser")
content=soup.find_all("h2")
table=PrettyTable()
table.field_names=["No of Movie","Title"]
for co in content[3:]:
    text=co.get_text()
    no=text.split()[0]
    title=text.split()[1:]
    table.add_row([no,title])
with open("movies.txt", "w", encoding="utf-8") as f:
    f.write(table.get_string())

