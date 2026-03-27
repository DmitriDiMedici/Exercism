def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    factors = [x for x in range(1,number) if number % x == 0]
    aliquot_sum = sum(factors)

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    try:
        if aliquot_sum == number:
            return "perfect"
        elif number < aliquot_sum:
            return "abundant"
        else:
            return "deficient"
    except ValueError as e:
        return e

