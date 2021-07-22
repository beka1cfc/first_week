#задача 1


a = float(input("Введите первое число: "))
operand = input("Что нужно сделать? ")
b = float(input("Введите второе число: "))

if operand == "+":
	print("Результат: "+ str(a+b))
elif operand == "-":
	print("Результат: "+ str(a-b))
elif operand == "/":
	print("Результат: "+ str(a/b))
elif operand == "*":
	print("Результат: "+ str(a*b))
elif operand == "**":
	print("Результат: "+ str(a**b))
elif operand == "//":
	print("Результат: "+ str(a//b))
elif operand == "%":
	print("Результат: "+ str(a%b))
else:
	print("Выбрана неверная операция!")


#задача 2


a = int(input("Введите число: "))
b = int(input("Введите число: "))

if a%b:
	print("Не делится ")
else:
	print("Результат: " + str(a/b) + ", Делится!")



#задача 3


a = input("Введите пароль: ")
b = input("Введите пароль еще раз: ")

if a == b:
	print("Пароль принят")
else:
	print("Пароль не принят")


#задача 4


a = int(input("Введите кол-во школьников: "))
b = int(input("Введите кол-во яблок: "))
print(f"Каждому по {b//a} яблок, В корзине осталось {b%a} яблок ")


#задача 5


a = input("Скорость Зума: ")
b = input("Скорость Флеша: ")

if a > b:
	print("NO")
elif a < b:
	print("YES")
else:
	print("Don't know")


#задача 6


a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
d = int(input("Четвертое число: "))

if(a<b) and (a<c) and (a<d):
	print(a)
if(b<a) and (b<c) and (b<d):
	print(b)
if(c<a) and (c<b) and (c<d):
	print(c)
else:
	print(d)



#задача 7

a = int(input("Напишите ваш вес: "))
if (a <= 59):
	print("Легкий вес")
elif (a == 60) or (a <= 63):
	print("Первый полусредний вес")
elif (a <= 68):
	print("Полусредний вес")



#задача 8 


a = int(input("Введите ваш возраст: "))
b = input("Введите ваш пол: ")
c = ("Мужчина")
d = ("Женщина")

if (a >= 21) and (b == c):
	print("Добро Пожаловать!")
elif(a >= 18) and (b == d):
	print("Добро Пожаловать!")
else:
	print("Вход запрещен")


#задача 9


n = int(input("Введите 3 значное число: "))
a = n // 100
b = n // 10 % 10
c = n % 10
print("Число:" + str(n) + " Сумма:" + str(a + b + c) + " Произведение:" + str(a * b * c))


#задача 10


red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0]
a = int(input("Введите число: "))
if a in red:
	print("Красный")
elif a in black:
	print("Черный")
elif a in green:
	print("Зеленый")
else:
	print("Ошибка ввода")



#алгоритм 1

a = 1
b = 2
a = a + b
b = a - b
a = a - b
print(a,b)
