# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

#     k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


list_num = ['x', '=', '0']
random_num = random.randint(2,10)


k = 1
i = 0

if(k == 1):
    list_num.insert(0, f'+{random_num}')
    new_str = ''.join(list_num) # x+0
    print(new_str)
    print(i)
    
# while(i <= k):
#     our_number = f'{random_num}x{k} +'
#     new_string += our_number
#     i+=1


# print(new_string + test)