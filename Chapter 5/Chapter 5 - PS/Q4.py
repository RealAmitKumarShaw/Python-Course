# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

for i in range(4):
    name = input(f"Enter name of Student {i+1} ")
    language = input(f"Enter language of Student {i+1} ")
    d.update({name: language})

print(d)
print(d.keys())
print(d.values())
    