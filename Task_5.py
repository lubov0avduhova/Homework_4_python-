# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import sympy
from sympy.abc import x


first_polynomial = open('Task_5_1.txt', 'r')
second_polynomial = open('Task_5_2.txt', 'r')


first_str = sympy.core.sympify(first_polynomial.read())

second_str = sympy.core.sympify(second_polynomial.read())

result = sympy.latex(first_str+second_str)


text_file = open("task_5_result.txt", "w")
n = text_file.write(result)
text_file.close()  
first_polynomial.close()
second_polynomial.close()