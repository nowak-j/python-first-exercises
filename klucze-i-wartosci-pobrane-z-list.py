# Napisz funkcję map_list(list1, list2), której wynikiem będzie słownik, w której list1 będą kluczami, a list2 wartościami tego słownika.

def map_list(list1, list2):
    slownik = {}
    krotka = tuple(list1)
    for (a,b) in zip(krotka, list2):
        slownik[a] = b
    return slownik