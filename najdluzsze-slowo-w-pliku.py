# Napisz program, który wyświetli najdłuższe słowo występujące w pliku polish.txt.

def longest_word():
    polish = open("polish.txt", "r")
    lines = polish.readlines()
    max = 0
    for line in lines:
        line = line.split()
        for element in line:
            if len(element) > max:
                max = len(element)
                longest_word = element

    polish.close()
    print(longest_word)

longest_word()