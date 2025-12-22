num = int(input("Enter the number: "))

def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = is_even(num)
print("The number is :",result)
