paliwo = 100
paliwo_zużyte_na_czas = 10
czas = 0

while paliwo > 0:
    print(f"Czas lotu: {czas} s, pozostałe paliwo: {paliwo} litrów")

    paliwo -= paliwo_zużyte_na_czas
    czas += 1

    if paliwo < 0:
        print("Koniec lotu")
        break