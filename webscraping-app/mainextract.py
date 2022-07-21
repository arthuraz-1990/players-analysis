from extracttiers import get_main_competitions_by_country
from extractteams import get_teams_by_competition
from extractplayers import get_players_by_team

from datetime import datetime

def main():
    # Campeonatos do brasilzão
    competitions = get_main_competitions_by_country()
    teams = []

    for tier in competitions:
        tier_teams = get_teams_by_competition(tier)
        teams.extend(tier_teams)

    print(f'Total de times encontrados: {len(teams)}\n')
    # print([team.text for team in teams])

    players = []
    for team in teams:
        players.extend(get_players_by_team(team))

    print(f'Total de jogadores encontrados: {len(players)}\n')
    # print(players)
    


start_time = datetime.now()
main()
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))