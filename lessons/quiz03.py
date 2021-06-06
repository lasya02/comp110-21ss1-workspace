a = [10,20,30,90]
b = [30,40,50,100]

c: list[int] = []

print(c[0])

for i in range(len(a)):
    x = a[i] + b[i]
    c.append(x)

print(c)
