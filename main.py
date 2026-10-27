n = int(input("Zadaj číslo: "))
s = 0
while n > 0:
    c = n % 10
    s += c
    n//=10
print(f"Sucet cifier je {s}")