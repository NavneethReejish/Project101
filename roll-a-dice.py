import random

def roll_dice():
    response = "y"
        
    while response.lower() == "y":
        dice_value = random.randint(1, 6)
            
        # Display the dice face based on the random value
        if dice_value == 1:
            print("---------")
            print("|       |")
            print("|   •   |")
            print("|       |")
            print("---------")
        elif dice_value == 2:
            print("---------")
            print("| •     |")
            print("|       |")
            print("|     • |")
            print("---------")
        elif dice_value == 3:
            print("---------")
            print("| •     |")
            print("|   •   |")
            print("|     • |")
            print("---------")
        elif dice_value == 4:
            print("---------")
            print("| •   • |")
            print("|       |")
            print("| •   • |")
            print("---------")
        elif dice_value == 5:
            print("---------")
            print("| •   • |")
            print("|   •   |")
            print("| •   • |")
            print("---------")
        elif dice_value == 6:
            print("---------")
            print("| •   • |")
            print("| •   • |")
            print("| •   • |")
            print("---------")

        response = input("Press y to roll again, and n to exit: ")