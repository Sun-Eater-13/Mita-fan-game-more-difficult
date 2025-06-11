import random

player_points=0
Mita_points=0
fighting_choices=(0, 1, 2)
player_chosen_card=0
deck_player=[(3,10,5), (6,2,8), (7,0,0), (10,0,2), (5,0,10), (6,2,8), (3,8,1), (7,0,0)]
deck_Mita=[(3,10,5), (6,2,8), (7,0,0), (10,0,2), (5,0,10), (6,2,8), (3,8,1), (7,0,0)]

def convert_into_text():
    match fighting_value:
        case 0:
            return "left"
        case 1:
            return "middle"
        case _:
            return "right"

def starting_round():
    print(f"The value used in this round is the {convert_into_text()} value.")
    print("This is your current deck:")
    for card in range(0, len(deck_player)):
        print(f"card_number_{card+1}: {deck_player[card]}")

def player_choosing_card(deck_player):
    global player_chosen_card
    while True:
        try:
            player_chosen_card = int(input(f"Choose your card. Type 1 to {len(deck_player)}: "))
            print("")
            if player_chosen_card < 1 or player_chosen_card > len(deck_player):
                print("Choose again correctly.")
            else:
                print(f"You chose card {player_chosen_card}. It\'s values are: {deck_player[player_chosen_card-1]}")
                print(f"Your value taken into account in this round is: {deck_player[player_chosen_card-1][fighting_value]}")
                break
        except ValueError:
            print("Choose again correctly.")

def check_if_win():
    match player_points:
        case _ if player_points>Mita_points:
            return "You won the whole game."
        case _ if player_points<Mita_points:
            return "Mita won the whole game."
        case _:
            return "The whole game ended in a draw."

def Mita_choosing_card(fighting_value):
    temporary_Mita_card=deck_Mita[0]
    for card in deck_Mita:
        if temporary_Mita_card[fighting_value]<card[fighting_value]:
            temporary_Mita_card=card
    return temporary_Mita_card

print(f"""
This is a game inspired by mini game from game MiSide. The game have 8 rounds.
You will get eight cards. Each of them will have 3 values for simplicity called left, middle and right.
At the begging of each round there will be drawn randomly which of them will be taken into account during current round.
Then You will have to choose a card from your deck. Next, your opponet called Mita will choose her card.
The player with the higher value will win and get 1 point. In case of draw, neither player will get any points.\n
This is your starting deck: {deck_player}
Mita has the same starting deck. Player with more points after 8 round will win the whole game.\n""")

while True:
    accept=input("Press enter to start the game\n")
    if accept!="" or accept=="":
        break

while len(deck_player)!=0:
    fighting_value = random.choice(fighting_choices)
    starting_round()
    player_choosing_card(deck_player)
    Mita_card = Mita_choosing_card(fighting_value)
    print(f"\nThe card chosen by Mita is {Mita_card}")
    print(f"Mita\'s value taken into account in this round is: {Mita_card[fighting_value]} \n")
    if Mita_card[fighting_value] > deck_player[player_chosen_card - 1][fighting_value]:
        Mita_points += 1
        print(f"Mita won this round.\nYour points: {player_points}. Mita\'s points: {Mita_points}\n")
    elif Mita_card[fighting_value] < deck_player[player_chosen_card - 1][fighting_value]:
        player_points += 1
        print(f"You won this round. \nYour points: {player_points}. Mita\'s points: {Mita_points}\n")
    else:
        print(f"It\'s draw in this round. \nYour points: {player_points}. Mita\'s points: {Mita_points}\n")
    deck_Mita.remove(Mita_card)
    deck_player.pop(player_chosen_card - 1)
    if len(deck_player)==0:
        print(f"This is the end of the game. The score is You {player_points} - {Mita_points} Mita. {check_if_win()}")
        play_again=input("Do You want to play again? Press X and enter for yes. Press antyhing else and enter to quit. ")
        if play_again.lower()=="x":
            deck_player = [(3, 10, 5), (6, 2, 8), (7, 0, 0), (10, 0, 2), (5, 0, 10), (6, 2, 8), (3, 8, 1), (7, 0, 0)]
            deck_Mita = [(3, 10, 5), (6, 2, 8), (7, 0, 0), (10, 0, 2), (5, 0, 10), (6, 2, 8), (3, 8, 1), (7, 0, 0)]
            player_points = 0
            Mita_points = 0
            print("\nThe game starts again.")
        else:
            print("\nThank You for playing.")