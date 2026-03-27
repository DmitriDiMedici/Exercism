def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if all(letter in sentence.lower() for letter in alphabet):
        return True
    return False