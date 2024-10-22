
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_without_none = []

for i in numbers:
    if i is not None:
        numbers_without_none.append(i)
summ = 0
for i in numbers_without_none:
    summ += i

sr_arif = summ/(len(numbers_without_none) + 1)

for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = sr_arif

print("Измененный список:", numbers)
