# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def squares_sums_of_odd_numbers(n):
    """
    Return the sum of the squares of all the odd positive integers smaller than n.
    """
    sum = 0
    for i in range(1, n, 2):
        sum += i ** 2
    return sum


def main():
    """
    Test function
    """
    print(squares_sums_of_odd_numbers(10))
    print(squares_sums_of_odd_numbers(1))
    print(squares_sums_of_odd_numbers(5))
    print(squares_sums_of_odd_numbers(100))

if __name__ == '__main__':
    main()