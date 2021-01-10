
# with all steps of triangle

def rec_pascal(n):
    if n == 1:
        print([1])
        return [1]
    else:
        array = rec_pascal(n - 1)
        counter = 0
        counter_k = 1
        sum_list = []
        sum_list.append(array[0])
        sum_list.append(array[-1])

        while len(array) >= len(sum_list):
            case = array[counter] + array[counter_k]
            sum_list.insert(1, case)
            counter = counter + 1
            counter_k = counter_k + 1
        print(sum_list)
        return sum_list

rec_pascal(4)