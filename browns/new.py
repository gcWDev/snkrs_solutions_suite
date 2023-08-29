import requests
import time
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

while True:
    response = requests.get(
        'https://www.brownsshoes.com/en/women/accessories-and-outerwear/slippers/product/ugg/tazz/266618.html?dwvar_266618_color=015&position=2', headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.prettify())
        approved = soup.find(class_="bs-select-size")
        blocked = soup.find(class_='px-captcha')
    else:
        print('blocked')
