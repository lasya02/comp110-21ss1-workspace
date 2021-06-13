"""A program that explores the animal kingdom."""
from __future__ import annotations

__author__ = "730411126"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 3: Uncomment the following lines to test your classes
    lion = Animal("lion", 10, "\U0001F981")
    pig = Animal("pig", 3, "\U0001F437")
    ram = Animal("ram", 6, "\U0001F40F")
    elephant = Animal("elephant", 9, "\U0001F418")
    gorilla = Animal("gorilla", 7, "\U0001F98D")
    camel = Animal("camel", 4, "\U0001F42A")

    team1 = Team("Hello Kitty", [lion, ram, pig])
    team2 = Team("BIG", [elephant, gorilla, camel])

    winners = team1.battle(team2)

    print(f"{team1.team_name} vs {team2.team_name}")

    for i in range(len(team1.animals)):
        print(f"{team1.animals[i].emoji}  vs {team2.animals[i].emoji}")
        print(f"The {winners[i].species} wins!")
    print(team1.who_won(team2))


class Animal: 
    """An animal."""
    species: str = ""
    danger_level: int = 0 
    emoji: str = ""

    def __init__(self, s: str, dan: int, em: str): 
        """Initialize."""
        self.species = s
        self.danger_level = dan
        self.emoji = em
    
    def fight(self, opponent: Animal) -> Animal: 
        """Who wins?"""
        x = self.danger_level 
        y = opponent.danger_level
        if x > y: 
            return self
        elif x == y: 
            return opponent
        else: 
            return opponent
        

class Team: 
    """A Team."""
    team_name: str
    animals: list[Animal] = []
    score: int = 0

    def __init__(self, t: str, a: list[Animal]): 
        """Initialize."""
        self.team_name = t 
        self.animals = a
        self.score = 0 

    def battle(self, opponent: Team) -> list[Animal]: 
        """Battle."""
        winners: list[Animal] = []

        if len(self.animals) != len(opponent.animals): 
            return winners
        i = 0 
        while i < len(self.animals): 
            a = self.animals[i]
            b = opponent.animals[i]
            result = a.fight(b)
            if result == a: 
                winners.append(a)
                self.score += 1
            else: 
                winners.append(b)
                opponent.score += 1 
            i += 1 
            
        return winners

    def who_won(self, opponent: Team) -> str: 
        """Who won?"""
        a = self.score
        b = opponent.score 

        if a == 0 and b == 0: 
            return "The battle hasn't happened yet"
        elif a == b: 
            return "It was a tie!"
        elif a > b: 
            return f"Team {self.team_name} won!"
        else: 
            return f"Team {opponent.team_name} won!"


if __name__ == "__main__":
    main()