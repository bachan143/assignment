for fizzbuzz in range(100):
    if fizzbuzz % 2==0 and fizzbuzz % 3==0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 2==0:
        print("fizz")
        continue
    elif fizzbuzz % 3==0:
        print("buzz")
        continue
    else:
        print("fizzbuzz")
        