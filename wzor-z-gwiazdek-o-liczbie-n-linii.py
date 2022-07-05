# Napisz program, który pobierze od użytkownika liczbę całkowitą n i wyświetli następujący wzorek. 
# W przypadku niepoprawnych danych, program ma ponownie je wczytać.

# Sample Input 1:
#     5

# Sample Output 1:
#     *        *
#     **      **
#     ***    ***
#     ****  ****
#     **********

n = int(input())
while (n < 0 or n == 0):
    n = int(input())

for i in range(n, 0, -1):
    print("*" * (n-i), end="")
    print(" " * i*2, end="")
    print("*" * (n-i), end="")
    print("")
print("*" * (n*2), end="")
