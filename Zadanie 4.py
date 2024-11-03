przyjaciół = int(input("Podaj liczbę gośći: "))
potraw = int(input("Podaj liczbę zamówionych potraw:"))

całkowity_cost = 0

i = 1
while i <= potraw:
    cena = float(input(f"Podaj cenę potrawy {i}: "))
    całkowity_cost += cena
    i += 1

średnia_cena = całkowity_cost/potraw

cena_na_1_osob = całkowity_cost/przyjaciół

print(f"Średnia cena zamówionej potrawy {średnia_cena:.2f} zł")
print(f"Kwota do zapłaty na osobę: {cena_na_1_osob:.2f} zł")