import constants
import copy


players_copy = copy.deepcopy(constants.PLAYERS)





def clean_data():
    int_player_height()
    bool_player_exp()


    

    
def int_player_height():
    for player in players_copy:
        player_inches = player['height'].split(' ')
        player_height_num = int(player_inches[0])
        player['height'] = player_height_num



        
        
def bool_player_exp():
    for player in players_copy:
        experience_test = player['experience']
        if experience_test == 'YES':
            player['experience'] = True
        elif experience_test == 'NO':
            player['experience'] = False


            

            
def balance_teams():
    num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)
    
    panthers = []
    bandits = []
    warriors = []
    all_teams = [panthers, bandits, warriors]
    num_teams = len(all_teams)
    for num in range(len(players_copy)):
        all_teams[num % num_teams].append(players_copy[num])
    return (panthers, bandits, warriors)







def menu():
    print('\n\n BASKETBALL TEAM STATS TOOL \n\n')
    print('\n----- Main Menu -----\n')
    print('\nThese are your choices:\n\n 1) View Team Stats\n 2) Quit The Program')
    choice = input('\nPlease enter your option > ')
    if choice == '1':
        print('\n 1) Panthers\n 2) Bandits\n 3) Warriors')
        team_select = input('\nEnter your option > ')
        if team_select == '1':
            panther_list = balance_teams()[0]
            player_amount = len(panther_list)
            print('\nTeam: Panthers Stats\nPlayers: {}\n'.format(player_amount))
            names_list1 = []
            for player in panther_list:
                player_names = player['name']
                names_list1.append(str(player_names))
            print("Players Names:")
            print(", ".join(names_list1))
            print('\n\nThank you for using Basketball Stats Tool! \n\n')
        elif team_select == '2':
            bandit_list = balance_teams()[1]
            player_amount = len(bandit_list)
            print('\nTeam: Bandits Stats\nPlayers: {}\n'.format(player_amount))
            names_list2 = []
            for player in bandit_list:
                player_names = player['name']
                names_list2.append(str(player_names))
            print("Players Names:")    
            print(", ".join(names_list2))
            print('\n\nThank you for using Basketball Stats Tool! \n\n')
        elif team_select == '3':
            warrior_list = balance_teams()[2]
            player_amount = len(warrior_list)
            print('\nTeam: Warrior Stats\nPlayers: {}\n'.format(player_amount))
            names_list3 = []
            for player in warrior_list:
                player_names = player['name']
                names_list3.append(str(player_names))
            print("Players Names:")    
            print(", ".join(names_list3))
            print('\n\nThank you for using Basketball Stats Tool! \n\n')       
    elif choice == '2':
        print("Goooood byeeee.\n\n")
    else:
        print("Oooops!That's not a valid option. Please try again. \n")
        




        
if __name__ == '__main__':
    clean_data()
    balance_teams()
    menu()
