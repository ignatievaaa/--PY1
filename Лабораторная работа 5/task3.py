from random import randint


def get_unique_list_numbers() -> list[int]:
    list = []
    start = -10
    stop = 10
    count = 15
    i = 0
    while i < count:
        var = randint(start, stop)
        if var not in list:
            list.append(var)
            i = i + 1
    return list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
#  Комментарий для пустой строки в конце кода