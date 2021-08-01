def fibonacci(anger):
    num_1 = 0
    num_2 = 1
    print(num_1)
    print(num_2)
    for i in range(anger-2):
        num_3 = num_1+num_2
        print(num_3)
        num_1 = num_2
        num_2 = num_3


anger = int(input("put a number"))
fibonacci(anger)
