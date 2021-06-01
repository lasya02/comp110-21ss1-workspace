"""Project 1"""

from random import randint

__author__: str = "730411126"


points: int = 15
player: str = ""
exit_1: bool = True
finish: bool = True

#greeting the player 
def greet() -> None: 
    global player
    player = input("What is your name? ")
    print("Welcome to Jumanji, {player}! Looks are deciving .... this is not a paradise and life or death choices await you at every turn.")
    return None

def crystal () -> None: 
    """Pick a number and get an outcome in the game"""

    global points
    global exit_1
    interact_1 = input("Pick a number between 1-50 ")
    interact = int(interact_1)
    if interact % 6 == 0: 
        print("Oh no! You've released bats.")
        if points >= 10: 
            print("Luckily you had a torch to fight off the bats")
            points += 5
        else: 
            print("Unfortunately, your panicked running from the bats caused you to get off course.")
            points -=2
    elif interact % 8 == 0: 
        print("The mosquites are out of blood and they're headed right toward you.....")
        if points >= 20: 
            print("Not to worry though, your mosquito repellent keeps all your blood right where you want it.")
            points += 7
        else: 
            print("Looks like itching those bites is going to slow you down. Hopefully, you have some repellent next time.")
            points -= 4
    elif interact % 4 == 0: 
        print("Look's like someone's not in Kansas in anymore and these monkey's seem to know it.")
        if points >= 30: 
            print("Huh? Look what you just found in your backpack ... a sack full of bananas. You might have some back problems later from lugging that around but for now, you're in the clear.")
            points += 10
        else:
            print("well ... those screams weren't that dignified. And just your luck, you've lost your token in your hurry to get away. I guess we're going to have to go back and look for it.")
            points -= 5
    elif interact % 10 == 0: 
        print("Today must be your lucky day! You move on with no obstacles in your path. I'd go try my luck at the lottery ... well, if you make it out of here")
        points += 13
    elif interact % 9 == 0: 
        print("You've released a player from the game.")
        points += 11
    elif interact % 3 == 0 and interact % 11 == 0: 
        print("uh oh ... why's the ground shaking? That crack looks like it's getting bigger.")
        print("... looks like you've gotten sucked into the game")
        if points >= 50: 
            print("someone must be looking out for you... looks like they chose you to be released from the game. Sheeesh, that was a close call wasn't it")
            points += 17
        else: 
            print("God, it's brutal out here ....")
            points -= 8
            exit_1 = False
    elif interact % 5 == 0: 
        print("What's that dropping from the ceiling?????")
        print("Ahhhhh it's getting everywhere and that smell must mean it's ......")
        print("Devil's Snare")
        if points >= 40: 
            print("But not to worry, even the devil can't overpower the sun rock.")
            points += 16
        else: 
            print("ahhh this is going to take a while to get out of")
            points -= 11
    elif interact % 7 == 0: 
        print("You really should have recycled that paper cup .... looks like Mother Nature decided to enter the game.")
        print("The water level's rising ")
        if points >= 60: 
            print("oh my god i just remembered your hair glows when you sing ... oh wait wrong story")
            print("BUT ... your backpack does have a map that shows you the best way to get out of this cave and onto high ground")
            print("better hurry up though ... the water's almost fryiii i nn gg    m y   ci r cu i t    s . ... . ... .")
            points += 23
        else: 
            print ("sorry you drowned")
            exit_1 = False
            points -= 17
    else: 
        print("you've ........")
        print("WON!!!!")
        print("Congrats on escaping Jumanji ... come back and play if you're ever looking for an adrenaline rush or ... worse")
        points = 100
        finish = False
    return None

def sphinx() -> None:
    print("The path appears to be blocked by a large golden statue")
    print("As you approach, the fog clears and a clear voice breaks through the mist")
    print("If you want to pass, you must correctly answer this riddle")

    x = randint(1,3)
    passing: bool = False
    if x == 1: 
        response_1 = input("What goes on four feet in the morning, two feet at noon, and three feet in the evening? ")
        answer_1 = "person"
        if response_1 == answer_1: 
            passing = True
    elif x == 2: 
        response_2 = input("There are two sisters: one gives birth to the other and she, in turn, gives birth to the first. Who are the two sisters?")
        answer_2 = "day and night"
        if response_2 == answer_2: 
            passing = True
    else: 
        response_3 = input("I’m tall when I’m young, and I’m short when I’m old. What am I?")
        answer_3 = "a candle"
        if response_3 == answer_3: 
            passing = True
    
    if passing == True: 
        finish = False
    else: 
        exit_1 = False
    
    return None

def shortcut(a: int) -> int: 
    shortcut = randint(1,50)
    if shortcut == a: 
        print("You have successfully escaped")
        points = 100
    else: 
        print("Looks like ")
    return b

def main() -> None: 
    greet()
    print("As soon as you enter the game, you're faced with two path, both surrounded by fog so you can't see what lies behind.")
    path_1 = input("Which path are you picking: left or right? ")
    left = "left"
    right = "right"
    if path_1 == left: 
        crystal()
    else: 
        sphinx()
    return None

if __name__ == "__main__":
    main()