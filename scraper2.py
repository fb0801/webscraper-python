#import BeautifulSoup
from os import link
import re
from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result  = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents
prices = {}

for tr in trs:
    for td in tr.contents:
        print (td)
        print()