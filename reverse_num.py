num = int(input("Enter a number: "))

def reverse_num(n):
    rev = 0
    while n > 0:
        last_digit = n % 10
        rev = rev * 10
        rev = rev + last_digit
        n = n // 10
    return rev    
print ("Revered number: " , reverse_num(num))