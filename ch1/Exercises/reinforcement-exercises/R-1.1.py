def is_multiple(number, multiple):
    if number != 0 and multiple % number == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    b = int(input('Enter a number above 1: '))
    nums =  [x for x in range(b*b) if x != 0]
    for num in nums:
        print(f'{num} is multiple of {b}: {is_multiple(b, num)}')
