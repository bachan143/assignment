def recur_fact(num):
    if num <= 1:
        return 1
    else :
        return num*recur_fact(num-1)
num =5;
print("factorial of",num,"is",recur_fact(num))