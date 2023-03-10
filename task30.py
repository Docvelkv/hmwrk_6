# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# pytest -v tests\test_30.py
from addInterface import correct_int


def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    """Возвращает список арифметической прогрессии по заданным:
    1) первый элемент
    2) разность
    3) количество элементов"""

    output_list = []
    for i in range(quantity):
        an = first + i * diff
        output_list.append(an)
    return output_list


print("Введите первый элемент АП: ", end="")
num_first = correct_int()
print("Введите разность АП: ", end="")
num_diff = correct_int()
print("Введите количество элементов АП: ", end="")
quantity_nums = correct_int()
list_ap = arithmetic_progression(num_first, num_diff, quantity_nums)
print(*list_ap)
