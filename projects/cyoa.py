"""Project 1!"""

from random import randint

__author__: str = "730411126"

YES = "yes"
NO = "no"
points: int = 15
player: str = ""
exit_1: bool = True
finish: bool = True
i: int = 1


def greet() -> None: 
    """Greets the user."""
    global player
    player = input("What is your name? ")
    print(f"Welcome to Jumanji, {player}! Looks are deciving ....")
    print("this is not a paradise and life or death choices await you at every turn.")
    return None


def crystal() -> None:
    """Pick a number and get an outcome in the game."""
    global player
    global points
    global exit_1
    global finish
    global YES
    global NO
    interact_1 = input("Pick a number between 1-50 ")
    interact = int(interact_1)
    if interact % 6 == 0: 
        print("Oh no! You've released bats.")
        if points >= 10: 
            print("Luckily you had a torch to fight off the bats")
            points += 5
        else: 
            print("Unfortunately, your panicked running from the bats caused you to get off course.")
            points -= 2
    elif interact % 8 == 0: 
        print("The mosquites are out of blood and they're headed right toward you.....")
        if points >= 20: 
            print("Not to worry though, your mosquito repellent keeps all your blood right where you want it.")
            points += 7
        else: 
            print("Looks like itching those bites is going to slow you down.")
            print("Hopefully, you have some repellent next time.")
            points -= 4
    elif interact % 4 == 0: 
        print("Look's like someone's not in Kansas in anymore and these monkey's seem to know it.")
        if points >= 30: 
            print("Huh? Look what you just found in your backpack ... a sack full of bananas. ")
            print("You might have some back problems later from lugging that around but for now, you're in the clear.")
            points += 10
        else:
            print("just your luck, you've lost your token in your hurry to get away. ")
            print("I guess we're going to have to go back and look for it.")
            points -= 5
    elif interact % 10 == 0: 
        print("Today must be your lucky day! You move on with no obstacles in your path.")
        print("I'd go try my luck at the lottery ... well, if you make it out of here")
        points += 13
    elif interact % 9 == 0: 
        print("You've released a player from the game.")
        points += 11
    elif interact % 3 == 0 and interact % 11 == 0: 
        print("uh oh ... why's the ground shaking? That crack looks like it's getting bigger.")
        print("... looks like you've gotten sucked into the game")
        if points >= 50: 
            print("someone must be looking out for you...")
            print("looks like they chose you to be released from the game.")
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
        print("You really should have recycled that paper cup .... ")
        print("looks like Mother Nature decided to enter the game.")
        print("The water level's rising ")
        if points >= 60: 
            print("oh my god i just remembered your hair glows when you sing ... oh wait wrong story")
            print("BUT, your backpack does have a map that shows you how to get out of this cave")
            print("better hurry up though ... the water's almost ")
            print("fryiii i nn gg    m y   ci r cu i t    s . ... . ... .")
            points += 23
        else: 
            print("sorry you drowned")
            exit_1 = False
            points -= 17
    else: 
        print("you've ........")
        print("WON!!!!")
        print("Congrats on escaping Jumanji")
        points = 100
        finish = False
    return None


def right_path() -> None:
    """Code for the path on the right side."""
    global player
    global points
    global exit_1
    global finish
    global YES
    global NO

    print("The path appears to be blocked by a large golden statue")
    print("As you approach, the fog clears and a clear voice breaks through the mist")
    print("'If you want to pass, you must correctly answer this riddle:'")
    print("Or .... take your chances with a shortcut. But I must warn you the stakes are high and the odds are low")
   
    y_s = input("Press 1 for the sphinx or 2 for the shortcut ")
    y = int(y_s)
    if y == 2: 
        a_s = input("Enter a number from 1 to 50 ... choose wisely ")
        a = int(a_s)
        if finish is True: 
            off = shortcut(a)
            print(f"Uh oh looks like you're falling into Jumanji and you were just {off} off from making it through")
            print("Well I did warn you about the odds")
    else: 
        sphinx()

    return None 


