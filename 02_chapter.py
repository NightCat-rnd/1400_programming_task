import math
#2.1.a
x = float(input('Введите число '))
y=17*x**2-6*x+1334
print('\nФункция y = 17*x**2 - 6*x +13')
print('При х=', x, 'y= ', y)

#2.2.
a=x
y = (a**2 + 10) / math.sqrt(a**2+1)
print('\ny = (a**2 + 10) / math.sqrt(a**2+1)')
print('При a=', a, 'y= ', y)

#2.3.a
print('\ny = SQRT((2a+SIN(|3a|)) / 3.56)')
y = math.sqrt((2*a + math.sin(abs(3*a)))/3.563)
print('При a=', a, 'y= ', y)

#2.4.
x = float(input('\nВведите длину стороны квадрата '))
print('Периметр квадрата равен ', x*4)

#2.5.
x = float(input('\nВведите радиус окружности '))
print('Ее диаметр равен ', 2*x)

#2.6.
x = float(input('\n Введите высоту над Землей '))
print('Расстояние до горизонта',math.sqrt((6350+x)**2/6350**2),'км')