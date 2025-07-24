# 1. Create a list of 5 integers and access items by index
lst = [10, 20, 30, 40, 50]
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])

# 2. Append a new item to the end of the list
lst = [1, 2, 3, 4]
lst.append(5)
print(lst)

# 3. Reverse the order of the items in the list
lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)

#4. Print the number of occurrences of a specified element in a list
lst = [1, 2, 2, 3, 4, 2, 5]
print(lst.count(2))

#5. Append the items of list1 to list2 in the front
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print(list2)

# 6. Insert a new item before the second element in an existing list
lst = [10, 30, 40]
lst.insert(1, 20)
print(lst)

#7. Remove the item from a specified index in a list
lst = [10, 20, 30, 40, 50]
del lst[2]
print(lst)

# 8. Remove the first occurrence of a specified element from a list
lst = [1, 2, 3, 2, 4, 2]
lst.remove(2)
print(lst)
