tekst = "Python jest super"

zerowy_ind = tekst[0]
print(f"Zerowy indeks: {zerowy_ind}")

ostatni_ind = tekst[-1]
print(f"Ostatni indeks: {ostatni_ind}")

co_drugi = tekst[::2]
print(f"Co drugi znak, zaczynając od zerowego: {co_drugi}")

co_trzeci = tekst [1::3]
print(f"Co trzeci znak, zaczynając od pierwszego: {co_trzeci}")

od_dziesiątego = tekst[9:]
print(f"Od dziesiątego do ostatniego: {od_dziesiątego}")

od_konca_do_poczatku = tekst[::-1]
print(f"Od końca do początku: {od_konca_do_poczatku}")