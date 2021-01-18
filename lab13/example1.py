

def rec_binary_search(number,list):
    if len(list)>0:
        middle_index=len(list)//2
        middle_value=list[middle_index]
        if number==middle_value:
            return print("I HAVE FOUNDED!")
        else:
            if len(list) == 1 and middle_value!=number:
                return print("I couldn't find it")

            if number>middle_value:
                return rec_binary_search(number,list[middle_index+1:])
            else:
                return rec_binary_search(number, list[:middle_index])


liste=[2,3,4,7,8,9,9]

rec_binary_search(8,liste)
rec_binary_search(3,liste)
rec_binary_search(1,liste)