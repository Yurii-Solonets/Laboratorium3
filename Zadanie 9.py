# 9_1
imię = input("Podaj swoje imię: ")
print(f"Witaj {imię}!")

# 9_2
wiek = input("Podaj swój wiek: ")
print(f"Twój wiek to: {wiek}")

# 9_3
imię_nazwisko = input("Podaj swoje imię i nazwisko: ")
imię, nazwisko = imię_nazwisko.split()
inicjały = imię[0].upper() + nazwisko[0].upper()
print(f"Iniciały: {inicjały}")

# 9_4
łańcuch = input("Podaj łańcuch: ")
for _ in range(5):
    print(łańcuch)

# 9_5
łańcuch1 = input("Podaj pierwszy łańcuch: ")
łańcuch2 = input("Podaj drugi łańcuch: ")
polaczony = łańcuch1 + łańcuch2
print(f"Połączony łańcuch: {polaczony}")

# 9_6
łańcuch3 = input("Podaj pierwszy łańcuch: ")
łańcuch4 = input("Podaj drugi łańcuch: ")
połowa = łańcuch3[:len(łańcuch3) //2 ]
print(f"Pierwsza połowa pierwszego łańcucha: {połowa}")