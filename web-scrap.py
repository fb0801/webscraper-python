#import BeautifulSoup and other modules

import re
from bs4 import BeautifulSoup
import requests


gpu = input('what would you like to search  for? ') # input from user

url=f"https://www.newegg.com/global/uk-en/p/pl?d={gpu}&N=4131" #feeding the input to the url to find the result
page = requests.get(url).text
doc= BeautifulSoup(page, 'html.parser')

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:1])

for page in range(pages):
    url=f"https://www.newegg.com/global/uk-en/p/pl?d={gpu}&N=4131&page={page}" #feeding the input to the url to find the result
    page = requests.get(url).text
    doc= BeautifulSoup(page, 'html.parser')


print(pages, "pages found")