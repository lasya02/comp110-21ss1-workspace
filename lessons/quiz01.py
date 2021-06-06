def main() -> None: 
    b: list[str] = a 
    print(b)
    f(a)
    print(b)
    print("6")
    g()
    print(b)
    print("4")
    print(b[0])
    return None

def f(c: list[str]) -> None: 
    c[0] = "p"
    print(c)
    c = ['m','j']
    print(c)
    print("0")
    return None


def g() -> None: 
    global a
    a[1] = "y"
    print(a)
    print("7")
    a = ["k","g"]
    print(a) 
    print("1")
    return None


a: list[str] = ["w", 'u']

if __name__ == "__main__": 
    main()
    print(a)
    print("2")
