#import bs4
#import BeautifulSoup
import re
from bs4 import BeautifulSoup
with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all(text=re.compile('\$.*'))
#doc.title
#doc.find()
#find_all('p')[0] get the first element

print(tags)
