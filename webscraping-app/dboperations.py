from typing import List
import psycopg2
import psycopg2.extras

from customtypes import PlayerInfo

from utilfns import convert_date, convert_float_value, convert_monetary_value, convert_player_number, str_or_null_value

def create_connection():
    return psycopg2.connect(
        host='localhost',
        port=5432,
        database='players_db',
        user='postgres',
        password='postgres'
    )

db_connection = create_connection()
main_table_name = 'public.players_info'

def truncate_table() -> None:
    """ Limpar a tabela antes da execução """

    print('Limpando dados antes da execução')
    cursor = db_connection.cursor()
    cursor.execute(
        f"""
            TRUNCATE {main_table_name};
        """)

    db_connection.commit()


def save_players_list(player_list: List[PlayerInfo]) -> None:
    """ Salvar lista de informações de jogadores no banco de dados """
    cursor = db_connection.cursor()

    print(f'Persistindo dados de {len(player_list)} jogadores')

    psycopg2.extras.execute_values(cursor, 
    f"""
        INSERT INTO {main_table_name}
        (
            name, position, number, team,
            nationality, height, foot,
            joined, signed_from, contract, market_value, 
            birth_date, loaned
        ) 
        VALUES %s;
    """, ((
        player.name, player.position,
        convert_player_number(player.number), 
        player.team, player.nationality, 
        convert_float_value(player.height), 
        str_or_null_value(player.foot), 
        convert_date(player.joined),
        str_or_null_value(player.signed_from), 
        convert_date(player.contract), 
        convert_monetary_value(player.market_value),
        convert_date(player.age), player.loaned
     ) for player in player_list), page_size=10000)

    db_connection.commit()
    db_connection.close()

