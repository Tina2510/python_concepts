num = int(input("Enter a number: "))

def sum_of_digits(n):
        total = 0
        while n > 0:
            last_digit = n % 10
            if n%2!=0:
                total = total + last_digit
            n = n // 10
        return total
print("Sum of digits:", sum_of_digits(num))    

