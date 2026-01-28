student = {
    "name": "Amit",
    "age": 21,
    "course": "MCA"
}

marks = {
    "Amit": 98,
    "Subham": 68,
    "Rohan": 78
}

print(student.items())
print(student.keys())
print(student.values())
student.update({"age": 22})
print(student["name"],student["age"])

print(marks)
marks.update({"Rahul": 77})
print(marks)
print(type(marks))
print(marks["Subham"])
print(marks["Rohan"])
print(marks.get("Amit1"))

a = {}  # Empty Dictionary
print(type(a))