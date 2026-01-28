def factorial(n):
    if n < 1:                       # Base Condition
        return 1
    else:
        return n * factorial(n - 1) # Function call with updated argument. 
    
n = int(input("Enter the number to find fectorial: "))
print(f"Factorial of {n} is {factorial(n)}")