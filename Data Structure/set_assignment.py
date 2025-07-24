# 1. Write a program to remove a given item from the set.
s = {1, 2, 3, 4, 5}
s.remove(3)
print(s)

#2. Write a program to create an intersection of sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a & b
print(c)

#3. Write a program to create a union of sets.
a = {1, 2, 3}
b = {3, 4, 5}
c = a | b
print(c)

#4. Write a program to find the maximum and minimum value in a set.
s = {10, 20, 5, 40, 15}
print(max(s))
print(min(s))
