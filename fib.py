def fibonacci():
    """
    Fibonacci number generator
    Can be used to generate fibonacci numbers
    Example usage: 
    
    for n in fibonacci():
        if not count == times:
            count = count + 1
            print(f'Fibonacci number({count}): {n}')
        else: break
    
    """
    a = 0
    b = 1
    while True:
        yield a
        temp = a + b
        a = b
        b = temp


if __name__ == '__main__':
    """Generate first hundred Fibnacci numbers
    Note: to generate more or less than 100 fibonacci numbers here
    Change the variable `times` to your desired number of times
    """
    times = 100
    count = 0

    for n in fibonacci():
        if not count == times:
            count = count + 1
            print(f'Fibonacci number({count}): {n}')
        else: break
