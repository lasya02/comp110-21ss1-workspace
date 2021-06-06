"""A program to determine top favorite colors."""

__author__ = "730411126"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    colors = {"anna": "blue", "kris": "green", "sarah": "blue", "shaurik": "blue"}
    print(favorite_color(colors))
    return None


def favorite_color(colors: dict[str, str]) -> str: 
    """What is the favorite color?"""
    count: dict[str, int] = {}
    for keys in colors: 
        if colors[keys] not in count: 
            count[colors[keys]] = 1
        else: 
            count[colors[keys]] += 1
    max = 0 
    color = ""
    for keys in count: 
        if count[keys] > max: 
            max = count[keys]
            color = keys
    return color
    

if __name__ == "__main__":
    main()