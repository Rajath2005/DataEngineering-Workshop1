import requests
from bs4 import BeautifulSoup

res = requests.get('https://blog.python.org/blog/')
soup = BeautifulSoup(res.content, 'html5lib')

for row in soup.findAll("article"):

    title = row.find("h3").text
    author = row.find("a").text
    date = row.find("time").text

    print("Title:", title)
    print("Author:", author)
    print("Date:", date)
