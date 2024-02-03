import random

def dice_game():
    player_bet = input("Place your bet! 🍀 Choose a number between 1 and 6: ")
    
    dice_roll = random.randint(1, 6)
    
    print("🎲 Dice roll:", dice_roll)
    
    if player_bet == dice_roll:
        print("🥳 You WIN!")
    else:
        print("☹️ Sorry, you are not a winner.")

dice_game()