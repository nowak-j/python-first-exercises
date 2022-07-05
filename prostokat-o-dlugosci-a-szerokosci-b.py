# Napisz program, który pobierze dwie liczby całkowite a,b większe od zera i wyświetli następujący prostokąt o długości a i szerokości b.
# Nie zakładamy tutaj błędnych danych wyjściowych.

# Sample Input 1:
#   3
#   3

# Sample Output 1:
#   ***
#   * *
#   ***

height = int(input())
width = int(input())
for i in range(0,height):
    for j in range (0,width):
        if i == 0 or i == height-1:
            print("*", end="")
        elif j == 0 or j == width-1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
