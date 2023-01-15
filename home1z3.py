z = int (input('Введите шестизначное число '))
n = z // 1000
a = n % 10
m = n // 10
b = m % 10
c = m // 10
p = z % 1000
d = p % 10
k = p // 10
f = k % 10
e = k // 10
if a + b + c == d + e + f: 
    print('yes')
else:
    print('no')
