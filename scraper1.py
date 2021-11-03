#import our modules
from bs4 import BeautifulSoup
import requests

#link we want to use
url = "https://www.argos.co.uk/product/8672210?clickPR=plp:4:145"

#connect to the url and print out the result in txt file
result = requests.get(url)
doc =BeautifulSoup(result.text, 'html.parser')

prices = doc.find_all(text="£")
print(prices)
