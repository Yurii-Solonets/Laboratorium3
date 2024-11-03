while True:
    number = int(input("Podaj liczbę całkowity: "))
    if number < 0:
        print("Podano liczbę ujemną.")
        break
    else:
        print(f"Podano liczbę: {number}")