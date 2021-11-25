a = int(input('введите первый отрезок'))
b = int(input('введите второй отрезок'))
c = int(input('введите третий отрезок'))

if a+b <= c or a+c <= b or b+c <= a:
  print ('невозможно')
else:
  print ('возможно')

if a == b == c:
  print ('равностронний')

elif a != b and a == c or a != c and a == b or b != c and b == a:
  print ('равнобедренный')

else:
  print ('разностронний')