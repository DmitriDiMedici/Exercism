def rebase(input_base, digits, output_base):

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for x in digits:
        if not (0 <= x < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    indexes = [i[0] for i in enumerate(digits)]
    nums = dict(zip(indexes[::-1], digits))

    # To decimal
    decimal = 0
    for key, value in nums.items():
        decimal += value * pow(input_base, key)

    # To whatever
    quotient = decimal
    remainders = []
    while quotient != 0:
        remainder = quotient % output_base
        quotient = quotient // output_base
        remainders.append(remainder)

    if not remainders:
        remainders = [0]
        
    return remainders[::-1]