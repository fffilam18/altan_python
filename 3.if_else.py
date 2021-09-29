# *** Условные операторы ***

var = 5

# if имеет условие
# выполняет код внутри тела если условие истинно 
# if var != 0:
#     print("hello")

# if var < 0:
#     print("hello")

var = -1

# if var < 0:
#     print ("меньше нуля")
# else:
#     print("не меньше нуля")

var = 'a'

if var == 'A':
    res = "lit A"
# else if
elif var == 'B':
    res = "lit B"
elif var == 'C':
    res = "lit C"
elif var == 'a':
    res = "lit a"
else:
    res = "ни один из вариантов"

# print(res)


# *** Пример. "Термостат" ***

# текущая температура
current_temp = 27

# диапазон температур
min_temp = 21
max_temp = 26

# логика термостата
if current_temp < min_temp:
    print("включен нагрев")
elif current_temp > max_temp:
    print("выключен нагрев")
else:
    print("температура оптимальна")