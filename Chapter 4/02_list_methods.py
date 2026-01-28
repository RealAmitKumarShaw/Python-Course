friends = ["Apple", "Orange", 5, 345.87, False, "Amit", "Ajay"]
print(friends)

friends.append("Harry")     # Used to add new element at the end of the list
print(friends)

l1 = [1, 31, 12, 45, 10, 9]
l1.sort()                   # Used to sort the element of the list.
l1.reverse()                # Used to reverse the element of the list.
print(l1)
l1.insert(3, 55)            # Used to Insert new element at the given index number (index_No , element).
print(l1)
print(l1.pop(4))            # Will delete element at index 4 and return its value.
print(l1)

l2 = [31, 56, 99, 33]
l1.extend(l2)               # Used to add another list at the end of the previous list
print(l1)