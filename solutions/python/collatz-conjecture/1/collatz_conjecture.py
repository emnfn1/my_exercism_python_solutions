def steps(number):
    steps = 0
    if number <= 0 or not isinstance(number, int):
        raise ValueError("Only positive integers are allowed")   
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        steps += 1
    return steps
