# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

from re import I


number = 20

def Factor(number):
    list_numbers = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            list_numbers.append(i)
            number //= i
        else:
            i += 1
    if number > 1:
        list_numbers.append(number)
    return list_numbers

print(Factor(number))