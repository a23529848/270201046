hnames=int(input("How many people:"))
n_list=[]
n1=""
for _ in range(hnames):
    name=input("Name:")
    age=int(input("Age:"))
    tuple1=(name,age)
    if age>18:
        n1=n1+name+"\n"
    n_list.append(tuple1)
print(n1)

