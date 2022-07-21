from typing import List
from utilfns import get_page_source_new
from customtypes import ItemInfo

def get_main_competitions_by_country(countryid = 26) -> List[ItemInfo]:
    print(f'Buscando competições país {countryid}...')
    baseurl = f'/wettbewerbe/national/wettbewerbe/{countryid}'
    soup = get_page_source_new(baseurl)
    items = []
    for link in soup.select('td.hauptlink td a[title~=Brasileiro]'):
        items.append(ItemInfo(link['href'], link['title'], link.text))

    print(f'{len(items)} campeonatos para o país {countryid}.')
    return items