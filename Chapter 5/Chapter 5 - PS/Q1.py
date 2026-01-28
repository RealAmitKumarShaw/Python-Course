# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up

hindi_english_dict = {
    "Madat": "Help",
    "Pustak": "Book",
    "Vidyarthi": "Student",
    "Shikshak": "Teacher",
}

word = input("Enter a Hindi word to translate: ")
print(hindi_english_dict[word])