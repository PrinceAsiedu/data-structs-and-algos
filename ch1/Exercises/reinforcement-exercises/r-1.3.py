# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.


def minmax(data):
    """
    Returns the smallest and largest numbers, in the form of a tuple of
    length two.
    """
    min = data[0]
    max = data[0]
    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)


def main():
    """
    Function to test `minmax function.
    """
    mnlist = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    print(minmax(mnlist))

if __name__ == '__main__':
    main()