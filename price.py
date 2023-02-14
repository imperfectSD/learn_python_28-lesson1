# Функции. Задание 2

def format_price(price):
    price = int(price)
    return("Цена: " + str(price) + " руб.")

a = format_price(56.24)
print(a)