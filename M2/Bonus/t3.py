'''
Напишіть програму, яка визначає ім'я фігури за кількістю сторін.
Прочитайте кількість сторін від користувача, 
а потім повідомте відповідне ім'я як частину змістовного повідомлення. 
Ваша програма повинна підтримувати фігури з будь-якого місця 
від 3 до 10 сторін (і включно). 
Якщо введено кілька сторін за межами цього діапазону, 
то ваша програма повинна видати відповідне повідомлення про помилку.

'''
figure = int(input("Введіть кількість сторін фігури (від 3 до 10):"))
try:

    if figure == 3:
        name = "трикутник"
    elif figure == 4:
        name = "квадрат"
    elif figure == 5:
        name = "пентагон"
    elif figure == 6:
        name = "гексагон"
    elif figure == 7:
        name = "гептагон"
    elif figure == 8:
        name = "октагон"
    elif figure == 9:
        name = "нонагон"
    elif figure == 10:
        name = "декагон"
    print(f"Це - {name}.")

except:
    print("Введіть число із заданого діапазону!")
