#задача 1
#list: ordered, changeable, allow duplicates
#tuple: ordered, allow duplicates
#set: changeable
#dict: ordered, changeable


#задача 2

a = "HELLO I AM WRITING CODE"
b = ("HELLO" , "I" , "AM" , "WRITING" , "CODE")
print(sorted(b))


#задача 3

names = ["Beks" , "Zhenya" , "Dana" , "Alibek"]
job = ["программист"]
for a in names:
	for b in job:
		print(a, b)


#задача 4

with open("word.txt","a") as b:
    for i in range(1000):
        b.write("i am developer\n")


#задача 5

a = [1,1,2,3,5,8,13,21,34,55,89]
for b in a:
	if b < 5:
		print(b)


#задача 6

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for d in range(len(a)):
	for e in range(len(b)):
		if a[d] == b[e]:
			c.append(a[d])
print(list(set(sorted(c))))


#задача 7

a = [2,3,4,7,237,2,2,4]
for b in a:
	if b == 237:
		break
	elif b % 2 == 0:
		print(b)

#задача 8

def check(a, b):
	if not a:
		return 0
	elif a[0] == b:
		return 1 + check(a[1:], b)
	else: 
		return check(a[1:], b)
a = input("Введите строку:")
b = input("Введите букву для проверки:")
print("Символ " + b + " встречается:")
print(check(a, b))


#задача 9

a = input("цифры: ")
b = a.split()
c = set(b)
if len(b) == len(c):
    print("true")
else:
    print("false")

#задача 10

text = (input())
words = text.split()
a = max(words, key=len)
b = max(words, key=words.count)
print(a,b)


#задача 11

n = int(input("Введите 3 значное число: "))
a = n // 100
b = n // 10 % 10
c = n % 10
print(f"Число: {n} Сумма: {a+b+c} Произведение:{a*b*c}")

#задача 12

from random import random
a = round(random() * 50)
b = 1
print("Компьютер загадал число. Отгадайте его. У вас 3 попыток")
while b <= 3:
    c = int(input(str(b) + '-я попытка: '))
    if b > a:
        print('Больше')
    elif b < a:
        print('Меньше')
    else:
        print('Вы угадали с %d-й попытки' % b)
        break
    b += 1
else:
    print("Game Over")


#задача 13

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)


#задача 14

a = input("текст: ")
 
a_new = a[0]
i = 1
while i < len(a):
    if a[i] != ' ':
        a_new += a[i]
    elif a[i - 1] != ' ':
        a_new += '_'
    i += 1
print(a_new)


#задача 15

def fill_list(m1, m2, amount, l):
    from random import randint
    for i in range(amount):
        l.append(randint(m1, m2))
 
 
def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1
 
 
lst = []
dct = {}
 
mn = int(input('Минимум: '))
mx = int(input('Максимум: '))
qty = int(input('Количество элементов: '))
 
fill_list(mn, mx, qty, lst)
analysis(lst, dct)
 
for item in sorted(dct):
    print("'%d':%d" % (item, dct[item]))


#задача 16

def sum_for_loop(a):
    s = 0
    for x in a:
        s += x
    return s

def sum_while_loop(a):
    s = 0
    n = len(a)
    while n:
        n -= 1
        s += a[n]
    return s
if __name__ == '__main__':
    t = [5, 3, 4, 1, 7]
    for f in (sum_for_loop, sum_while_loop,):
        print(f(t))

#задача 17

a = input("цифра: ")
b = input("2 цифра: ")
c = a + b
d = b + a
print(max(c,d))


#задача 18

a = int(input("год: "))
if a % 4 != 0:
    print("Не Високосный")
elif a % 100 == 0:
    if a % 400 == 0:
        print("Високосный")
    else:
        print("Не Високосный")
else:
    print("Високосный")

#задача 19

import os

print(os.listdir())

#задача 20

from pathlib import Path
print(Path(r'C:\Users\user\Desktop\tutorPy\dom.py').suffix)

#задача 21

while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print(x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '/':
            if y != 0:
                print(x/y)
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")