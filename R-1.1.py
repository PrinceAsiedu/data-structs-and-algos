def is_multiple(multiple, number):
    if multiple != 0 and number % multiple == 0:
        return True
    else: return False

nums =  [x for x in range(100)]
b = 3
for num in nums:
    if num == 0:
        num+=1
    print(f'{num} is multiple of {b}: {is_multiple(b, num)}')
