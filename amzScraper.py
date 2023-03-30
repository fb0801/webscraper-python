import requests
from bs4 import BeautifulSoup
import smtplib


url="https://www.amazon.co.uk/JavaScript-Definitive-Guide-David-Flanagan/dp/1491952024/ref=sr_1_12?crid=2ANADZPKVIT42&keywords=javascript+book&qid=1680199981&sprefix=java%2Caps%2C136&sr=8-12"

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


def checkPrice():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id="priceBlock_ourprice").get_text()
    convertedPrice = price[0:5]

    if(convertedPrice < 20):
        sendMail()


    print(convertedPrice)

    print(title.strip)


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587) #connect to sever
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('', '')
    subject = "New Price alert"
    body= "check amazon link: "
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "",
        msg
    )

    print("Email sent")

    server.quit()#close connection

checkPrice()