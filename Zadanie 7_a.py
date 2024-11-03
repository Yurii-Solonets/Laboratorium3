n = int(input("Podaj liczbę studentów: "))
suma_punktów = 0
liczba_studentów = 0

while liczba_studentów < n:
    punkty = int(input(f"Podaj punkty dla studenta {liczba_studentów + 1}: "))

    if punkty < 0 or punkty > 100:
        print("Punkty muszą być w zakresie 0-100. Proszę podać ponowie. ")
        continue

    suma_punktów += punkty
    liczba_studentów += 1

if liczba_studentów > 0:
    średnie = suma_punktów / liczba_studentów
    print(f"Średnia liczba punktów w grupie: {średnie:.2f}")
else:
    print("Brak danych do obliczenia średniej.")