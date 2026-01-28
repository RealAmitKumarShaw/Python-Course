name = "Amit Kumar Shaw" # Strings Are immutable
print(name)
namelength = len(name)
print(namelength)
print(name.endswith("aw")) # True
print(name.endswith("Aw")) # False
print(name.startswith("amit")) # False
print(name.startswith("Ami")) # False

# name[0] = "N" # You can't do this

# Changing Case
print(name.upper())
print(name)
print(name.lower())
name1 = "ajit KumaR PaUl"
print(name1.title())
print(name1.capitalize())

# Removing Whitespace
text = "  hello world  "
print(text)
print(text.strip())  # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: "  hello world"

# Finding and Replacing
text1 = "Python is fun and fun and fun"
print(text1.find("is"))   # Output: 7
print(text1.replace("fun", "awesome"))  # Output: "Python is awesome"
print(text1)