import math

print("The quadratic equation i.e ax2 + bx + c = 0 ")

a = int(input("Enter value for a"))
b = int(input("Enter value for b"))
c = int(input("Enter value for c"))
print("the roots are:-")

d=math.pow(b,2)-4*a*c
res1=(-b+math.sqrt(d))/(2*a)
res2=(-b-math.sqrt(d))/(2*a)

print(res1)
print(res2)