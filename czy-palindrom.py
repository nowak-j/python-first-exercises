# Napisz program, który wczyta od użytkownika ciąg znakowy, a następnie sprawdzi czy ciąg ten jest palindromem czy nie.
# W wyniku program ma wyświetlić wartość prawda (jeżeli jest palindromem) lub fałsz (w przeciwnym przypadku).

# słowo = input()
# litery = list(słowo)
# litery_od_końca = [] + litery
# litery_od_końca.reverse()
# if litery == litery_od_końca:
#     print("True")
# else:
#     print("False")


def is_palindrome():
    word = input().lower()
    letters = list(word)
    letters_from_end = [] + letters
    letters_from_end.reverse()
    if letters == letters_from_end:
        print("True")
    else:
        print("False")

is_palindrome()