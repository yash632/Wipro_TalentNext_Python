# 1. Add a key and value to a dictionary
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}
d = {0: 10, 1: 20}
d[2] = 30
print(d)

#  2. Concatenate the following dictionaries
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# Expected Result: {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
d = {}
for dic in (dic1, dic2, dic3):
    d.update(dic)
print(d)

#3. Check if a given key exists in a dictionary
d = {1: 'a', 2: 'b', 3: 'c'}
key = 2
if key in d:
    print("Key exists")
else:
    print("Key does not exist")
#4. Iterate over dictionary and print keys, values, and both
d = {1: 'apple', 2: 'banana', 3: 'cherry'}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, value)

#5. Prepare a dictionary with keys 1 to 15 and values as square
d = {}
for i in range(1, 16):
    d[i] = i ** 2
print(d)

# 6. Sum all values in a dictionary
d = {'a': 100, 'b': 200, 'c': 300}
print(sum(d.values()))


