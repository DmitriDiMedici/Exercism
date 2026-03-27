def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    caps = alphabet.upper()


    if -1 < key < 27 :
        final_message = ""
        for char in text:
            if char in alphabet + caps:
                letters_to_use = alphabet if char in alphabet else caps
                shifted_position = letters_to_use.index(char) + key
                shifted_position %= len(letters_to_use)
                final_message += letters_to_use[shifted_position]
            else:
                final_message += char


        return final_message