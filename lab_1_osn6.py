print(' введите числа на элементы x, y, z, w, v, e ')

x = int(input())
y = int(input())
z = int(input())
w = int(input())
v = int(input())
e = int(input())

a = [x, y, z, w, v, e]

h = (a[0] ** 4 - a[1] ** 6 + 3*a[2] - a[3] + (a[4] * a[5]) ** 2)

print (h)