import constants
from copy import deepcopy


def print_team_statistics(local_team):
    players_on_team = [player['name'] for player in local_team]
    guardians_on_team = [player['guardians'] for player in local_team]
    print(f'the total count of players on team = {len(players_on_team)}')
    experienced_players = len([player['experience'] for player in local_team if player['experience'] == True])
    inexperienced_players = len([player['experience'] for player in local_team if player['experience'] == False])
    print(f'the number of experienced players = {experienced_players}')
    print(f'the number of inexperienced players = {inexperienced_players}')
    height_on_team = [player['height'] for player in local_team]
    height_on_team_in_strings = [str(player['height']) for player in local_team]
    print('The name of my players are')
    print(", ".join(players_on_team))
    print('The guardians of my players are')
    print(", ".join(guardians_on_team))
    print(f'average_height_team = {sum(height_on_team)/len(players_on_team)}')
    print()
    
    
def processPlayers():
    players = deepcopy(constants.PLAYERS)
    for player in players:
        
        
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experince'] = False
        height = player['height'].split()
        player['height'] = int(height[0])
    return players

def assignPlayersToTeam(players):
    teams = constants.TEAMS[:]
    panthers = []
    bandits = []
    warriors = []
    
    experienced_player = []
    non_experienced_player = []
    for player in players:
        if player['experience'] == True:
            experienced_player.append(player)
        else:
            non_experienced_player.append(player)
            
            
        while experienced_player:
            panthers.append(experienced_player.pop())
            warriors.append(experienced_player.pop())
            bandits.append(expereienced_player.pop())
        while non_experienced_player:
            panthers.append(non_experienced_player.pop())
            warriors.append(non_experienced_player.pop())
            bandits.append(non_experienced_player.pop())
        return panthers, warriors, bandits
    
    
def displayMenuOptions(panthers, warriors, bandits):
    while True:
        menu()
        command = input("Please enter the number for the COMMAND that you want >  ")
        print()
        if command == '1':
            sub_menu()
            option = input("Please enter the number for the OPTION that you want >  ")
            if (option == '1'):
                print("TEAM name: Panthers")
                print_team_statistics(panthers)
            elif (option == '2'):
                print("TEAM name: Warriors")
                print_team_statistics(warriors)
            else:
                print("TEAM name: Bandits")
                print_team_statistics(bandits)
        elif command == '2':
            print("Good bye.\n\n")
            break
        else:
            print("\nThat is not a valid option. Please try again. \n")
            continue
            
def menu():
    print()
    print('These are the options for the Basketball Stats Tool')
    print("type 1 to display team_stats")
    print("type 2 to display to quit")
    
def sub_menu():
    print("type 1 for panthers")
    print("type 2 for warriors")
    print("type 3 for bandits")
    
def main():
    print("Hello, welcome to the basketball game")
    new_player_list = processPlayers()
    panthers, warriors, bandits = assignPlayersToTeam(new_player_list)
    displayMenuOptions(constants.panthers, constants.warriors, constants.bandits)
    
    
    
if __name__ == '__main__':
    main()
    
            
   
