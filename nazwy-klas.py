# Napisz program, który pobierze od użytkownika liczbę oraz literę z alfabetu łacińskiego.
# Wynikiem programu mają być nazwy klas w postaci: liczba_litera.

# Sample Input:
#   6
#   d

# Sample Output:
#   1a,1b,1c,1d
#   2a,2b,2c,2d
#   3a,3b,3c,3d
#   4a,4b,4c,4d
#   5a,5b,5c,5d
#   6a,6b,6c,6d

liczba = int(input())
litera = str(input())

for i in range(1,liczba+1):
    akt_litera = "a"
    while akt_litera <= litera:
        print(str(i)+akt_litera, end="")
        if akt_litera != litera:
            print(",", end="")
        akt_litera = chr(ord(akt_litera)+1)
    print("")