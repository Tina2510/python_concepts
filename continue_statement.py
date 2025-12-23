even_sum, odd_sum = 0,0
n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    if i%2==0:
        even_sum += i
        continue
    odd_sum += i
print("Sum of all even numbers is: ", even_sum)
print("Sum of all odd numbers is: ", odd_sum)
    

