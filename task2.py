#Використовуючи підпрограми для додавання векторів та
# множення вектора на число, знайти вектор
#c=a-3*b+2*c, де a,b,c .
a = [int(input('Введіть координати вектора a: ')) for x in range(3)]
b = [int(input('Введіть координати вектора b: ')) for x in range(3)]
c = [int(input('Введіть координати вектора c: ')) for x in range(3)]
b3 = list(map(lambda coordinate: coordinate * 3, b))
c2 = list(map(lambda coordinate: coordinate * 2, c))
a_3b = list(map(lambda x, y: x - y, a, b3))
res = list(map(lambda x, y: x + y, a_3b, c2))
print(res)

