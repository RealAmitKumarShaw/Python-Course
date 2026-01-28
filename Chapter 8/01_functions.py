# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# c = int(input("Enter number: "))

# avg = (a+b+c)/3
# print(f"Average = {avg}")

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# c = int(input("Enter number: "))

# avg = (a+b+c)/3
# print(f"Average = {avg}")  
""" It will be very dificult to write this code again again.
To Solve this problem function was introduce."""

# Function
def avg():               # Function Defination
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    c = int(input("Enter number: "))

    avg = (a+b+c)/3
    print(f"Average = {avg}")

avg()                   # Function Call

for i in range(5):      # Here function avg will be call 5 times
    avg()
