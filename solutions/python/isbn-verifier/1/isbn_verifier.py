def is_valid(isbn):
    isbn_clean = isbn.replace("-","")
    total_count = 0

    if len(isbn_clean) != 10:
        return False

    for index, element in zip(range (10, 0, -1), isbn_clean):
        try:
            if index == 1 and element == "X":
                element = "10"
            total_count += index * int(element)
        except ValueError:
            return False


    if total_count % 11 == 0:
        return True
    else:
        return False