# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def square_sums(n):
    sum = 0
    for i in range(1, n):
        sum += i**2
    return sum


print(square_sums(5))   
