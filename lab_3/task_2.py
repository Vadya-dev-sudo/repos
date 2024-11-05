# TODO Напишите функцию find_common_participants
def func(first_gr, second_gr, sep=","):
    first_gr_l = first_gr.split(sep)
    second_gr_l = second_gr.split(sep)

    partic = set(first_gr_l) & set(second_gr_l)

    return sorted(partic)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
separator = "|"
com_partic = func(participants_first_group,participants_second_group, separator)
print(com_partic)