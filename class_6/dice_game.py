import random

def dice_game():
    player_bet = input("Place your bet! 🍀 Choose a number between 1 and 6: ")

    if not player_bet.isdigit():
        print("🙄 That's not even a number. Please choose a number between 1 and 6.")
        return

    player_bet = int(player_bet)

    if player_bet < 1 or player_bet > 6:
        print("🚫 Invalid input. Please choose a number between 1 and 6.")
        return
    
    dice_roll = random.randint(1, 6)
    
    print("🎲 Dice roll:", dice_roll)
    
    if player_bet == dice_roll:
        print("🥳 You WIN!")
    else:
        print("☹️ Sorry, you are not a winner.")

dice_game()