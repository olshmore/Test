a=int(input('Введите результат в первый день, км'))
b=int(input('Введите цель, км'))
i=1
while a<=b:
    a=a+a*0.1
    i+=1
print('На ',i,' день спортсмен достиг результата — не менее', b, 'км')