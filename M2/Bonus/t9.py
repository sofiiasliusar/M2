'''
Напишіть програму, яка починається з читання буквеної оцінки від користувача. 
Потім ваша програма повинна обчислити та відобразити еквівалентну кількість 
балів оцінок. Переконайтеся, що програма створює відповідне повідомлення 
про помилку, якщо користувач вводить неприпустиму оцінку букв.

'''
try:
    mark = input("Вкажіть вашу оцінку (A, B, C, D, F):").upper()
    if mark == "A":
        points = 5
    elif mark == "B":
        points = 4
    elif mark == "C":
        points = 3
    elif mark == "D":
        points = 2
    elif mark == "F":
        points = 1
    print(f"Ваша оцінка в балах - {points}.")

except:
    print("Введене значення невірне!")