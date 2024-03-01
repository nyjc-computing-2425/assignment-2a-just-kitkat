num = input('Enter a number (decimal or integer): ')
# type your code here
sf = 0
leading_zeros = True
for char in num:
    if leading_zeros and char not in "0.":
        leading_zeros = False
    if not leading_zeros and char != ".":
        sf += 1


# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
