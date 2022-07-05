# Napisz program, który pobierze od użytkownika dwa ciągi tekstowe. 
# Wynikiem działania programu ma być wyświetlenie w postaci posortowanej liter podanych ciągów, bez ich części wspólnej.
# Uwzględniamy tutaj wszystkie znaki widoczne (oprócz spacji) w tabeli ASCII. Sortujemy je według ich kodów.

input1 = input()
input2 = input()
set1 = set()
set2 = set()
set1.update(input1)
set2.update(input2)
final_set = set1.symmetric_difference(set2)
result = ' '.join(sorted(final_set))
print(result)