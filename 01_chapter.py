import math

#1.1.
print('31','18','79')

#1.2.
print('47'+'  '+'52'+'  '+'150')

#1.3.
print('50\n10')

#1.4.
print('5\n10\n21')

#1.5.
print('1\n2')

#1.6.
print('%.3f' %math.pi)

#1.7.
print('%.1f' %math.e)

#1.8.
number = input('Введите число: ')
print('Вы ввели число:', number)

#1.9.
number = input('Введите число: ')
print(number, '- вот какое число вы ввели')

#1.10.
print(input('Введите ваше имя: '))

#1.11
name = input('Введите название футбольной команды: ')
print(name.title(),'- это чемпион')

#1.12.
name = input('Введите имя: ')
print('Привет, '+name+'!')

#1.13.
number = int(input('Введите целое число: '))
print('Следующее за числом',number,'число -',number+1)
print('Для числа',number,'предыдущее число -',number-1)

#1.14.
n1 = int(input('Введите первое число '))
n2 = int(input('Введите второе число '))
n3 = int(input('Введите третье число '))
print(n1,' ',n2,' ',n3)

#1.15.
n1, n2, n3, n4 = map(int,input('Введите 4 числа через пробел ').split())
print(n1,n2,n3,n4)

#1.16.в.
x,y = map(int, input('Введите через пробел 2 числа ').split())
print(x, 25)
print(x,y)

#1.17.в
x,y = map(int, input('Введите через пробел 2 числа ').split())
print(x, y)
print(5,y)

