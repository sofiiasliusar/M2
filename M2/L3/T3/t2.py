'''
Виправте помилки. 
Програма повинна запитувати у користувача колір крокодила, 
поки він не введе правильну відповідь.
'''

answer = "зелений"
color = input("Якого кольору крокодил?")
while answer != color:
    print ("Ні!")
    color = input ("Якого кольору крокодил?")
print ("Молодець, ти вгадав!")