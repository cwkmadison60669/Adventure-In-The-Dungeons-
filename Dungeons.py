# Great start Maddy! I like that you are separating the different parts of the map with functions!
# I will be adding comments throughout to help you further throughout the code!


import random
import time
# As stated in the slideshow, this should be a list!
inventory = {}

def enter_dungeon():
    response = input("You take a hike to the mountains and saw a cave. There is a terrible storm outside and you need shelter. The cave is dark and quiet. Would you like to enter the dungeon?") 
    # All of your print statements are being set as a variable with the words. To actually print things you need to do
    # print("words are entered here")

    # Another thing to note is, after the user enters yes/no think about what function should be called
    # example: When you say yes to entering the cave, it should ask about the torch vs sword. After that "pick up sword"
    #           method should be called
    if response.lower() == "yes":
        print = "You have entered the cave."

    # If the user has died here. You need to break the program all together.
    elif response.lower() == "no":
        print = "You have died from the storm."
    # Great work Maddy!
    else: 
        print = "Invalid choice"

def pickup_sword():
    sword = input("You walk into the cave and see that there is a dragon sleeping. You also see there is a sword on the ground. Would you like to pick it up?")
    if sword.lower() == "yes":
        print = "You have collected a sword"
    # If the user has died here. You need to do what to stop the program?
    elif sword.lower() == "no":
        print = "Oh no, the dragon has awaken and you have nothing to defend yourself, you have died!"
    else: 
        print = "Invalid choice"

def fight_dragon():
    fight = input("You accidentally stepped on a twig and woken up the dragon. Do you want to fight it?")

# Remember at the end you will need to call the main function to start the program

