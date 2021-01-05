xd=[3,12,76,[4,56,43],[2,8],81,75]


def flat_list(a_list):
    new_list = list()
    if len(a_list) == 0:
        return new_list
    if type(a_list[0]) == list:
        item = a_list[0]
        for i in item:
            new_list.append(i)
    else:
        new_list.append(a_list[0])
    return flat_list(a_list[1:]) + new_list


def sum_of_flat_list(a_list):
    if len(a_list) == 0:
        return 0
    return a_list[0] + sum_of_flat_list(a_list[1:])


print(sum_of_flat_list(flat_list(xd)))
