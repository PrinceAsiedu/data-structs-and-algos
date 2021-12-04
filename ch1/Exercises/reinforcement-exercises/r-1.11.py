# Demonstrate how to use Python’s list comprehension syntax to produce
# the list[1, 2, 4, 8, 16, 32, 64, 128, 256].


def main():
    """ 
    Demonstrate how to use Python’s list comprehension syntax to produce
    the list[1, 2, 4, 8, 16, 32, 64, 128, 256].
    """
    print([2 ** x for x in range(9)])

if __name__ == '__main__':
    print(2**0)
    main()