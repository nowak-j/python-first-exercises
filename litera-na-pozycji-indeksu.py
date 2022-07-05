# Napisz funkcję o nazwie get_letter_word(word, index), która pobiera słowo oraz liczbę całkowitą. 
# Wynikiem funkcji jest litera znajdująca się na pozycji, której wartość jest indeksem.
# W przypadku błędnym program zwraca wartość None.

def get_letter_word(word, index):
    if index != 0:
        index -= 1
    if index < len(word) and index >= 0:
        return word[index]
    else:
        return None