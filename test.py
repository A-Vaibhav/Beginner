size = 5
k = size-1

for i in range(0,5):
    for j in range(k):
        print(end=" ")

    k=k-1

    for v in range(i):
        print("*",end=" ")

    print("\r")