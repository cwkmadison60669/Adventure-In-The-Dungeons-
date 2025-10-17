import random, import time
inventory = {}

def enter_dungeon():
    response = input("You take a hike to the mountains and saw a cave. There is a terrible storm outside and you need shelter. The cave is dark and quiet. Would you like to enter the dungeon?") 
    if response.lower() == "yes":
        print = "You have entered the cave."
    elif response.lower() == "no":
        print = "You have died from the storm."
    else: 
        print = "Invalid choice"

def pickup_sword():
    sword = input("You walk into the cave and see that there is a dragon sleeping. You also see there is a sword on the ground. Would you like to pick it up?")
    if sword.lower() == "yes":
        print = "You have collected a sword"
    elif sword.lower() == "no":
        print = "Oh no, the dragon has awaken and you have nothing to defend yourself, you have died!"
    else: 
        print = "Invalid choice"

def fight_dragon():
    fight = input("You accidentally stepped on a twig and woken up the dragon. Do you want to fight it?")


