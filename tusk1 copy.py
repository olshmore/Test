#1

name=input('Hi! What is your name?')
print('Welcome, ' , name)

input('Do you like maths?')

p=int(input('Whatever, type integer number'))
print(p+10)

#2

s=int(input('Whats the time?'))

hours = s//3600
minutes= (s%3600)//60
seconds=(s%3600)%60
print(hours,'h' , minutes, 'm', seconds, 's')

#3

n=(input('Type in digit'))

three=int(n+n+n)
two=int(n+n)
one=int(n)
print(one+two+three)

#4

n=int(input('Type in number'))
max=0
while (n%10>=1) and (n%10<=9):
    if n%10>max:
        max=n%10
    n = n//10
print('max= ',max)

#5

revenue=int(input('Введите размер выручки'))
costs=int(input('Введите размер издержек'))
if revenue>costs:
    print('Прибыль')
    print('Рентабельность составляет', (revenue-costs)/revenue)
    employees=int(input('Введите численность сотрудников фирмы'))
    print('Прибыль фирмы в расчете на одного сотрудника составляет',
          (revenue-costs)/revenue/employees)
else:
    print('Убыток')

#6

a=int(input('Введите результат в первый день, км'))
b=int(input('Введите цель, км'))
i=1
while a<=b:
    a=a+a*0.1
    i+=1
print('На ',i,' день спортсмен достиг результата — не менее', b, 'км')