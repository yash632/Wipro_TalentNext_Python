# 1. Count the number of upper and lower case letters in a String
s = "Hello World"
upper = sum(1 for i in s if i.isupper())
lower = sum(1 for i in s if i.islower())
print("Uppercase:", upper)
print("Lowercase:", lower)

#2. Check whether a given String is Palindrome or not
s = "madam"
print("Palindrome" if s == s[::-1] else "Not Palindrome")

#3. Return a new string made of n copies of the first 2 chars of the original string
s = "Wipro"
n = len(s)
print(s[:2] * n)

#4. If first or last character is 'x', return string without those 'x', else return unchanged
s = "xHix"
if s.startswith('x'):
    s = s[1:]
if s.endswith('x'):
    s = s[:-1]
print(s)

#5. Given a string and an integer n, return a string made of n repetitions of the last n characters
s = "Wipro"
n = 3
print(s[-n:] * n)
