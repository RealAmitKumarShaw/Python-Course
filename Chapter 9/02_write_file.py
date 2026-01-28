# Write something in a new file called New File.txt

f = open("New File.txt", "w")

str = """
'r' (Read mode): Opens the file for reading. This is the default mode. If the file doesn't exist, you'll get an error.
'w' (Write mode): Opens the file for writing. If the file exists, its contents will be overwritten. If the file doesn't exist, a new file will be created.
'a' (Append mode): Opens the file for appending. Data will be added to the end of the file. If the file doesn't exist, a new file will be created.
"""

f.write(str)
f.close

f = open("New File.txt", "r")
content = f.read()

print(content)
f.close()