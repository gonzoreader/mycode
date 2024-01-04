#!/usr/bin/env python3


def main():

    choice = input("You are standing at a crossroad.\n There are four directions you can go in, North, West, East, or South.\n There is a sign with names of towns at the crossroads\n What do you do?")
    if choice == "go west":
        print(f"You head west, and soon see a gigantic cavern at the foot of a cliff.")
    elif choice == "go east":
        print(f"You wander eastward until you stumble upon a small child. He looks cold, and is crumpled up into a ball on the side of the road.")
    elif choice == "go south":
        print(f"You amble southward at a steady pace, the wind seeming to tug at your cloak.")
    elif choice == "go north":
        print(f"After around 3 hours of walking you find yourself at the entrance to an enchanted forest.")
    elif choice == "read sign":
        print(f"The sign looks old and beaten. One of the pieces is broken down the middle and is illegible. You make out 'North to Breki Forest, South to The wastes, West to the Forbidden Cavern, East to-'")
    else:
        print(f"You must have hit your head recently, you dont know how to do that")
main()
