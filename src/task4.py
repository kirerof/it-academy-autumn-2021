"""4. Даны два списка чисел. Посчитайте, сколько различных чисел входит только
в один из этих списков."""
a = [12, 43, 1, 5, 67, 4]
b = [8, 10, 16, 1, 6, 67]
print(len(set(a) ^ set(b)))
