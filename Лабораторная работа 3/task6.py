list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_i = 0
max_num = list_numbers[max_i]

for i, num in enumerate(list_numbers):  # перебираем пары индекс-значение
    max_num = list_numbers[max_i]
    if num >= max_num:  # если значение больше или равно исходного
        max_i = i  # то максимальное значение становится новым значением
        max_num = list_numbers[max_i]  # находим максимальное значение в исходном списке чисел

list_numbers[19], list_numbers[max_i] = list_numbers[max_i], list_numbers[19]  # меняем местами найденный последний элемент с максимальным

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]


