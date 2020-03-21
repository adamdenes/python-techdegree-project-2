"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
--------------------------------
"""

import re
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
    list_of_teams = {team: [] for team in teams}

    panthers = list_of_teams['Panthers']
    bandits = list_of_teams['Bandits']
    warriors = list_of_teams['Warriors']

    for player in players.copy():
        for key, value in player.items():
            if key == 'guardians':
                player[key] = value.split(' and ')
            elif key == 'experience' and value == 'YES':
                player[key] = True
            elif key == 'experience' and value == 'NO':
                player[key] = False
            elif key == 'height':
                player[key] = int(re.sub(r'\s\w+', '', value))

    for l in list_of_teams.copy():
        for player in players.copy():          
            r = random.choice(players)
            if (r not in list_of_teams[l] and
                len(list_of_teams[l]) < num_of_players):
                list_of_teams[l].append(r)
                players.remove(r)

    # print(len(panthers))
    # print(panthers)
    # print(len(bandits))
    # print(bandits)
    # print(len(warriors))
    # print(warriors)

    return list_of_teams

cleaned_data = cleanse_data(players=constants.PLAYERS, teams=constants.TEAMS)


def show_data(data, option):

    name = [k['name'] for k in data[option]]
    guardian = [g for guardian in data[option] for g in guardian['guardians']]
    height = [h['height'] for h in data[option]]
    print(height)
    # sum_height = [re.sub(r'\s\w+', '', h) for h in height]
    
    summ = 0
    for s in height:
        summ += s

    experience = 0
    inexperience = 0
    for exp in data[option]:
        if exp['experience'] == True:
            experience += 1
        else:
            inexperience += 1

    print('\nTeam: {} Stats'.format(option))
    print('-' * 20)
    print('Total players: {}'.format(len(data[option])))
    print('Number of inexperienced players: {}'.format(inexperience))
    print('Number of experienced players: {}'.format(experience))
    print('Average height of the team: {}'.format(summ))
    print('\nPlayers on Team:\n- {}'.format(', '.join(name)))
    print('\nGuardians of Players:\n- {}'.format(', '.join(guardian)))


def get_teams(*args):
    """
    Converting TEAMS list into a dictionary

    TEAMS = (['Panthers', 'Bandits', 'Warriors'],)
    teams = {1: 'Panthers', 2: 'Bandits', 3: 'Warriors'}
    """

    teams = {index: value for team in args for index, value in enumerate(team, 1)}

    for key, value in teams.items():
        print(f'  {key}) {value}')

    team_option: int = int(input('\n Enter a *Teams* option > '))

    if team_option == 1:
        show_data(cleaned_data, 'Panthers')
    elif team_option == 2:
        show_data(cleaned_data, 'Bandits')
    elif team_option == 3:
        show_data(cleaned_data, 'Warriors')


def display_stats():
    """
    DOCSTRINGS TBC
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

            option: int = input('\n Enter a *Menu* option > ')
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
                print(f'Please enter an integer! -> "{option}" is invalid.')

    except KeyboardInterrupt:
        print('\nExiting... CTRL+C')
        sys.exit()


if __name__ == '__main__':
    display_stats()
    