def sphinx() -> None:
    """Code for the sphinx."""
    global player
    global points
    global exit_1
    global finish
    global YES
    global NO

    x = randint(1, 3)
    passing: bool = False
    if x == 1: 
        response_1 = input("What goes on four feet in the morning, two feet at noon, and three feet in the evening? ")
        answer_1 = "person"
        if response_1 == answer_1: 
            passing = True
    elif x == 2: 
        print("There are two sisters: one gives birth to the other and she, in turn, gives birth to the first.")
        response_2 = input("Who are the two sisters? ")
        answer_2 = "day and night"
        if response_2 == answer_2: 
            passing = True
    else: 
        response_3 = input("I’m tall when I’m young, and I’m short when I’m old. What am I? ")
        answer_3 = "a candle"
        if response_3 == answer_3 or response_3 == "candle": 
            passing = True
    
    if passing is True: 
        finish = False
        points = 100
    else: 
        exit_1 = False
    
    return None


def shortcut(a: int) -> int: 
    """Code for the shortcut."""
    global player
    global points
    global exit_1
    global finish
    global YES
    global NO

    shortcut = randint(1, 50)
    if shortcut == a: 
        print("You have successfully escaped")
        points = 100
        finish = False
    else: 
        exit_1 = False
    
    b = abs(shortcut - a)
    return b


def final_outcomes() -> int: 
    """Code for the final outcome."""
    global player
    global points
    global exit_1
    global finish
    global YES
    global NO
    global i

    if finish is False: 
        print(f"Congrats, you've sucessfully escaped... with a total of {points} points")
        try_again = input("Want to try your luck again? ")
        if try_again == YES: 
            i = 1
        else: 
            i = 0
    elif exit_1 is False: 
        print(f"Unfortunately, it looks like Jumanji won this time ... you only had {points} points") 
        difference = 100 - points
        print(f"You were {difference} points away from escaping. ")
        try_again = input("Want to try your luck again? ")
        if try_again == YES: 
            i = 1
        else: 
            i = 0
    else: 
        print(f"You have {points} and need 100 to make it out.")
        try_again = input("Do you want to continue? ")
        if try_again == YES: 
            print("Do you want to continue on the same path or do you want to restart?")
            which_path = input("Press 1 to continue and 2 to restart: ")
            which_path_int = int(which_path)
            if which_path_int == 1: 
                crystal()
                final_outcomes()
            else: 
                i = 1
        else: 
            i = 0
    points = 15
    return i


def main() -> None:
    """Main function Code.""" 
    global player
    global points
    global exit_1
    global finish
    global YES
    global NO
    global i

    greet()
    print("As soon as you enter the game, you're faced with two paths.")
    print("both are filled by a thick fog so you can't see what lies behind")
    path_1 = input("Which path are you picking: left or right? ")
    left = "left"

    if path_1 == left: 
        crystal()
    else: 
        right_path()
    
    while i == 1: 
        i = final_outcomes()
        if i == 1:
            print("Do you want to re-enter the left path, right path, or at the shortcut or the sphinx?")
            path_str = input("1 for left, 2 for right, 3 for shortcut, 4 for sphinx ")
            path_int = int(path_str)
            if path_int == 1: 
                crystal()
            elif path_int == 2: 
                right_path()
            elif path_int == 3: 
                print("Looks like you decided to take your chances with a shortcut. ")
                print("But I must warn you the stakes are high and the odds are low")
                a_s = input("Enter a number from 1 to 50 ... choose wisely")
                a = int(a_s)
                shortcut(a)
            else: 
                print("The path appears to be blocked by a large golden statue")
                print("As you approach, the fog clears and a clear voice breaks through the mist")
                print("If you want to pass, you must correctly answer this riddle")
                sphinx()

    print(f"Come back soon,{player}")
    return None


if __name__ == "__main__":
    main()
    print(" ")
