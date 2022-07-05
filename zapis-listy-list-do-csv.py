# Napisz program, który do pliku o nazwie data.csv zapisze następującą listę list:
# [[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]

import csv
lista_list = [[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
data = open('data.csv','a',newline='')
outputWriter = csv.writer(data)
for lista in lista_list:
   outputWriter.writerow(lista) 

data.close()