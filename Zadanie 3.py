ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

for ulica in ulice:
    for numer in range (0, 5):
        numer += 1
        for mieszkanie in range (0, 10):
            mieszkanie += 1
            adres = f"{ulica}, {numer}/{mieszkanie}"
            print(adres)