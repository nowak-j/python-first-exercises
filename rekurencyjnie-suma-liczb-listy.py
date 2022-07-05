# Utwórz funkcję sum_list(numbers), która jako argument będzie przyjmowała listę liczb. 
# Działanie tej funkcji ma polegać na obliczeniu za pomocą rekurencji sumy wszystkich elementów listy i zwróceniu tej wartości.

def sum_list(numbers):
    if len(numbers)==0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:]) 