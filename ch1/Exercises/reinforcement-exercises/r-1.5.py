# Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.
def square_sums(n):
    return sum([x**2 for x in range(1, n)])

print(square_sums(5))


