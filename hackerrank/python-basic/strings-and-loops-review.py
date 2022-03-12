"""Given a string, , of length  that is indexed from to, print its 
even-indexed and odd-indexed characters as space-separated 
strings on a single line(see the Sample below for more detail).
Note: 0 is considered to be an even index."""

num_of_strings = int(input())
for i in range(1, num_of_strings + 1):
    even_string = ''
    odd_string = ''
    string = str(input())
    for j in range(len(string)):
        if j % 2 == 0:
            even_string += string[j]
        else:
            odd_string += string[j]
    print(even_string, odd_string)
