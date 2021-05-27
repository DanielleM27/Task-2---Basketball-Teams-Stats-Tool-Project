import os 
import time
from copy import deepcopy

import csv
import constants 


def print_team_statistics(local_team):
    guardians_on_team= [player['guardians'] for player in local_team]
    players_on_team= [player['name'] for player in local_team]
    print(f'the total amount of players on the team ={len(players_on_team)}')
    experienced_players=len([player['experience'] for player in local_team if player['experience'] == True])
    inexperienced_players=len([player['experience'] for player in local_team if player['experience'] == False])
    print(f'number of experienced players = {experienced_players}')
    print(f'number of inexperienced players = {inexperienced_players}')
    
    height_of_team = [player['height'] for player in local_team]
    height_of_team_in_strings = [str(player['height']) for player in local_team]
    
    print('The names of all the players are')
    print(",".join(players_on_team))
    print('The guardians of all my players are')
    print(",".join(guardians_on_team))
    print(f'average_height = {sum(height_of_team)/len(players_on_team)}')
    print()
    
    
    print("The details of all the plaers are as follows: ")
    for a_player in local_team:
        print("player name: " + a_player['name'])
        print("guardian: " + a_player['guardian'])
        print("height: " + str(a_player['height']))
        print()
        
        
        
def procesPlayers():
    players = deepcopy(constants.PLAYERS)
    for player in players:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        height = player['height'].split()
        player['height'] = int(height[0])
    return players





def assignPlayersToTeam(players):
    teams = constants.TEAms[:]
    panthers = []
    bandits = []
    warriors = []
    
    experienced_player = []
    inexperienced_player = []
    for player in players:
        if player ['experience'] == True:
            experienced_player.append(player)
        else:
            inexperienced_player.append(player)
            
    while experienced_player:
        panthers.append(experienced_player.pop())
        warriors.append(experienced_player.pop())
        bandits.append(experienced_player.pop())
    while inexperienced_player:
        panthers.append(inexperienced_player.pop())
        warriors.append(inexperienced_player.pop())
        bandits.append(inexperienced_player.pop())
    return panthers, warriors, bandits





def displayMenuOptions(panthers, warriors, bandits):
    while True:
        menu()
        command = input("Please enter the number for the COMMAND that you want >   ")
        print()
        if command == '1':
            sub_menu()
            option = input("Please enter the number for the OPTION that you want >    ")
            if (option == '1'):
                print("TEAM name: Panthers")
                print_team_statistics(panthers)
            elif (option == '2'):
                print("TEAM name:Warriors")
                print_team_statistics(warriors)
            else:
                print("TEAM name: Bandits")
                print_team_statistics(bandits)
        elif command == '2':
            print("Good Bye.\n\n")
            break
        else:
            print("\nThat is not a valid option. Please can you try again. \n")
            continue
            
            
def menu():
    print()
    print('These are the two options for the Basketball Stats Tool')
    print("Type 1 to display team_stats")
    print("Type 2 to display to quit")
    
    
    
    
    
def sub_menu():
    print("Type 1 for panthers")
    print("Type 2 for warriors")
    print("Type 3 for bandits")
    
    
    
    
    
def main():
    print("Welcome to the Basketball Stats Tool")
    displayMenuOptions(constants.panthers, constants.warriors, constants.bandits) 
    
if __name__ == "__main__":
    main()
            
            

                                     