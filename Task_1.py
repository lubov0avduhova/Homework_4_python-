# Вычислить число c заданной точностью d
# Пример:

#     при $d = 0.001, π = 3.141


number_p = list('3.14159265358979323')

# find_number = (input('Введи число в формате, например, 0.001: '))
test = list(input('Введите число: '))
i = 0
result = []


while(i < len(test)):
        result.append(number_p[i])
        i+=1
    
print(result)