"""3. Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором."""
a = [1, 2, 4, 6, 7, 12, 34, 52]
b = [11, 3, 5, 2, 12, 52, 45]
print(len(set(a) & set(b)))