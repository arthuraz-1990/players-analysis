from typing import List
from utilfns import get_page_source_new
from customtypes import ItemInfo

def get_teams_by_competition(competitioninfo: ItemInfo) -> List[ItemInfo]:
    print(f'Buscando times do campeonato {competitioninfo.title}...')
    baseurl = competitioninfo.href
    soup = get_page_source_new(baseurl)

    items = []
    base_css_search = 'td.hauptlink a[href*=verein]'
    # Pegando os links dos times na seção principal da página
    links = soup.select(f'.large-8.columns {base_css_search}')
    if (len(links) > 0):
        for link in links:
            items.append(ItemInfo(link['href'], link['title'], link.text))
    else:
        # Pegando os links dos times na seção secundária da página
        for link in soup.select(base_css_search):
            # Colocando o href no mesmo padrão dos links principais
            href = link['href'].replace('spielplan', 'startseite')
            items.append(ItemInfo(href, link['title'], link.text))


    print(f'{len(items)} times para o campeonato {competitioninfo.title}.\n')
    return items