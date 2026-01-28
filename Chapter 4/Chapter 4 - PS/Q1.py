# 1. Write a program to store seven fruits in a list entered by the user.

fruits = []

for i in range (7):
    f = input(f"Enter {i+1} Fruit name: ")
    fruits.append(f)

print(fruits)