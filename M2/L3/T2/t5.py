'''
Програма повинна запитати, яка температура на вулиці, 
і надрукувати одну з трьох відповідей: 
"Холодно!", "Тепло!", "Спекотно!". 
Ось схема роботи:

якщо введена температура більше 20 перевірити:
якщо введена температура більше 35 Друкувати : "Спекотно!" інакше Друкувати: "Тепло!"
в усіх інших випадках Друкувати: "Холодно!"

використовувати вкладений умовний оператор

'''

# Можливі відповіді: "Холодно!", "Тепло!", "Спекотно!".
# Тепло - це температура від 20 до 35.

temp = int(input("Вкажіть температуру повітря:"))
if temp > 20:
    if temp > 35:
        print("Спекотно!")
    else:
        print("Тепло!")
else:
    print("Холодно!")