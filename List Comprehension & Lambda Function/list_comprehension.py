# 1. Write a Python program using List Comprehension to create an output dictionary which contains only the odd numbers that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values.

numbers = [1, 2, 3, 4, 5, 6, 7]

output_dict = {num: num**3 for num in numbers if num % 2 != 0}

print("Output Dictionary:", output_dict)

# 2. Make a dictionary of the 26 English alphabets mapping each with the corresponding integer using List Comprehension.


import string

alphabet_dict = {letter: index+1 for index, letter in enumerate(string.ascii_lowercase)}

print("Alphabet Dictionary:", alphabet_dict)
