'''
1 Вычислить число π c заданной точностью d
*Пример:* 
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''
'''
#Алгоритм вычисления числа ПИ
def pi_numb():
    k = 1
    sum = 0
    for i in range(100):
        if i % 2 == 0:
            sum += 4/k
        else:
            sum -= 4/k
        k += 2
        print(sum)       
pi_numb()
'''
from math import pi

d =  int(input("Введите число: "))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')