x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

def maximum(a,b):
    if a > b:
        return a
    return b
print("Maximum number is: " , maximum(x,y))