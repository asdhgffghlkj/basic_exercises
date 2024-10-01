# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
my_dict = {}
for element in students:
    name = element["first_name"]
    if name in my_dict:
        my_dict[name] += 1
    else:
        my_dict[name] = 1

for key, value in my_dict.items():
    print(f"{key}: {value}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
print("")
counter = {}
for element in students:
    name = element["first_name"]
    if name not in counter:
        counter[name] = 1
    else:
        counter[name] += 1
print(f"Самое частое имя среди учеников: {max(counter, key=counter.get)}")



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print("")
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???

counter = {}
for element in students:
    name = element["first_name"]
    if name not in counter:
        counter[name] = 1
    else:
        counter[name] += 1
print(f"Самое частое имя среди учеников: {max(counter, key=counter.get)}")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]

is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
print("")
for grade in school:
    boys, girls = 0, 0
    for element in grade["students"]:
        if is_male[element["first_name"]]:
            boys += 1
        else:
            girls += 1
    print(f"Класс {grade['class']}: девочки {girls}, мальчики {boys}")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

# ???
print("")
gender_per_class = {}
for grade in school:
    gender_count = [0, 0]
    for element in grade["students"]:
        if is_male[element["first_name"]]:
            gender_count[0] += 1
        else:
            gender_count[1] += 1
    gender_per_class[grade['class']] = gender_count
print(f"Больше всего мальчиков в классе {max(gender_per_class, key=lambda k: gender_per_class[k][0])}")
print(f"Больше всего девочек в классе {max(gender_per_class, key=lambda k: gender_per_class[k][1])}")
