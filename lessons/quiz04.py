def main() -> None: 
    word = input("enter a word; ")
    funny = is_funny(word)
    print(funny)

def is_funny(word: str) -> bool: 
    if len(word) < 3: 
        return False 
    
    i = 0 
    while i < len(word): 
        if not_funny(word[i]): 
            return False
        i += 1

    return True 

def not_funny(Char: str) -> bool: 
    return Char != "h" and Char != "a"

if __name__ == "__main__": 
    main()
    