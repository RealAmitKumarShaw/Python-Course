# 1. Write a program using functions to find greatest of three numbers.

def greatest(n1, n2, n3):
    if n1 > n2 and n2 > n3:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n3
    
a = int(input("Enter 1st number: "))
b = int(input("Enter 1st number: "))
c = int(input("Enter 1st number: "))

number = greatest(a, b, c)
print("Greatest Number = ",number)