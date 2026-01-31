# Class: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# Object: An instance of a class. It is created using the class blueprint and can have its own unique attributes and behaviors.

class employee:         # create class

    language = "Py"     # create attribute
    salary = 1000000

amit = employee() # create object
amit.name = "Amit"  # create attribute using object (instance attribute)
print(amit.name, amit.salary, amit.language)   # access attribute using object

rohan = employee()
rohan.name = "Rohan Ojha"
print(rohan.name, rohan.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class