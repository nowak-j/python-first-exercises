# Napisz program, który będzie wypisywał unikalne słowa (wedle występowania w pliku) pliku test.txt.

file = open("test.txt", "r")
text = file.read()
text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('\n', '')
text = text.lower()
text = text.split()
unique = []
for element in text:
    if element not in unique:
        unique.append(element)
for element in unique:
    print(element)

file.close()
