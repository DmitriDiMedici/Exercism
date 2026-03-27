def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    n = [x ** len(digits) for x in digits]
    if sum(n) == number:
        return True
    else:
        return False
