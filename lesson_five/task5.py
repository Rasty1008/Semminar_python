'''
 Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.
*Пример:* 
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
'''

lst = [1, 5, 2, 3, 4, 6, 1, 7]

L = [] 
M = []
j = 1
while j < len(lst):
    i = j
    N = lst[:]
    while i < len(N) - 1:
        if N[i] < N[i + 1]:
            M.append(N[i])
            i += 1
        else:
            N.pop(i + 1)

    j += 1
    if len(L) < len(M):
        L = M
    M = []

if lst[-1] > L[ -1]:
    L.append(lst[ - 1])
if lst[0] < L[0]:
    L.insert(0, lst[0])
print(L)

#Вариант решение рекурсией
from pprint import pprint

numbers = [1, 5, 2, 3, 4, 6, 1, 2, 7] 
seq = set()

def find_sequenses(arr, cur_i = 0, cur_seq = tuple()):
    #Точка выхода: когда индекс вышел за границу
    if cur_i == len(arr):
        if len(cur_seq) > 1:
            seq.add(cur_seq)
        return

    #Ищем дальше, игнурируя текущий элемент
    find_sequenses(arr, cur_i + 1, cur_seq)

    #Ищем дальше, используя текущий элемент, но только если он подходящий
    if (cur_seq and cur_seq[-1] <= arr[cur_i] or not(cur_seq)):
        find_sequenses(arr, cur_i + 1, cur_seq + (arr[cur_i],))

find_sequenses(numbers)

pprint(seq)
print(len(seq))