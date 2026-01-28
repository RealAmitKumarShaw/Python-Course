# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

for i in range(6):
    mark = float(input(f"Enter the marks of student {i + 1}: "))
    marks.append(mark)

print(f"Marks of all the student = {marks}")
marks.sort()
print(f"Marks of all the student After sort = {marks}")