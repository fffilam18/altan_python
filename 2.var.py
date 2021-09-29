# *** Переменные, функция input(), типы данных ***

# in_1 = input("Введите число А: ")
# in_2 = input("Введите число Б: ")

# # result = int(in_1) + int(in_2) # конкатенация 
# result = int(in_1) + int(in_2) 

# print("Результат: ", result)


# Типы данных

# целочисленный тип данных
int_num = 777

# тип данных число с плавающей точкой (пишутся через ТОЧКУ)
float_num = 3.14

# строка (строковой тип данных)
string = "Hello, World!"

# булевы типы данных (Джордж Буль)
boolean_t = True # "истина" (логическая 1)
boolean_f = False # "ложь" (логический 0)

# print(boolean_t, boolean_f)


# способ форматирования строк f-строка (f-string)

name = "Ayta"
age = 29

s = f"Имя: {name} Возраст: {age}"

# print(s)


# Арифметические операции

x = 5
y = 7

# сложение 
res = x + y

# вычитание
res = x - y

# умножение
res = x * y

# обычное деление (результатом всегда является число с плавающей точкой)
x = 10
y = 5
res = x / y

# целочисленное деление
res = x // y

# деление по остатку
x = 3
y = 2
res = x % y

# возведение в степень
res = x ** y


# Логические операции

x = 5
y = 3

# операция "не равно"
# res = x != y

# операция "равно"
res = x == y

# операция "меньше"
res = x < y

# операция "больше"
res = x > y

# операция "меньше либо равно"
res = x <= y

# операция "больше либо равно"
res = x >= y


z = False
k = False

# оператор НЕ (NOT, инверсия)
res = not z

# оператор И (AND, конъюнкция)
res = z and k

# оператор ИЛИ (OR, дизъюнкция)
res = z or k


# более слолжный пример
a = 5
b = 3
c = 1

res = (a > b) and (b == c)

print(res)