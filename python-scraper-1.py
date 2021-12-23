#import bs4
#import BeautifulSoup
from os import link
import re
from bs4 import BeautifulSoup
with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, "html.parser")

#tags = doc.find_all(text=re.compile('\$.*'))
#doc.title
#doc.find()
#find_all('p')[0] get the first element
tags = doc.find_all('p', type='text')
for tag in tags:
    tag['placeholder']='Im new hehe'

with open("changed.html", "w") as file:
    file.write(str(doc))

print(tags)
