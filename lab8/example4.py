#10101000
def bit_to_baseten():
    ct=0
    sumof=0
    case=True
    while case==True:
        eibit=input("{Space to exit.}Enter 8 bit to convert base ten:")
        if len(eibit)==8:
            for i in eibit[::-1]:
                if i==0:
                    sumof=sumof+int(i)*(2**ct)
                    ct=ct+1
                else:
                    sumof=sumof+int(i)*(2**ct)
                    ct=ct+1
            case=False
        elif eibit=="":
            break
        else:
            print("Try again")
    print(sumof)
def baseten_to_bit():
 number=int(input("Enter a number:"))
 string=""
 i=7
 while i>-1:
      if (2**i)>number:
          string=string+"0"
      else:
          string=string+"1"
          number=number-(2**i)
      i=i-1
 print(string)

baseten_to_bit()
bit_to_baseten()