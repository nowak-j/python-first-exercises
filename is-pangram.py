# Napisz funkcję is_pangram(word), który sprawdza czy dany ciąg tekstowy jest pangramem.
# W przypadku pozytywnej odpowiedzi funkcja powinna zwracać True, w przeciwnym przypadku False.

def is_pangram(word):
    if word == '':
        return False

    word = word.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter in word:
            continue
        else:
            return False
        
    return True