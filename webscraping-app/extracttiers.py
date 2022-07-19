from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from utilfns import get_page
import pandas as pd


baseUrl = 'https://www.transfermarkt.com/wettbewerbe/national/wettbewerbe'
baseCountryId = 26

URL = f'{baseUrl}/{baseCountryId}'
print(URL)

driver = get_page(URL)

soup = BeautifulSoup(driver.page_source, 'html.parser')
for td in soup.find_all('td', class_='hauptlink'):
    link = td.find('a', title=True)
    if (link):
        print(link['href'])
        print(link['title'])
        print(link.text)
