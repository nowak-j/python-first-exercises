# Napisz program, który najpierw pobiera liczbę naturalną nn, a następnie do słownika wrzuca nn par typu klucz-wartość. 
# Następnie program ma wyświetlić w innym słowniku ilość występowania wartości w pierwszym słowniku.

# Sample Input:
#   3
#   ala kota
#   ada kota
#   ama kota

# Sample Output:
#   {'kota': 3}

n = int(input())
slownik = dict()
for i in range(n):
    para = input().split()
    slownik[para[0]] = para[1]

slownik_wynik = {}
for value in slownik.values():
    if value not in slownik_wynik.keys():
        slownik_wynik[value] = 1
    else:
        slownik_wynik[value] += 1

print(slownik_wynik)