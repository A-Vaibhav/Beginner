def fibonacci_series():
    number = int(input("Enter the Range for the Fibonacci Series : "))

    fibo = [0,1]
    summ = 0

    for i in range(number+1):
        summ = fibo[i] + fibo[i+1]
        fibo.append(summ)

    return f"Sum of {fibo} : {sum(fibo)}"

print(fibonacci_series())