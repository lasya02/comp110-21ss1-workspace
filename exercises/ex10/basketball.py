"""A class to model a basketball game."""

__author__ = "730411126"


# TODO 1: Define the BBallGame class, and its logic, here.

class BBallGame: 
    """This is a basketball program."""
    biscuits: bool
    points: int 
    winning_team: str
    losing_team: str

    def __init__(self, p: int, w: str, lo: str): 
        """Initialize variables."""
        self.points = p 
        self.winning_team = w 
        self.losing_team = lo 
        self.biscuits = False 
    
    def check_points(self) -> None: 
        """Do we get free biscuits?"""
        if self.points > 100: 
            self.biscuits = True
        return None
    
    def winner(self) -> str: 
        """Did we win?"""
        if self.winning_team == "UNC": 
            if self.losing_team == "Dook": 
                return "GTHD!!"
            else: 
                return "woohoo"
        else: 
            return "daggum"

    def reset_points(self) -> int: 
        """Back to 0."""
        result: int = self.points 
        self.points = 0 
        return result