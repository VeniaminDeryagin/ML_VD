# x = float(input())
# y = float(input())

# if x**2 + y**2 > 100:
#     print("Вы вышли в море и рискуете быть съеденным акулой!")
# elif (y <= 5 and 5 * x + 35 <= 3 * y and (x + 1)**2 - 36 <= 4 * y) or (y <= 5 and x**2 + y**2 <= 25):
#     print("Опасность! Покиньте зону как можно скорее!")
# else:
#     print("Зона безопасна. Продолжайте работу.")


# Вы уже знаете, как написать программу, которая знакомится с человеком и спрашивает его имя.
# Теперь напишите программу, которая сначала познакомится с пользователем, 
# а затем поинтересуется его настроением.
print("Как Вас зовут?")
name = input()
print(f"Здравствуйте, {name}!")
print("Как дела?")
hau = input()
if hau == 'хорошо':
    print("Я за Вас рада!")
elif hau == 'плохо':
    print("Всё наладится!")

# В главной велогонке года участвуют более тысячи гонщиков, которые должны пройти 
# трассу длиной 43872 метра. Задача — определить победителя.
# Нам известны средние скорости двух фаворитов — Пети и Васи. Помогите узнать, 
# кто из них пришёл к финишу первым.
p_speed = float(input())
v_speed = float(input())
if p_speed >= v_speed:
    print("Петя")
else:
    print("Вася")

# Три велогонщика снова хотят узнать, кто из них быстрее. Им предстоит пройти трассу 
# длиной 43872 метра, и нам нужно определить, кто из них пришёл к финишу первым.
# Нам известны средние скорости трёх фаворитов — Пети, Васи и Толи. Кто из них финишировал первым?
p_speed = float(input())
v_speed = float(input())
t_speed = float(input())
if p_speed >= v_speed and p_speed > t_speed:
    print("Петя")
elif v_speed >= p_speed and v_speed > t_speed:
    print("Вася")
else:
    print("Толя")

# Время подвести итоги гонки и объявить победителя!
# Длина трассы — 43872 метра, и нам известны средние скорости трёх фаворитов: Пети, Васи и Толи.
# Ваша задача — сравнить результаты гонщиков и вывести имя победителя.
first_name = 'Петя'
first_speed = float(input())
second_name = 'Вася'
second_speed = float(input())
third_name = 'Толя'
third_speed = float(input())
if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_name, third_name = third_name, second_name
if first_speed < third_speed:
    first_speed, third_speed = third_speed, first_speed
    first_name, third_name = third_name, first_name
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name
print(f'1. {first_name}')
print(f'2. {second_name}')
print(f'3. {third_name}')

# У Пети было 7 яблок, а у Васи 6.
# Затем Петя отдал 3 яблока Васе, а у Толи взял 2 яблока.
# Вася попросил у Толи 5 яблок, но отдал Гене 2.
# Затем Дима дал Пете N
# N яблок, а Васе M
# Так у кого в итоге яблок больше — у Пети или Васи?
N = int(input())
M = int(input())
Petr = 7
Vasya = 6
Petr = 7 - 3 + 2
Vasya = 6 + 3
Vasya = (6 + 3) + 5 - 2
Petr = 6 + N
Vasya = 12 + M
if Petr > Vasya:
    print("Петя")
else: 
    print("Вася")

# Вася любит полениться. Особенно ему нравится, когда в году появляется такой 
# лишний денёк, которого обычно не бывает.
# Напишите программу, которая поможет Васе определить, удастся ли ему побездельничать 
# в определённом году или нет.
year = int(input())
if year % 400 == 0:
    print("YES")
elif year % 100 == 0:
    print("NO")
elif year % 4 == 0:
    print("YES")
else:
    print("NO")

# А как быстро понять, является ли слово палиндромом? Написать программу для проверки этого! 
# В этом нам снова поможет условный оператор.
number = int(input())
a = number // 1000
b = number // 100 % 10
c = number // 10 % 10
d = number % 10
if a == d and b == c:
    print("YES")
else:
    print("NO")

# Давайте сыграем! С помощью условного оператора if-else и оператора in 
# проверим, не спрятался ли зайка в введённом предложении
rabbit = input()
if 'зайка' in rabbit:
    print("YES")
else:
    print("NO")

# Давайте сравним имена игроков лексикографически и с помощью 
# условных операторов определим, кто начнёт игру.
name_1 = input()
name_2 = input()
name_3 = input()
print(min(name_1, name_2, name_3))

