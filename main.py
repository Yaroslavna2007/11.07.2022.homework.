n = int(input('n='))
m = int(input('m='))
k = int(input('k='))
if k < m*n and (((n+m)-k) % n == 0 or ((n+m)-k) % m == 0):
    print('yes')
