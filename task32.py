# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# pytest -v tests\test_32.py
from addInterface import correct_int, creat_int_list


def is_in_mass(num_lst: list[int],
               min_num: int,
               max_num: int) -> list[int]:
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num] """

    output_list = []
    for i in range(len(num_lst)):
        if num_lst[i] >= min_num and num_lst[i] <= max_num:
            output_list.append(i)
    return output_list


input_lst = creat_int_list(51, 1, 50)
print("Введите начало диапазона: ", end="")
minimum = correct_int()
print("Введите конец диапазона: ", end="")
maximum = correct_int()
output_lst = is_in_mass(input_lst, minimum, maximum)
print(f"Входной список: {input_lst}.\nДиапазон от {minimum} "
      f"до {maximum}.\nИндексы элементов: {output_lst}.")
