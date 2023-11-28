'''
Трикутник можна класифікувати, виходячи з довжин його сторін, 
на рівносторонній, рівнобедрений або прямокутний. 
Всі три сторони рівностороннього трикутника мають однакову довжину. 
Рівнобедрений трикутник має дві сторони, які мають однакову довжину, 
і третю сторону, яка має різну довжину. Якщо всі сторони мають різну довжину, 
то трикутник рівносторонній.
Напишіть програму, яка зчитує довжини трьох сторін трикутника від користувача. 
Потім відобразіть повідомлення, в якому вказано тип трикутника.

'''
side1 = int(input("Введіть довжину першої сторони трикутника:"))
side2 = int(input("Введіть довжину другої сторони трикутника:"))
side3 = int(input("Введіть довжину третьої сторони трикутника:"))

if side1 == side2 == side3:
    type = "рівносторонній"
elif side1 == side2 or side1 == side3 or side3 == side2:
    type = "рівнобедрений"
elif side1 ** 2 == side2 ** 2 + side3 ** 2 or side2 ** 2 == side1 ** 2 + side3 or side3 ** 2 == side1 ** 2 + side2:
    type = "прямокутний"
elif side1 != side2 != side3:
    type = "різносторонній"

print(f"Тип трикутника - {type}.")

# 2 спосіб
# side1 = int(input("Введіть довжину першої сторони трикутника:"))
# side2 = int(input("Введіть довжину другої сторони трикутника:"))
# side3 = int(input("Введіть довжину третьої сторони трикутника:"))

# sides = [side1, side2, side3]
# print(sides)

# rest = [x for x in sides if x != max(sides)]
# # друкує елементи списку, які не дорівнюють максимальному значенню
# rest1 = rest[0]
# rest2 = rest[1]
# print(rest)
# #щоб не змінювати перший список, бо потрібні обидва
# if side1 == side2 == side3:
#     type = "рівносторонній"
# elif side1 == side2 or side1 == side3 or side3 == side2:
#     type = "рівнобедрений"
# elif max(sides) ** 2 == rest1 ** 2 + rest2 ** 2:
#     type = "прямокутний"
# elif side1 != side2 != side3:
#     type = "різносторонній"

# print(f"Тип трикутника - {type}.")

