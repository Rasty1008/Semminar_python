'''
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''

def input_value(x):
    xyz = ["X", "Y", "Z"]
    lst = []
    for i in range(x):
        lst.append(input(f"Введите значение {xyz[i]}: "))
    return lst

def predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

input_user = input_value(3)

if predicate(input_user) == True:
    print("Истинно")
else:
    print("Ложь")