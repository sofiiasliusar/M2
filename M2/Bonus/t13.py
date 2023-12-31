'''
Найбільшим спільним дільником двох натуральних чисел, n і m, 
є найбільше число, d, яке ділиться рівномірно як на n, так і на m. 
Існує кілька алгоритмів, які можуть бути використані для вирішення 
цього завдання.
    Напишіть програму, яка зчитує два додатніх цілих числа від користувача 
і використовує алгоритм для визначення і повідомлення їх найбільшого 
спільного дільника
'''
try:
    def find_result(n, m):
        while m: #поки b не 0 і відповідно True
            n, m = m, n % m #присвоюємо n залишок від ділення
        return n


    n = int(input("Введіть перше число: "))
    m = int(input("Введіть друге число: "))
    result = find_result(n, m)
    print(f"Найбільший спільний дільник чисел {n} і {m} - {result}")
    
except ValueError:
    print("Будь ласка, введіть правильні цілі числа.")

