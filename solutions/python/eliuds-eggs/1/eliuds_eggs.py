def egg_count(display_value):
    binary = bin(display_value)[2:]
    number_eggs = str(binary).count("1")
    return number_eggs