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
for link in soup.select('td.hauptlink td a[title~=Brasileiro]'):
    print(link['href'])
    print(link['title'])
    print(link.text)
