# Stream: Python
# Tech Module: Functions/Modules/Packages
# Project: 2
# Create a Python module with the following functions:
# Function Name
# ispalindrome(name)
# count_the_vowels(name)
# frequency_of_letters(name)
# Task
# Given the user name as input, this function should
# tell us whether the name is a palindrome or not.
# Given the user name as input, this function should
# tell us how many vowels are present in it.
# Given the user name as input, this function should
# tell us how many times each letter appears in the
# name.
# Note: name will be completely in either lower case or upper case.
# Import the module in another python script and test the functions by passing
# appropriate inputs.
# Sample input 1: bob
# Sample output 1:
# Yes it is a palindrome.
# No of vowels: 1
# Frequency of letters: b-2, o-1







import name_utils

name = "bob"

print(name_utils.ispalindrome(name))
print(name_utils.count_the_vowels(name))
print(name_utils.frequency_of_letters(name))
