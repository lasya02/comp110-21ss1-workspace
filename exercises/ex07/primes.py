"""An exercise with functions and lists."""

__author__ = "730411126"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    first_str = input("Enter a number ")
    second_str = input("Enter another greater number ")
    first = int(first_str)
    second = int(second_str)
    print(list_primes(first, second))
    return None


def is_prime(a: int) -> bool: 
    """If this is prime, then true."""
    prime = False
    x: list[int] = []
    for values in range(2, a):
        if a % values == 0: 
            x.append(values)
    if len(x) > 0: 
        prime = False
    else: 
        prime = True
    if a <= 1: 
        prime = False
    return prime


def list_primes(x: int, y: int) -> list[int]: 
    """This makes a list."""
    primes: list[int] = []
    checking = range(x, y, 1)

    for values in checking: 
        prime_or_not = is_prime(values)
        if prime_or_not is True: 
            primes.append(values) 
    return primes


if __name__ == "__main__":
    main()