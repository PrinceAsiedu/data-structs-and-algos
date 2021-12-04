# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def is_odd_product(seq):
    """
    Returns True if there is a distinct pair of numbers in the sequence whose
    product is odd.
    """
    for i in seq:
        for j in seq:
            if i * j % 2 == 1:
                return True
    return False
