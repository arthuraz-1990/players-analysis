from typing import List
from utilfns import get_page_source_new
from customtypes import ItemInfo, PlayerInfo

import re

def get_players_by_team(teaminfo: ItemInfo) -> List[PlayerInfo]:
    """ Função para extrair as informações dos jogadores de um time """
    print(f'Buscando jogadores do time {teaminfo.title}...')
    # Pegando informações mais detalhadas do jogador...
    baseurl = f'{teaminfo.href}/plus/1'
    baseurl = baseurl.replace('startseite', 'kader')
    soup = get_page_source_new(baseurl)

    items = []
    for player_row in soup.select('table.items tr.odd, table.items tr.even'):
        player_info = PlayerInfo()
        player_info.team = teaminfo.title
        items.append(player_info)
        cols = player_row.findAll('td', recursive=False)
        i = 1

        loaned_re = re.compile(r'Emprestado(.*)')
        # Iterando em cada coluna em cada linha
        for player_col in cols:
            match i:
                case 1:
                    info = player_col.find('div', {'class': 'rn_nummer'})
                    player_info.number = info.text
                case 2:
                    player_info.name = player_col.find('td', {'class': 'hauptlink'}).find('a').text.strip().replace('\n', '')
                    player_info.position = player_col.find('td', {'class': None, 'rowspan': None}).text.strip().replace('\n', '')
                    player_info.loaned = player_col.find('a', title=loaned_re) is not None
                case 3:
                    player_info.age = player_col.text
                case 4:
                    flags = player_col.findAll('img', {'class': 'flaggenrahmen'})
                    player_info.nationality = ', '.join([flag['title'] for flag in flags])
                case 5:
                    player_info.height = player_col.text
                case 6:
                    player_info.foot = player_col.text
                case 7:
                    player_info.joined = player_col.text
                case 8:
                    signed_from = player_col.find('img')
                    if signed_from is not None:
                        player_info.signed_from = signed_from['alt']
                case 9:
                    player_info.contract = player_col.text
                case 10:
                    player_info.market_value = player_col.text        
            i = i + 1;

        
    print(f'{len(items)} jogadores para o time {teaminfo.title}.\n')
    return items