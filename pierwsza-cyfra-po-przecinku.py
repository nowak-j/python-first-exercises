# Napisz program, który pobierze od użytkownika liczbę rzeczywistą, a następnie wyświetli pierwszą cyfrę po przecinku.
number = input()
x = number.split(".")
if(len(x) == 2):
    print(x[1][0])
else:
    print(0)