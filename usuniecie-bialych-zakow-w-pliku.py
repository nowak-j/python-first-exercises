# Napisz funkcję o nazwie remove_whitespace (fileInput, fileOutput), który jako argumenty przyjmuje (jako ciąg tekstowy) nazwę pliku wejściowego oraz wyjściowego. 
# W wyniku funkcji w pliku wyjściowym ma pojawić się zawartość pliku wejściowego bez znaków spacji, tabulacji oraz nowej linii.

def remove_whitespace(fileInput, fileOutput):
    input_file = open(fileInput, 'r')
    output_file = open(fileOutput, 'w')
    lines = input_file.readlines()
    for line in lines:
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        line = line.replace('\t', '')
        output_file.write(line)
    input_file.close()
    output_file.close()