liczba = 2
licznik = 0
listaPerwsz = []

while licznik < 10:
    for i in range(2, liczba):
        if liczba % i ==0:
            break
    else:
        listaPerwsz.append(str(liczba))
        licznik += 1
    liczba += 1

print(", ".join(listaPerwsz))