#!/usr/bin/env python3
import random
import time
# defining the dice
def roll_d20():
    d20result = random.randint(1, 20)
    return d20result
def roll_d12():
    d12result = random.randint(1, 12)
    return d12result
# main function
def main():
    # defining player and goblin hp
    goblin_hp = 20
    player_hp = 20
    print("You encounter a goblin!")
    # creating a while loop to continue the encounter past the first round
    while player_hp > 0 and goblin_hp > 0:
        input("Press Enter to roll a d20 to hit the goblin...")

        # Dice variables
        d20result = roll_d20()
        d12result = roll_d12()
        gd20result = roll_d20()
        gd12result = roll_d12()
        # your roll results
        print(f"\nYou rolled a {d20result}.")
        if d20result >= 10:
            print('You scored a hit on the goblin!')
            time.sleep(2)
            input('Press Enter to roll your d12 for damage...')
            dmg_roll = d12result
            goblin_hp -= dmg_roll
            print(f'\nYou hit the goblin for {dmg_roll} damage!')
            # checking to see if the goblin is dead before he can counter 
            if goblin_hp <= 0:
                print("The goblin is defeated!")
                break

            print('The goblin is counterattacking!')
            time.sleep(2)

        else:
            print('You missed! The goblin prepares to counterattack...')
            time.sleep(2)
        # the goblins roll
        print('\nThe goblin swings his axe at you!')
        if gd20result >= 10:
            gdmg_roll = gd12result
            player_hp -= gdmg_roll
            print(f'The goblin hits you with his axe for {gdmg_roll} damage!')
            time.sleep(2)
        else:
            print('The goblin misses you! What a fool!')
            time.sleep(2)
    # checking if the player is dead
    if player_hp <= 0:
        print("\nYou have been defeated. How Tragic...")
    else:
        print("\nYou have defeated the goblin! songs will be sung of your success!")




main()
