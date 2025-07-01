import random

def roll_dice(num_dice,num_sides):
    rolls=[]

    for el in range(num_dice):
        roll = random.randint(1,num_sides)
        rolls.append(roll)

    return rolls
def main():
    print("🎲 welcome to the Dice Roller Simulator!")

    while True:
        try:

            num_dice = int(input("How many dice do you want to roll?"))
            num_sides = int(input("How many sides should each die have?"))
        except ValueError:
            print("Please enter a valid number-")
            continue

        
        results = roll_dice(num_dice,num_sides)
        print(f'\nYou rolled: {results}')
        print(f'Total:{sum(results)}\n')

        again = input("Do you want to roll the dice again? (y/n)").lower()
        if again != "y":
            print("Thanks for playing!")
        else:
            print("Thanks for playing this game another time 😊")

if __name__=="__main__":
     main()
            
