import random

def get_rand_list(b,e,n):
    created_list=list()
    for _ in range(5):
        x=random.randint(b,e)
        created_list.append(x)
    return created_list
        
def overlap(b,e,n):
    first=get_rand_list(b, e,n)
    print(first)
    second=get_rand_list(b, e,n)
    print(second)
    c = list(set(first).intersection(set(second)))
    return c
    
print(overlap(0,10,5))