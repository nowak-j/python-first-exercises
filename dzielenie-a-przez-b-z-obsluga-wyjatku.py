# Napisz program, który pobierze dwie liczby rzeczywiste a i b i wyświetli na ekran wynik dzielenia a/b. 
# W przypadku dzielenia przez zero program powinien wyświetlić komunikat: Nie dziel przez zero! 
# W przypadku błędnego sformatowania danych program powinien wypisać komunikat: Błędny format danych wejściowych!

a = input()
b = input()
try:
    a = float(a)
except ValueError:
    print("Błędny format danych liczbowych!")
    exit()
          
try:
    b = float(b)
except ValueError:
    print("Błędny format danych liczbowych!")
    exit()
          
try:
    print(a/b)
except ZeroDivisionError:
    print("Nie dziel przez zero!")