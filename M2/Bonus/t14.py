'''
Напишіть програму, яка перетворює двійкове число (з основою 2) 
в десяткове (з основою 10). Ваша програма повинна починатися 
з читання двійкового числа від користувача у вигляді рядка. 
Потім слід обчислити еквівалентне десяткове число, 
обробляючи кожну цифру двійкового числа. 
Нарешті, ваша програма повинна відображати еквівалентне десяткове 
число з відповідним повідомленням.
'''

binary_input = input("Введіть двійкове число: ")
decimal_result = int(binary_input, 2)
print(f"Десятковий еквівалент: {decimal_result}")