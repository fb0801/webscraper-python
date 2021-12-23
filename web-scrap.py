#import BeautifulSoup and other modules

import re
from bs4 import BeautifulSoup
import requests


gpu = input('what would you like to search  for? ') # input from user

url=f"https://www.newegg.com/global/uk-en/p/pl?d={gpu}&N=4131" #feeding the input to the url to find the result
page = requests.get(url).text
doc= BeautifulSoup(page, 'html.parser')

