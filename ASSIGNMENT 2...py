n= int(input("Enter N:"))
if (n % 2) !=0 and n<100:
    print("Weird")
elif (n % 2)==0 and (n>=2 and n<=5):
    print("Not weird")
elif (n % 2)==0 and (n>=6 and n<=20):
    print("Weird")
elif (n % 2)==0 and  n>=20 and n<100:
    print("Not weird")
elif n>100 :
    print("Is too big try again")
else:
    print("Is not allowed")
