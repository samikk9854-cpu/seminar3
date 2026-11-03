import random
cislo = random.randint(0, 50)

while cislo != 0:
    print(cislo)
    if cislo % 2 == 0:
        print("Cislo je parne")
    else:
        print("Cislo je neparne")
    cislo = random.randint(0, 50)
print(f"Ciselko je {cislo} koniec")