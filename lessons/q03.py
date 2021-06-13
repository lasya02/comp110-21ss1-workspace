
from __future__ import annotations

class Yikes: 
    x: int = 0 
    def __add__(self, rhs: Yikes) -> int: 
        self.x += rhs.x
        return self.x 

a = Yikes()
a.x = 5 
b = Yikes()
b.x = 10 
c = a + b
print(a.x)
print(b.x)
d = b + a 
print(b.x)
print(a.x)

print(c)
print(d)

x = 3.0 * 3.0 
y = 3.14 * 10.0 * 10.0 
print(x + y)