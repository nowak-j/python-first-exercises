# Napisz program, który pobierze od użytkownika tekst, a następnie wypisze następujące statystyki:
# Ilość liter
# Ilość cyfr
# Ilość białych znaków

tekst = input()
znaki_białe = 0
for znak in tekst:
    if znak.isspace():
        znaki_białe += 1
litery = 0
cyfry = 0
tekst.split()
for element in tekst:
    if element.isalpha():
        litery += len(element)
    elif element.isdecimal():
        cyfry += len(element)
print("Ilość liter == ", litery)
print("Ilość cyfr == ", cyfry)
print("Ilość znaków białych == ", znaki_białe)