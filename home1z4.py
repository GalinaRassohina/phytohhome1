n = int (input('длину шоколадки '))
m = int (input('ширину шоколадки '))
k = int (input('количество желаемых долек '))
if k< n * m and (k % m == 0 or k % n == 0):
    print('yes')
else:
    print('no')