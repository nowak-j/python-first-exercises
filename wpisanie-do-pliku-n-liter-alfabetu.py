# Napisz program, który pobierze od użytkownika liczbę całkowitą n, a następnie w pliku words.txt umieści wszystkie litery z alfabetu łacińskiego tak,
# że w jednej linii będzie n znaków dużymi literami. 

# Sample Input:
#     3

# Sample Output:
#     ABC
#     DEF
#     GHI
#     JKL
#     MNO
#     PQR
#     STU
#     VWX
#     YZ

def alphabet():
    number = int(input())
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    file = open("words.txt", "w")
    
    i = 0
    while i < len(alphabet):
        for j in range(number):
            if(i == len(alphabet)):
                break
            file.write(alphabet[i])
            i += 1
        file.write('\n')

    file.close()

alphabet()