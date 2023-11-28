'''
Потрібно порахувати суму чисел від a до b. 
Програма запитує два числа і виводить результат - одне число.


TODO input:
2
4
TODO output:
9
'''
a = int(input("Введіть число a:"))
b = int(input("Введіть число b:"))
result = 0
for i in range(a, b+1):
    result += i
print(result)
