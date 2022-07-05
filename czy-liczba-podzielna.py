# Napisz program, który będzie przerabiał liczbę otrzymaną przez użytkownika według następujących zasad:

# Jeżeli liczba jest podzielna przez 3 to program powinien wyświetlić słowo Pling
# Jeżeli liczba jest podzielna przez 5 to program powinien wyświetlić słowo Plang
# Jeżeli liczba jest podzielna przez 7 to program powinien wyświetlić słowo Plong
# Jeżeli nie zachodzi żaden z powyższych przypadków program powinien wyświetlić otrzymaną liczbę
# Jeżeli liczba będzie podzielna przez 3 oraz 5, to program powinien wypisać PlingPlang.

liczba = int(input())
if liczba % 3 == 0 and liczba % 5 == 0 and liczba % 7 == 0:
    print("PlingPlangPlong")
elif liczba % 3 == 0 and liczba % 7 == 0:
    print("PlingPlong")
elif liczba % 3 == 0 and liczba % 5 == 0:
    print("PlingPlang")
elif liczba  % 5 == 0 and liczba % 7 == 0:
        print("PlangPlong")
elif liczba % 3 == 0:
    print("Pling")
elif liczba % 5 == 0:
    print("Plang")
elif liczba % 7 == 0:
    print("Plong")
else:
    print(liczba)