# Коля решил зашифровать свои пароли, чтобы Аня не смогла их подсмотреть в блокноте. 
# Для этого он берёт изначальный пароль — трёхзначное число — и превращает его в
# новое, следуя таким правилам:
# Сначала находит сумму двух младших цифр (десятков и единиц).
# Затем находит сумму двух старших цифр (сотен и десятков).
# Эти суммы записываются в порядке не возрастания, образуя зашифрованное число.
# Помогите реализовать алгоритм шифрования, используя базовое применение 
# условного оператора if-else.
number = int(input())
b = number // 100 % 10
c = number // 10 % 10
d = number % 10
step_1 = c + d
step_2 = b + c
if step_1 > step_2:
    print(f'{step_1}{step_2}')
else:
    print(f'{step_2}{step_1}')

# Согласно одному древнему поверью, трёхзначное число считается красивым, 
# если сумма его минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.
# Напишите программу, которая проверяет, является ли число красивым.
number = int(input())
b = number // 100 % 10
c = number // 10 % 10
d = number % 10
min_number = min(b, c, d)
max_number = max(b, c, d)
lost_number = b + c + d - min_number - max_number
if min_number + max_number == lost_number * 2:
    print("YES")
else:
    print("NO")

# Вася обожает треугольники и решил попробовать сделать один самостоятельно.
# У него есть несколько алюминиевых трубочек разной длины, и он хочет узнать, 
# можно ли из них собрать треугольник.
b = int(input())
c = int(input())
d = int(input())
if b + c > d and c + d > b and d + b > c:
    print("YES")
else:
    print("NO")

# Во времена магии и драконов ходили легенды о числах, обладающих великой силой, 
# способной изменить мир.
# Три числа были даны эльфам, семь — гномам, а девять достались человеческому роду.
# Но все они были обмануты... Потому что существовало ещё одно число. В стране Нумия, 
# на бумаге из тёмного папируса, властелин Зерон тайно записал 
# Единую Цифру, подчиняющую себе все великие числа.
elf = int(input())
dwarf = int(input())
people = int(input())
a = elf // 10
b = elf % 10
c = dwarf // 10
d = dwarf % 10
e = people // 10
f = people % 10
if a == c == e:
    print(a)
elif a == c == f:
    print(a)
elif a == d == e:
    print(a)
elif a == d == f:
    print(a)
elif b == c == e:
    print(b)
elif b == c == f:
    print(b)
elif b == d == e:
    print(b)
elif b == d == f:
    print(b)

# Неверно
# Теперь, чтобы проникнуть в башни обоих злодеев одновременно,
# нужно разделить силу числа, которое защищало нас в дороге.
# Для этого возьмём трёхзначное число и составим из него 
# минимальное и максимальное возможные двухзначные числа. Каждая цифра 
# может использоваться не более того количества раз, сколько раз она встречается во входном числе.
number = int(input())
a = number // 100 % 10
b = number // 10 % 10
c = number % 10
max_num = max(a, b, c)
min_num = min(a, b, c)
other_num = a + b + c - max_num - min_num
min_to = f"{min_num}{other_num}"
max_to = f"{max_num}{other_num}"
print(max_to, min_to)

# Для этого нам нужно создать трёхзначное магическое число, которое будет сильнее двух 
# защитных чисел Зерона.
# Как его составить?
# Первая цифра — максимальная из всех защитных чисел.
# Последняя цифра — минимальная.
# Средняя цифра — сумма оставшихся цифр без учёта переноса разряда.
# Соберите это магическое число и помогите одолеть зло!
x1 = int(input())
x2 = int(input())
# Разбиваем первое число на цифры
a1 = x1 // 10
b1 = x1 % 10
# Разбиваем второе число на цифры
a2 = x2 // 10
b2 = x2 % 10
# Ищем максимальную цифру из 2 чисел
m = max(a1, b1, a2, b2)
n = min(a1, b1, a2, b2)
used_max = 0
used_min = 0
s = 0
if used_max == 0 and a1 == m:
    used_max = 1
elif used_min == 0 and a1 == n:
    used_min = 1
else:
    s = s + a1

if used_max == 0 and b1 == m:
    used_max = 1
elif used_min == 0 and b1 == n:
    used_min = 1
else:
    s = s + b1

if used_max == 0 and a2 == m:
    used_max = 1
