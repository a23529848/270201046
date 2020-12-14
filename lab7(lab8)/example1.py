

def square_of_sum(numbers):
 sumof=0

 for i in numbers:
   sumof=sumof+i
 value=sumof**2
 return value

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
print(square_of_sum(a_list))