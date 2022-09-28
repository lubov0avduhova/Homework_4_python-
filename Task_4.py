# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

#     k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def new_number():
    random_num = random.randint(0,10)
    if(random_num < 2):
        return ''
    return random_num


def add_number_to_string(k):
    if(k == 0):
        print('Это не многочлен')

    random_num = new_number()
    list_num.insert(0, f'{random_num} ') # число 5 = 0
    if(random_num != ''):
        list_num.insert(0, f' + ')
    

    random_num = new_number()
    list_num.insert(0, f'{random_num}x') # добавляем х, пример, 2x + 5 = 0
    if(k < 2):
        new_str = ''.join(list_num)
        return new_str

    if(k > 2):
            i = 2
            while (i <= k):
                list_num.insert(0, f'{new_number()}x^{i} + ')
                new_str = ''.join(list_num) # x+0
                if(i == k):
                     return new_str
                i+=1
            

list_num = ['=',' ', '0']
k = 4

text_file = open("task_4.txt", "w")
n = text_file.write(add_number_to_string(k))
text_file.close()   