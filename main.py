# задача 1
n = int(input('n='))
m = int(input('m='))
k = int(input('k='))
if k < m*n and (((n+m)-k) % n == 0 or ((n+m)-k) % m == 0):
    print('yes')
else:
    print('no')

    
    
    
# задача 2
n = int(input('длинна меньшего борта'))
m = int(input('длина большего борта'))
y = int(input('расстояние до меньшего борта'))
x = int(input('расстояние до большего борта'))
z = m - y
v = n - x
if y < z and y < x and y < v:
    print(y)
elif v < y and v < z and v < x:
    print(v)
elif x < y and x < z and x < v:
    print(x)
elif z < x and z < y and z < v:
    print(z)



# номер 3
k = int(input('введите число от 1 до 10'))
x = k//2
y = k - x -1
m = 45 * k + x * 5 + y * 15
v = m // 60
c = 9 + v
print(c, ':', m - (60 * v))
