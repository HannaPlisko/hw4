x=float(input('введите число '))
y=float(input('введите число '))
z=input('введите операцию ')
if z=='+':
    r=x+y
elif z=='-':
    r=x-y
elif z=='*':
    r=x*y
if y == 0:
    r = 'деление на 0!'
elif z=='/':
    r = x/y

print('результат =', r)