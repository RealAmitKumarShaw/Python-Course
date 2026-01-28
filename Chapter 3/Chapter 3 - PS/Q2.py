# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
#        Dear <|Name|>, 
#        You are selected! 
#        <|Date|> 
#         '''


name = input("Enter your name\n")
date = input("Enter the date\n")

print(f'''  
       Dear {name}, 
       You are selected! 
       {date} 
        ''')