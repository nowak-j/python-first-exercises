# W systemie znajdue się plik data.csv, który wygląda następująco:

# department_id,department_name,manager_id,location_id
# 10,Administration,200,1700
# 20,Marketing,201,1800
# 30,Purchasing,114,1700
# 40,Human Resources,203,2400
# 50,Shipping,121,1500

# Napisz program, który wyświetli ten plik csv na ekranie.

import csv
with open("data.csv") as csv_file:
    for string in csv_file:
        print(string, end="")
