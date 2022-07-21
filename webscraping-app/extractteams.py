from typing import List
from utilfns import get_page_source_new
from customtypes import ItemInfo

def get_teams_by_competition(competitioninfo: ItemInfo) -> List[ItemInfo]:
    print(f'Buscando times do campeonato {competitioninfo.title}...')
    baseurl = competitioninfo.href
    soup = get_page_source_new(baseurl)

    items = []
    for link in soup.select('#yw1 td.hauptlink a[title]'):
        items.append(ItemInfo(link['href'], link['title'], link.text))

    print(f'{len(items)} times para o campeonato {competitioninfo.title}.')
    return items