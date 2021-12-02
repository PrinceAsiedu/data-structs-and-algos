# mydetails = {
#     'firstname': 'Prince',
#     'lastname': 'Asiedu',
#     'email': 'prince14asiedu@gmail.com',
#     'phone': '+233553288993',
#     'address': '123 Main St Asiedu Ave'
# }

# myDataKeys = iter(mydetails.keys())
# myDataValues = iter(mydetails.values())
# myDataItems = iter(mydetails.items())

# exhausted = False

# while not exhausted:
#     try:
#         print(next(myDataKeys))
#         print(next(myDataValues))
#         print(next(myDataItems))
#     except StopIteration:
#         exhausted = True
#         raise StopIteration('One or more series of iterators exhausted')

#     continue

# traditional function that computes factors
# def factors_of(number):
#     results = []
#     for k in range(1, number + 1):
#         if number % k == 0:
#             results.append(k)
#     return results


# generator that computes factors
# def factors(number): 
#     for k in range(1, number + 1):
#         if number % k == 0:
#             yield k


# factors again but this time more efficient
# def factors(number): 
#     k = 1
#     while k * k < number:
#         if number % k == 0:
#             yield k
#             yield number // k
#         k += 1 
#     if k * k == number:
#         yield k 

# for factor in factors(int(input('Enter a number to get its factors: '))):
#     print(factor)


# now for something completely different
# fibonacci baby!!

# def fibonacci():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         future = a + b
#         a = b
#         b = future

# counter = 0
# limit = 100
# for n in fibonacci():
#     if counter < limit:
#         print(f'Fibo number: {n}')
#         counter += 1
#     else: 
#         break