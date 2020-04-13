number=int(input("Enter the number"))
temp=number
rev=0
while(number>0):
    dig=number%10
    rev=rev*10+dig
    number=number//10
if(temp==rev):
    print("The number is palindrom")
else :
    print("The number is not palindrom")
