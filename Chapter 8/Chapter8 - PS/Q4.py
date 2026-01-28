# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
    
num = int(input("Enter the natural number: "))
a = sum(num)

print(f"Sum of {num} natural number is {a}")