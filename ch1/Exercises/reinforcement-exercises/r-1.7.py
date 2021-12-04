# Give a single command that computes the sum from Exercise R-1.6, relying
# on Python’s comprehension syntax and the built-in sum function.
def squares_sums_of_odd_numbers(n):
    """
    Return the sum of the squares of all the odd positive integers smaller than n.
    """
    return sum(x**2 for x in range(1, n, 2))


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
