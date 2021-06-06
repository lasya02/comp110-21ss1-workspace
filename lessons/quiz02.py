def zip_dict(ks: list[str], vs: list[str]) -> dict[str,str]: 
    d: dict[str,str] = {}

    if len(ks) != len(vs): 
        return d 
    print(ks)
    print(vs)
    
    i = 0
    while i < len(ks): 
        d[ks[i]] = vs[i]
        print(d)
        i += 1

    return d 

a = ["ROY", "UNC", "ROY", "UNC"]
b = ["hi", "w", "bye", "L"]
c: dict[str,str] = zip_dict(a,b)
print(c)