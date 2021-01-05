

my_list = [0, 1, 2, 3, 4, 5]


def even_number_counter(my_list):
    if len(my_list)==0:
        return 0

    if my_list[0] % 2==0:
        counter = 1
        return even_number_counter(my_list[1:])+counter
    else:
        counter=0
        return even_number_counter(my_list[1:])+counter

print(even_number_counter(my_list))