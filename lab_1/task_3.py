# TODO Найдите количество книг, которое можно разместить на дискете


max_size = 1.44 * 1024 * 1024
size_knigi = 100 * 50 * 25 * 4
print("Количество книг, помещающихся на дискету:", int(max_size//size_knigi))
