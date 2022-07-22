from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

import re
import datetime

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


BASE_PAGE_URL = 'https://www.transfermarkt.com.br'

def convert_date(value: str) -> datetime.date | None:
    """ Conversão da data em string para um valor que possa ser salvo pelo banco de dados """
    if value is not None:
        date_str = re.match(r'\d{2}/\d{2}/\d{4}', value)
        if date_str is not None:
            date_parts = date_str.group(0).split('/')
            return datetime.date(int(date_parts[2]), int(date_parts[1]), int(date_parts[0]))
    return None

def convert_float_value(number_value: str) -> float | None:
    """ Conversão de um valor float de uma string para um numero que possa ser salvo no banco de dados """
    if number_value is not None:
        number_str = re.match(r'^\d+(?:,\d+)?', number_value)
        if number_str is not None:
            return float(number_str.group(0).replace(',', '.'))
    return None

def convert_monetary_value(monetary_value: str) -> float | None:
    """ Conversão de um valor monetário de uma string para um numero que possa ser salvo no banco de dados """
    value_float = convert_float_value(monetary_value)
    if value_float is None:
        return None
    elif "mi." in monetary_value:
        return value_float * 1000000
    else:
        return value_float * 1000
    

def convert_player_number(number_str: str) -> int | None:
    """ Convertendo número do jogador de uma String para um número inteiro """
    if number_str is not None and "-" not in number_str:
        return int(number_str)
    else:
        return None

def str_or_null_value(str_value: str) -> str | None:    
    if str_value is None or str_value.strip() == '-' or len(str_value.strip()) == 0:
        return None
    else:
        return str_value