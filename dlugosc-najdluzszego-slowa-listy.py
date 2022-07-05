# Napisz funkcję get_largest_size(words), która jako argument przyjmuje listę słów a w wyniku zwraca długość najdłuższego słowa w liście words.
# Napisz wyłącznie samą funkcję.

def get_words():
    words = input().split()

def get_largest_size(words):
    for word in range(len(words)):
        largest = max(words, key=len)
        largest = len(largest)
        return largest