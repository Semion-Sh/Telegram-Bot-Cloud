import requests
from bs4 import BeautifulSoup


url = 'https://myfin.by/currency/minsk'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# items = soup.find_all('div', class_='c-best-rates')
items = soup.find('div', class_='c-best-rates')
item = float(items.text[63:69])