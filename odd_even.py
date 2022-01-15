def odd_even():
    num = int(input("Enter Number :"))

    if num%2==0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

result = odd_even()
print(result)