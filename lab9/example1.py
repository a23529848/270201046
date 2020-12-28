
# Iterative One
# My Solution
def reversed(my_list):
  reversed_list=[]
  for i in my_list[::-1]:
    reversed_list.append(i)
  return reversed_list

my_list=[1,2,3,4]
x=reversed(my_list)
print(x)

# Recursive One

def FlipList(my_list):
    takeAList=[]
    if len(my_list) == 1:
        takeAList.append(my_list[0])
        return takeAList
    else:
        takeAList.append(my_list[-1])
        return takeAList + FlipList(my_list[:-1])

arr1=[2,3,4,5,6]

print(FlipList(arr1))
