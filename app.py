"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
--------------------------------
"""

import sys
import random
from stats import constants  # basketball-team-stats_v1
from typing import List, Dict


def cleanse_data(**kwargs):

    players = kwargs['players']
    teams = kwargs['teams']
    total_players = len(players)
    total_teams = len(teams)
    num_of_players = total_players // total_teams

    experienced = [e for e in players if e['experience'] == 'YES']
    inexperienced = [i for i in players if i['experience'] == 'NO']
    total_experienced = len(experienced)
    total_inexperienced = len(inexperienced)
    max_experienced = total_experienced // total_teams

    list_of_teams = {team: [] for team in teams}

    for p in players.copy():
        r = random.choice(players)
        if (r not in list_of_teams['Panthers'] and 
            len(list_of_teams['Panthers']) < num_of_players):
            list_of_teams['Panthers'].append(r)
            players.remove(r)
        elif (r not in list_of_teams['Bandits'] and 
            len(list_of_teams['Bandits']) < num_of_players):
            list_of_teams['Bandits'].append(r)
            players.remove(r)
        elif (r not in list_of_teams['Warriors'] and 
            len(list_of_teams['Warriors']) < num_of_players):
            list_of_teams['Warriors'].append(r)
            players.remove(r)

            
    # print(list_of_teams['Panthers'], '\n')
    # print(len(list_of_teams['Panthers']), '\n')

    # print(list_of_teams['Bandits'], '\n')
    # print(len(list_of_teams['Bandits']), '\n')

    # print(list_of_teams['Warriors'], '\n')
    # print(len(list_of_teams['Warriors']), '\n')

    panthers = list_of_teams['Panthers']
    bandits = list_of_teams['Bandits']
    warriors = list_of_teams['Warriors']
    
    return panthers, bandits, warriors

    # print(f'\nTeam: {teams[0]} Stats')
    # print('-' * 20)
    # print(f'Total players: {len(teams)}')  # Balance Teams
    # print(f'Players on Team:\n ')

cleanse_data(players=constants.PLAYERS, teams=constants.TEAMS)


def get_teams(*args):
    """
    Converting TEAMS list into a dictionary
    making sure the list of the teams can grow in the future

    TEAMS = (['Panthers', 'Bandits', 'Warriors'],)
    teams = {1: 'Panthers', 2: 'Bandits', 3: 'Warriors'}
    """

    teams = {index: value for team in args for index, value in enumerate(team, 1)}

    for key, value in teams.items():
        print(f'  {key}) {value}')

    team_option: int = int(input('\n Enter an option > '))

    if team_option == 1:
        pass
    elif team_option == 2:
        pass
    elif team_option == 3:
        pass


def display_stats():
    """
    DOCSTRINGS
    """

    app_title = 'BASKETBALL TEAM STATS TOOL'
    menu_header = 'MENU'
    print('-' * (len(app_title)+2) + '\n' + '|' + '' * (len(app_title)+2) + app_title + '|\n' + '-' * (len(app_title)+2) + '\n')
    print(f'---- {menu_header} ----\n')

    menu = {}
    menu['1'] = 'Display Team Stats'
    menu['2'] = 'Quit'

    print('Here are your choices:')

    for key, value in menu.items():
        print(f'  {key}) {value}')

    try:
        while menu:

            option: int = input('\n Enter an option > ')
            try:
                option = int(option)
                if option == 1:
                    get_teams(constants.TEAMS)
                elif option == 2:
                    print('\nClosing application...')
                    break
                elif option < 1 or option > 2:
                    print(f'Specified value "{option}" is not in the list! Try again...')
                    continue
            except ValueError:
                print(f'Please enter an integer! => "{option}" is invalid.')
               
    except KeyboardInterrupt:
        print('\nExiting... CTRL+C')
        sys.exit()


if __name__ == '__main__':
    display_stats()
