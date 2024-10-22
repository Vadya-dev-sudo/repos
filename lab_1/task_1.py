

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_without_none = []

a = 0
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = 0
        a = i
        break

numbers[a] = (sum(numbers))/(len(numbers))


print("Измененный список:", numbers)
