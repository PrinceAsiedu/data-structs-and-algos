# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

for i in range(8, -9, -2):
    if not i == -8:
        print(i, end=', ')
    else:
        print(i)