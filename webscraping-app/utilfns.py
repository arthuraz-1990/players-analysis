from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def get_page_source_new(url: str) -> BeautifulSoup:
    url = f'{BASE_PAGE_URL}{url}'
    print(url)
    req = Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    html = urlopen(req)
    return BeautifulSoup(html, 'html.parser')


BASE_PAGE_URL = 'https://www.transfermarkt.com'