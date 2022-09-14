import requests
from bs4 import BeautifulSoup


url = 'https://myfin.by/currency/minsk'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find('div', class_='c-best-rates')
prodaja = float(soup.select('.c-best-rates table > tbody > tr > td:nth-child(3)')[0].text)
pokupka = float(soup.select('.c-best-rates table > tbody > tr > td:nth-child(2)')[0].text)
nbrb = float(soup.select('.c-best-rates table > tbody > tr > td:nth-child(4)')[0].text)

