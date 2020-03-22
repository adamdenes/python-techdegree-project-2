"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
--------------------------------
"""

import re
import sys
import random
from stats import constants


def cleanse_data(**kwargs):
    """
    Cleanse_data will take two variable arguments and return a cleansed dict
        - guardians field will only contain list of names
        - experience will be turned into a boolean
        - height will only contain numbers
        - teams will be balanced based on experienced and inexperienced players
    """

    players = kwargs['players']
    teams = kwargs['teams']
    total_players = len(players)
    total_teams = len(teams)
    num_of_players = total_players // total_teams
    list_of_teams = {team: [] for team in teams}
    players_with_experience = []
    players_without_experience = []

    for player in players.copy():
        for key, value in player.items():
            if key == 'guardians':
                player[key] = value.split(' and ')
            elif key == 'experience' and value == 'YES':
                player[key] = True
                players_with_experience.append(player)
            elif key == 'experience' and value == 'NO':
                player[key] = False
                players_without_experience.append(player)
            elif key == 'height':
                player[key] = int(re.sub(r'\s\w+', '', value))

    exp_per_team = len(players_with_experience) // total_teams
    inexp_per_team = len(players_without_experience) // total_teams

    for name, val in list_of_teams.items():
        experienced_players = 0
        inexperienced_players = 0

        for player in players.copy():          
            rand_player = random.choice(players)

            if rand_player['experience'] == True and experienced_players < 3 and len(list_of_teams[name]) < num_of_players:
                experienced_players += 1
                list_of_teams[name].append(rand_player)
                players.remove(rand_player)

            elif rand_player['experience'] == False and inexperienced_players < 3 and len(list_of_teams[name]) < num_of_players:
                inexperienced_players += 1 
                list_of_teams[name].append(rand_player)
                players.remove(rand_player)

    return list_of_teams

cleaned_data = cleanse_data(players=constants.PLAYERS, teams=constants.TEAMS)


def show_data(data, option):
    """
    Generate the output data that will be showed if one of the teams is selected

    EXAMPLE RESULT::

    Team: Panthers Stats
    --------------------
    Total players: 6
    Number of inexperienced players: 3
    Number of experienced players: 3
    Average height of the team: 253

    Players on Team:
    - Suzane Greenberg, Phillip Helm, Kimmy Stein, Karl Saygan, Joe Kavalier, Arnold Willis

    Guardians of Players:
    - Henrietta Dumas, Thomas Helm, Eva Jones, Bill Stein, Hillary Stein, Heather Bledsoe, Sam Kavalier, Elaine Kavalier, Claire Willis
    """
    name = [k['name'] for k in data[option]]
    guardian = [g for guardian in data[option] for g in guardian['guardians']]
    height = [h['height'] for h in data[option]]

    summ = 0
    for s in height:
        summ += s

    average_height = summ / len(data[option])

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
    print('Average height of the team: {0:.2f}'.format(average_height))
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

    try:
        if team_option == 1:
            show_data(cleaned_data, 'Panthers')
        elif team_option == 2:
            show_data(cleaned_data, 'Bandits')
        elif team_option == 3:
            show_data(cleaned_data, 'Warriors')
        else:
            raise ValueError('Please use the presented options!')
    except ValueError as ve:
        print(ve)


def display_stats():
    """
    Display_stats is the main function of the app
    it will display the main menu and prompt the user for options
    as long as the player does not quit (CTRL-C or 'Quit' option).

    The app will handle invalid input data and react accordingly.
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
                print(f'Please enter an integer!')

    except KeyboardInterrupt:
        print('\nExiting... CTRL+C')
        sys.exit()


if __name__ == '__main__':
    display_stats()
    