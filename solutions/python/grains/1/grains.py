def square(number):
    if number <= 64 and number > 0:
        grains_in_square = 2 ** (number - 1)
        return grains_in_square
    else:
        raise ValueError("square must be between 1 and 64")



def total():
    nums = [*range(1,65)]
    squared = [square(n) for n in nums]
    total_sum = sum(squared)
    return total_sum    
    
