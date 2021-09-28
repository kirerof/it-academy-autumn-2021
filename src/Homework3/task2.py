"""2. List practice"""


import copy


"""1. Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd']."""
lst = [(letter1 + letter2) for letter1 in 'ab' for letter2 in 'bcd']
print('1: ', lst)


"""2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc']."""
print('2: ', lst[::2])


"""3. Используйте генератор списков чтобы получить следующий: ['1a', '2a', '3a', '4a']."""
lst2 = [str(element1) + 'a' for element1 in '1234']
print('3: ', lst2)


"""4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его."""
print('4: ', lst2.pop(1))


"""5. Скопируйте список из прошлого пункта и добавьте в него элемент '2a' так,
чтобы в исходном списке этого элемента не было."""
lst3 = copy.copy(lst2)
lst3.insert(1, '2a')
print('5: ', lst3)
