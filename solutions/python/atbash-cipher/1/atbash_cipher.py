def encode(plain_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = plain[::-1]
    equivalences = dict(zip(plain, cipher))
    plain_text = "".join([char for char in plain_text if char.isalnum()])
    to_encode = " ".join([plain_text[i:i+5] for i in range(0,len(plain_text),5)])
    encoded_text = ""
    for char in to_encode.lower():
        if char in plain:
            encoded_text += equivalences[char]
        else:
            encoded_text += char
    return encoded_text


def decode(ciphered_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = plain[::-1]
    equivalences = dict(zip(cipher, plain))
    encoded_text = ""
    for char in ciphered_text.lower():
        if char in cipher:
            encoded_text += equivalences[char]
        else:
            encoded_text += char
    return encoded_text.replace(" ", "")