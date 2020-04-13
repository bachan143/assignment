number=input("enter phonenumber")
otp=''
length=len(number)
for odd in range(1,length,2):
    otp+=str(int(number[odd])**2)
print(otp[0:4])