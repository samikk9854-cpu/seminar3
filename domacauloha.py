#4
x = int(input("Zadaj číslo: "))
for i in range (0, x+1):
    print(i, end=" ")
    print(i**2)

#5
o = int(input("Zadaj číslo od: "))
d = int(input("Zadaj čislo do: "))
for i in range (o, d+1):
    print(i, end=" ")
    print(round(i**0.5, 2))

#6
for x in range (1,21):
    if x == 3:
        print("funkcia  nieje definovaná")
    else:
        y=(x ** 2 - 1)/(x - 3)
        print(y)

#7
n = int(input("Zadaj číslo: "))
for i in range (0, n+1, 3):
    print(i)

#8
for i in range (1, 21, 2):
    print(i)

#9
z = int(input("Zadaj číslo 1: "))
k = int(input("Zadaj číslo 2: "))
for i in range (z, k+1):
    if i % 2 == 1:
        print(i)

#10
g = int(input("Zadaj G: "))

for i in range(g, 0, -1):
 if i == 1:
     print(i, end="")
 else:
     print(i, end=", ")

