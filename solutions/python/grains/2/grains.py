def square(number):
    if number in range(1, 65):
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")

def total():
    squares = range(1, 65)
    t = 0
    for n in squares:
        t = t + (2 ** (n - 1))
    return t
        
