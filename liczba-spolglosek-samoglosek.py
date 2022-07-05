# Napisz program, który wczyta słowo od użytkownika, a następnie wypisze ilość samogłosek (a,e,i,o,u,y) oraz spółgłosek.

słowo = input()
słowo = słowo.lower()
litery = list(słowo)
sam = 0
spół = 0
for znak in litery:
    if znak == "a" or znak == "ą" or znak == "e" or znak == "ę" or znak == "i" or znak == "o" or znak == "u" or znak == "ó" or znak == "y":
        sam += 1
    else:
        spół += 1
print(f"Liczba samogłosek: {sam}")
print(f"Liczba spółgłosek: {spół}")