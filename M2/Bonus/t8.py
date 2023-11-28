'''
Напишіть програму, яка просить користувача ввести свій місяць і день народження. 
Потім ваша програма повинна повідомити знак зодіаку користувача як частину 
відповідного вихідного повідомлення.

Козеріг з 22 грудня по 19 січня
Водолій з 20 січня по 18 лютого
Риби з 19 лютого по 20 березня
Овен з 21 березня по 19 квітня
Телець з 20 квітня по 20 травня
Близнюки з 21 травня по 20 червня
Рак з 21 червня по 22 липня
Лев з 23 липня по 22 серпня
Діва з 23 серпня по 22 вересня
Терези з 23 вересня по 22 жовтня
Скорпіон з 23 жовтня по 21 листопада
Стрілець з 22 листопада по 21 грудня


'''
date = int(input("Вкажіть свою дату народження:"))
month = input("Вкажіть свій місяць народження:").lower()
try:
#перевіряємо чи дата дорівнює хоча б одному числу від 22 до 32, виключаючи 32
    if date in range(22, 32) and month == "грудень" or date in range (1, 20) and month == "січень":
        sign = "козеріг"
    elif date in range(20, 32) and month == "січень" or date in range (1, 19) and month == "лютий":
        sign = "водолій"
    elif date in range(19, 30) and month == "лютий" or date in range (1, 21) and month == "березень":
        sign = "риби"
    elif date in range(21, 32) and month == "березень" or date in range (1, 20) and month == "квітень":
        sign = "овен"
    elif date in range(20, 31) and month == "квітень" or date in range (1, 21) and month == "травень":
        sign = "телець"
    elif date in range(21, 32) and month == "травень" or date in range (1, 21) and month == "червень":
        sign = "близнюки"
    elif date in range(21, 31) and month == "червень" or date in range (1, 23) and month == "липень":
        sign = "рак"
    elif date in range(23, 32) and month == "липень" or date in range (1, 23) and month == "серпень":
        sign = "лев"
    elif date in range(23, 32) and month == "серпень" or date in range (1, 23) and month == "вересень":
        sign = "діва"
    elif date in range(23, 31) and month == "вересень" or date in range (1, 23) and month == "жовтень":
        sign = "терези"
    elif date in range(23, 32) and month == "жовтень" or date in range (1, 22) and month == "листопад":
        sign = "скорпіон"
    elif date in range(22, 31) and month == "листопад" or date in range (1, 22) and month == "грудень":
        sign = "стрілець"
    print(f"Ваш знак зодіаку - {sign}.")
except:
    print("Перевірте дані!")

