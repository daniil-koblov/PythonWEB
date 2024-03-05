for k in (0, 4):
    print("\n")
    for i in range(2, 10):
        print(" ")
        for j in range(2 + k, 6 + k):
            print(f"{j} * {i} = {i * j} \t", end="")
