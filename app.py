import os 
import time
from copy import deepcopy

import csv
import constants

TEAMS = {}
PLAYERS = [player for player in constants.PLAYERS]


def clean():
    """Clean Console"""
    os.system("cls" if os.name == "nt" else "clear")
def clean_constants():
    teams = constants.TEAMS[:]
    players = deepcopy(constants.PLAYERS)
for player in players:
    player["height"] = player['height'].split()
    player['height'] = int(player['height'][0])
    if player['experience'] == 'YES':
             player['experience'] = True
    else:
           player['experience'] = False    
    return players, teams
    
def divide_players(players, team):
    """Dividing given iterables of players into balanced teams"""
panthers = []
bandits = []
warriors = []
experienced_players = [player for player in players if player['experience'] == True]
while experienced_players:
    panthers.append(experienced_players.pop())
    bandits.append(experienced_players.pop())
    warriors.append(experienced_players.pop())
inexperienced_players = [player for player in players if player['experience'] == False]
while inexperienced_players:
    panthers.append(inexperienced_players.pop())
    bandits.append(inexperienced_players.pop())
    warriors.append(inexperienced_players.pop())
    team_lists = [panthers, bandits, warriors]
    return panthers, bandits, warriors, team_lists
  
def welcome ():
    tool_name = "BASKETBALL TEAM STATS TOOL"
    print("*" * len(tool_name))
    print(tool_name)
    print("*" * len(tool_name), end="\n")
    print("-" * 10, "MENU", "-" * 10, end="\n")
    
    
    
def menu():
    COMMANDS = ["Display Team Stats", "Quit"]
    for index, item in enumerate (COMMANDS, start = 1):
        print("{})  {}".format(index, item))
print()

  
def sub_menu():
    for index, item in enumerate(constants.TEAMS, start=1):
        print("{})  {}".format(index, item))
print()
  
def display_info(option):
    try:
        team = team_lists[int(option) - 1]
    players_on_team = [player['name'] for player in team]
    average_height = round(sum([player["height"] for player in team])  / len(players_on_team), 2)
    experienced_players = len([player['experience'] for player in team if player['experienced'] == True])
    inexperienced_players = len([player['experience'] for player in team if player['experience'] == False])
    guardians = [", ".join(player['guardians']) for player in team]
    print("\nTEAM: {} Stats".format(constants.TEAMS[int(option) - 1]))
    print("-" * 26, "\n")
    print("Total Players: {}".format(len(team)))
    print()
    print("Player on Team: ", end="")
    for player in players_on_team:
    if player == players_on_team[-1]:
        print(player)
    else:
        print(player, end=", ")
    print("Guardians: ", end="")
    for guardian in guardians:
    if guardian == guardians[-1]:
        print(guardian, end="\n")
    else:
        print(guardian, end+", ")
    print("Number of Experienced Players: {}".format(experienced_players))
    print("Number of inexperienced Players: {}".format(inexperienced_players))
    print("Average Height: {} inches\n".format(average_height))
    input("Press Enter to continue.")
    clear()
    welcome()
except IndexError:
    print("\nThat isn't a valid option. Please try again. \n")
except IndexError:
    print("\nThat isn't a valid option. Please try again. \n")
        
          
def main():
while True:
      menu()
    command = input("Please enter the number for the COMMAND that you want  >  ")
      print()
if command =='1':
      sub_menu()
    option = input("Please enter the number of the OPTION that you want  >  ")
      display_team_info(option)
    print()
      pass 
elif command =='2':
      clean()
    print('The Teams Stats will display a sub menu to choose which teams stats you want displayed')
    print('Quit will allow you to exit the tool')
    print()

elif command == '3':
      print("Good bye.\n")
else:
      print("\n That isn't a valid option. Please try again. \n")




if __name__ =="__main__":
panthers, bandits, warriors, team_lists = divide_players(*clean_constants())
  clean()
welcome()
  
main()
