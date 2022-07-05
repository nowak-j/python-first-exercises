# Napisz program, który pobierze liczbę naturalną nn, następnie nn słów do zbioru, a następnie wyświetli ten zbiór na ekranie posortowane.

liczba = int(input())
zbior = set()
for i in range(liczba):
    slowo = input()
    zbior.add(slowo)
print(sorted(zbior))