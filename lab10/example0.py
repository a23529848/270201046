
def product(num,x):
    if x==0:
        return 0
    return product(num,x-1)+num
print(product(6,4))

