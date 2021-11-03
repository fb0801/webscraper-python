#import bs4
#import BeautifulSoup
from bs4 import BeautifulSoup
with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all('p')
#doc.title
#doc.find()
#find_all('p')[0] get the first element

print(tags)
