# String Slicing
full_name = "Amit Kumar Shaw"
print(full_name)
namelength = len(full_name)
print(namelength)

# sl = name[index_Start : index_End]
nameshort = full_name[0:3] # It will print 0 to (3 - 1) ie. 2
print(nameshort)
nameshort2 = full_name[2:-3] # Same as full_name[2:12]
print(nameshort2)

# String Slicing
text = "Hello, Python!"
print(text[0:5])   # Output: Hello
print(text[:5])    # Output: Hello (same as text[0:5])
print(text[7:])    # Output: Python! (from index 7 to end)
print(text[::2])   # Output: Hlo Pto!
print(text[-6:-1]) # Output: ython (negative indexing)
print(text[::-1])  # Output: !nohtyP ,olleH (reverses string)