"""A program to determine names over 21."""

__author__ = "730411126"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 2: Test your function here
    i = 1
    inputing: dict[str, int] = {}
    while i == 1: 
        name = input("Enter a name of a person ")
        year_str = input("What year were they born? ")
        year = int(year_str)
        inputing[name] = year 
        continuing = input("Do you want to add more? yes/no ")
        if continuing == "yes": 
            i = 1 
        else: 
            i = 0 
    print(inputing)
    print(over_21(inputing))
    return None


def over_21(age: dict[str, int]) -> list[str]: 
    """Are people over 21?"""
    old: list[str] = []
    for values in age: 
        if age[values] <= 2000: 
            old.append(values)
    return old


if __name__ == "__main__":
    main()