elif used_min == 0 and a2 == n:
    used_min = 1
else:
    s = s + a2
    
if used_max == 0 and b2 == m:
    used_max = 1
elif used_min == 0 and b2 == n:
    used_min = 1
else:
    s = s + b2

y = s % 10
print(m, y, n, sep='')

# В новом сезоне за первенство в велогонках снова сражаются сильнейшие. 
# Протяжённость финальной трассы — 43872м, и все хотят узнать, кто первым пересечёт финишную черту.
# Нам известны средние скорости трёх претендентов — Пети, Васи и Толи. Кто станет победителем?
first_name = 'Петя'
first_speed = float(input())
second_name = 'Вася'
second_speed = float(input())
third_name = 'Толя'
third_speed = float(input())
if second_speed < third_speed:
    second_speed, third_speed = third_speed, second_speed
    second_name, third_name = third_name, second_name
if first_speed < third_speed:
    first_speed, third_speed = third_speed, first_speed
    first_name, third_name = third_name, first_name
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed
    first_name, second_name = second_name, first_name
print(f'{"":8}{first_name:^8}{"":8}')
print(f'{second_name:^8}{"":8}{"":8}')
print(f'{"":8}{"":8}{third_name:^8}')
print(f"{'II':^8}{'I':^8}{'III':^8}")

# Давайте воспользуемся его возможностями и найдём корни уравнения, используя составные условные операции.
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0 and c != 0:
    print("No solution")
elif a == 0:
    x = -c / b
    print(f"{x:.2f}")
elif a != 0:
    if D < 0:
        print("No solution")
    elif D == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    else:
        x1 = (-b - D**0.5) / (2 * a)
        x2 = (-b + D**0.5) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        print(f"{x1:.2f} {x2:.2f}")

# При этом риск столкнуться с ним зависел от формы треугольника:
# Остроугольный — вероятность встречи со злом крайне мала.
# Тупоугольный — опасность велика.
# Прямоугольный — вероятность 100%!
# Напишите программу, которая определяет вероятность встретить 
# зло по длинам сторон треугольника. Воспользуйтесь для этого составными условными операциями.
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
max_side = max(a, b, c)
min_side = min(a, b, c)
other_side = a + b + c - min_side - max_side
if min_side**2 + other_side**2 == max_side**2:
    print("100%")
elif min_side**2 + other_side**2 < max_side**2:
    print("велика")
else:
    print("крайне мала")

# руппа исследователей готовится к высадке на остров идеальной формы, но спутниковая разведка 
# обнаружила на нём зону зыбучих песков.
# Чтобы обеспечить безопасность экспедиции, разработана система оповещения, 
# которая предупреждает об опасности в зависимости от координат исследователя.
# Для снижения расходов было решено создать программное обеспечение, 
# которое автоматически определит, безопасна ли точка местонахождения исследователя.
x = float(input())
y = float(input())

if x**2 + y**2 > 100:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif x >= 0 and y >= 0 and x**2 + y**2 <= 25:
    print("Опасность! Покиньте зону как можно скорее!")
elif -4 <= x < 0 and 0 <= y <= 5:
    print("Опасность! Покиньте зону как можно скорее!")
elif -7 <= x < -4 and 0 <= y <= 5 and (5 * x - 3 * y) > -35:
    print("Опасность! Покиньте зону как можно скорее!")
elif (0.25 * x**2 + 0.5 * x - 9) <= y <= 0:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")

# Вам предстоит проверить три строки, найти среди них ту, где встречается слово "зайка", 
# и вывести её вместе с её длиной. Если таких строк несколько, выберите наименьшую в алфавитном порядке.
# Для этого используйте составные условные операции, чтобы одновременно учесть несколько условий.
text_1 = input()
text_2 = input()
text_3 = input()
hare_in_1 = "зайка" in text_1
hare_in_2 = "зайка" in text_2
hare_in_3 = "зайка" in text_3
if hare_in_1 and hare_in_2 and hare_in_3:
    result = min(text_1, text_2, text_3)
elif hare_in_1 and hare_in_2:
    result = min(text_1, text_2)
elif hare_in_2 and hare_in_3:
    result = min(text_2, text_3)
elif hare_in_3 and hare_in_1:
    result = min(text_3, text_1)
elif hare_in_1:
    result = text_1
elif hare_in_2:
    result = text_2
elif hare_in_3:
    result = text_3
print(result, len(result))