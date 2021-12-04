# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

# pseudo-code
# 1. Define a function that takes a list of numbers as an argument
# 2. Reverse the list
# 3. Define a variable to store the reversed list
# 4. Use a built-in function to do the same thing
# 5. Compare the two results


def list_reverse(l):
    """
    Reverse a list
    """
    return l[::-1]


def main():
    """
    Main function
    """
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myfuncResult = list_reverse(data)
    builtinResult = list(reversed(data))
    print(myfuncResult == builtinResult)

if __name__ == '__main__':
    main()
