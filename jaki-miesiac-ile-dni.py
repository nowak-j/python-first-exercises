# Napisz program, który dla podanej liczby z odpowiedniego zakresu wyświetli jaki to miesiąc i ile ma on dni.
# Zakładamy, że rok tutaj nie jest przestępny.
# W przypadku niepoprawnych danych program ma wypisać komunikat: BŁĄD

liczba = input()
if (liczba == "1"):
    print("Styczeń: 31 dni")
elif (liczba == "2"):
    print("Luty: 28 dni")
elif (liczba == "3"):
    print("Marzec: 31 dni")
elif (liczba == "4"):
    print("Kwiecień: 30 dni")
elif (liczba == "5"):
    print("Maj: 31 dni")
elif (liczba == "6"):
    print("Czerwiec: 30 dni")
elif (liczba == "7"):
    print("Lipiec: 31 dni")
elif (liczba == "8"):
    print("Sierpień: 31 dni")
elif (liczba == "9"):
    print("Wrzesień: 30 dni")
elif (liczba == "10"):
      print("Październik: 31 dni")
elif (liczba == "11"):
      print("Listopad: 30 dni")
elif (liczba == "12"):
      print("Grudzień: 31 dni")
else:
      print("BŁĄD")