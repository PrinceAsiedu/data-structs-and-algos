if __name__ == '__main__':
    n = int(input('Enter a number to find first 10 multiples of it: ').strip())
    for i in range(1, 10 + 1):
        multiple = n * i
        print(f'{n} x {i} = {multiple}')

# Given a string, , of length  that is indexed from to, print its even-indexed 
# and odd-indexed characters as space-separated strings on a single line(see the Sample below for more detail).

# Note: is considered to be an even index.

