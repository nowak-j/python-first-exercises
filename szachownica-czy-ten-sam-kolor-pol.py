# Rozważmy podstawową szachownicę.
# Pola szachownicy niech będą numerowane od 1 do 8 (w poziomie i pionie).
# Napisz program, który pobierze od użytkownika cztery liczby, reprezentujący odpowiednio pierwsze pole oraz drugie.
# Wynikiem programu ma być wartość True, jeżeli pola są w tym samym kolorze lub False w przeciwnym przypadku.

liczba_1 = int(input())
liczba_2 = int(input())
liczba_3 = int(input())
liczba_4 = int(input())
zielone = [11, 13, 15, 17, 22, 24, 26, 28, 31, 33, 35, 37, 42, 44, 46, 48, 51, 53, 55, 57, 62, 64, 66, 68, 71, 73, 75, 77, 82, 84, 86, 88]
białe = [12, 14, 16, 18, 21, 23, 25, 27, 32, 34, 36, 38, 41, 43, 45, 47, 52, 54, 56, 58, 61, 63, 65, 67, 72, 74, 76, 78, 81, 83, 85, 87]
pierwsze_pole = str(liczba_1) + str(liczba_2)
drugie_pole = str(liczba_3) + str(liczba_4)
if (liczba_1 > 8 or liczba_2 > 8 or liczba_3 > 8 or liczba_4 > 8 or liczba_1 <= 0 or liczba_2 <= 0 or liczba_3 <= 0 or liczba_4 <= 0):
    print("BŁĄD")
else:
    if (int(pierwsze_pole) in zielone and int(drugie_pole) in zielone):
        print("True")
    elif (int(pierwsze_pole) in białe and int(drugie_pole) in białe):
        print("True")
    else:
        print("False")