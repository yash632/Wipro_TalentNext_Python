# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.
t = (1, 2, 3, 4, 5, 6, 7, 8)
print(t[3])
print(t[-4])

#2. Write a program to check whether an element exists in a tuple or not.
t = (1, 2, 3, 4, 5)
x = 3
if x in t:
    print("Exists")
else:
    print("Not Exists")

#3. Write a program to convert a list into a tuple.
l = [1, 2, 3, 4]
t = tuple(l)
print(t)

#4. Write a program to find the index of an item in a tuple.
t = (10, 20, 30, 40, 50)
x = 30
print(t.index(x))

#5. Write a program to replace last value of tuples in a list to 100.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
result = []
for i in l:
    result.append(i[:-1] + (100,))
print(result)

