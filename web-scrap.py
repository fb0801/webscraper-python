#import BeautifulSoup and other modules

import re
from bs4 import BeautifulSoup
import requests


search_term = input('what would you like to search  for? ') # input from user

url=f"https://www.newegg.com/global/uk-en/p/pl?d={search_term}&N=4131" #feeding the input to the url to find the result
page = requests.get(url).text
doc= BeautifulSoup(page, 'html.parser')

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:1])

for page in range(1, pages + 1):
    url=f"https://www.newegg.com/global/uk-en/p/pl?d={search_term}&N=4131&page={page}" #feeding the input to the url to find the result
    page = requests.get(url).text
    doc= BeautifulSoup(page, 'html.parser')
    
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = doc.find_all(text=re.compile(search_term))

    for item in items:
        print(item)

#print(pages, "pages found")