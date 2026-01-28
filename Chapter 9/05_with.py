with open("amit.txt", "r") as f:
    content = f.read()
    print(content) # No need to write f.close(), it's done automatically