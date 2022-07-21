from extracttiers import get_main_competitions_by_country
from extractteams import get_teams_by_competition

# Campeonatos do brasilzão
competitions = get_main_competitions_by_country()
teams = []

for tier in competitions:
    tier_teams = get_teams_by_competition(tier)
    teams.extend(tier_teams)

print(f'Total de times encontrados: {len(teams)}')
print([team.text for team in teams])