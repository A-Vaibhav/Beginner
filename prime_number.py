def prime_number():
    num = int(input("Enter Number :"))
    i = 2
    flag = 0
    while(i<=num):
        if num%i == 0:
            flag+=1
    
        i+=1

    if flag == 1:
        return f"{num} is Prime Number"
    else:
        return f"{num} is Not Prime Number"
        

result = prime_number()
print(result)