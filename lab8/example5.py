
def level(string):
    level=0
    al=0
    num=0
    spec=0
    if len(string)<8:
        return level
    else:
        for i in string:
            if i.isalpha()==True:
                al=al+1
            elif i.isspace()==True:
                return level
            elif i.isalnum()==True:
                num=num+1
            else:
                spec=spec+1
    
        if spec>0:
            level=level+1
        if al>0:
            level=level+1
        if num>0:
            level=level+1
            
    return level
    
        
password=input("Your Password:")

level_of=level(password)
print(f"Level Of Your Password {level_of}")
