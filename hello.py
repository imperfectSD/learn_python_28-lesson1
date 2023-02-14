# Функции. Задание 1

def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    result = one + delimiter + two
    return result

result = str(get_summ("Learn", "python")) 
print(result.upper())