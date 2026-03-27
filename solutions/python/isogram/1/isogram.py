def is_isogram(string):
    no_hyphens = string.replace("-","")
    clean_string = no_hyphens.replace(" ","")
    if len(clean_string.lower()) == len(set(clean_string.lower())):
        return True
    else:
        return False
