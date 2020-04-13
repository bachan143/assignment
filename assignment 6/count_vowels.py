str=str(input("Enter the String"))
vcount=0
for i in range(0,len(str)):
    if str[i] in('a','e','o','u','i'):
        vcount=vcount+1
if(vcount>0):
    print(vcount,"vowels are in ",str)
else:
    print(vcount," vowels are in",str)







