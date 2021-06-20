num=int(input("enter a number"))
if num%2!=0:
    print("weird")
if num%2==0:
     if num in range(2,6):
         print("not weird")
     elif num in range(6,21):
         print("weird")
     else :
         print("not weird")
        

        
