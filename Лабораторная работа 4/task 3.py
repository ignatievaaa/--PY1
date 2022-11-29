def delete(list_, index=None): # TODO реализовать функцию удаления элемента из списка по индексу
    value = len(list_)
    if index == None:
        index = len(list_) - 1
    if index < 0:
        index = value - index

    return list_[0:index] + list_[index + 1:len(list_)]

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
