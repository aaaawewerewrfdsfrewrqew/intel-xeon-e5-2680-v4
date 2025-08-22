import math
import random

#1
try:
    a = float(input("введіть перше число: "))
    b = float(input("введіть друге число: "))
    print("результат ділення:", a / b)
except ValueError:
    print("введене значення не є числом")
except ZeroDivisionError:
    print("ділення на нуль не можливе")
finally:
    print("операцію завершено")

#2
lst = [10, 20, 30, 40, 50]
try:
    idx = int(input("Введіть індекс: "))
    print("Елемент списку:", lst[idx])
except ValueError:
    print("індекс повинен бути числом")
except IndexError:
    print("індекс виходить за межі списку")
finally:
    print("Операцію завершено")

#3
try:
    sales = list(map(float, input("введіть дані про продажі через пробіл: ").split()))
    print("Сума продажів:", sum(sales))
except ValueError:
    print("некоректне введення")
finally:
    print("Обробку завершено")

# 4
try:
    num = float(input("Введіть число: "))
    if num < 0:
        raise Exception("Не можна обчислити квадратний корінь від'ємного числа")
    print("квадратний корінь:", math.sqrt(num))
except ValueError:
    print("значення не є числом")
except Exception as e:
    print(e)
finally:
    print("Обчислення завершено")

#5
try:
    data = input("введіть товар у форматі: назва, ціна, кількість: ")
    name, price, qty = data.split(",")
    price = float(price.strip())
    qty = int(qty.strip())
    print("товар:", name.strip(), "| Ціна:", price, "| Кількість:", qty)
except ValueError:
    print("Помилка: некоректні дані")
finally:
    print("завершено")

#6
def connect_to_server():
    if random.choice([True, False]):
        return "Підключення успішне"
    else:
        raise ConnectionError("помилка підключення")

try:
    print(connect_to_server())
except ConnectionError:
    print("не вдалося підключитися до сервера")
finally:
    print("спробу завершено")