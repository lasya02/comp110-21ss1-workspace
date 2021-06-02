"""Examples of dictionaries."""

#dict[key type, value type]

players: dict[str,int]= {}

players["Brooks"] = 15
players["Bacot"] = 4 
players["Love"] = 2 

players["Bacot"] = players["Bacot"] + 1 

print(players)

new_dict: dict[str,str] = {"Kaki": "blue", "Lasya": "Green"}
new_dict["Matt"] = "Red"

removed = new_dict.pop("Matt")

print(new_dict)

for key in new_dict: 
    print(f"The key is {key} and the value is {new_dict[key]}")

for value in new_dict.values(): 
    print(f"The value is {value}")


def passes(students: dict[str,float]) -> list[str]:
    """Given student info, who passes?"""
    result: list[str] = []
    for student in students:
        if students[student] > 60: 
            result.append(student)
    return result

s: dict[str, float] = {"Andrew": 100.0, "Shaurik": 89.0, "Claire": 40.0}
print(passes(s))
