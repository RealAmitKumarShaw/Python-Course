def greet(name):        # Function with argument.
    print(f"Hi {name} Good Morning")
    print("Nice to meet you!")
    return 7

n = input("Enter your name: ")
greet(n)                # Function call by refrence.

a = greet(n)
print(a)