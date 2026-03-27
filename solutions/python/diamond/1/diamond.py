def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(letter)
    lines = []


    # Upper half
    for i in range(index + 1):
        char = alphabet[i]
        outer_spaces = index - i
        if i == 0:
            line = " " * outer_spaces + char + " " * outer_spaces
        else:
            inner_spaces = i * 2 - 1
            line = " " * outer_spaces + char + " " * inner_spaces + char + " " * outer_spaces
        lines.append(line)

    # Lower half
    for i in range(index - 1, -1, -1):
        lines.append(lines[i])
        
    return lines