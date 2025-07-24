# Q1. Write a program to check if a given number is Positive, Negative, or Zero.
a=12
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
# Q2. Write a program to check if a given number is odd or even.
a=10
if a%2==0:
    print("even")
else:
    print("odd")
# Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) > true
# lastDigit(6, 17) > false
# lastDigit(3, 113) > true
a=12
b=2220
print("true") if a%10==b%10 else print("False")

# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.

for i in range(1,11):
    print(i)

# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a
# separate row.
for i in range(23,57,2):
    print(i+1)

# Q6. Write a program to check if a given number is prime or not.
n = int(input("Enter a number: "))
if n <= 1:
    print(n, "is not a Prime Number.")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a Prime Number.")
    else:
        print(n, "is not a Prime Number.")

# Q7. Write a program to print prime numbers between 10 and 99.
for n in range(10, 100):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n)

# Q8. Write a program to print the sum of all the digits of a given number.
# Example:
# I/P:1234
# 0/P:10/
a = 1234
sum = 0

while a > 0:
    sum += a % 10     
    a = a // 10      

print(sum)

# Q9. Write a program to reverse a given number and print.

# Example:1
# I/P: 1234
# 0/P:4321
# Example:2
# I/P:1004
# 0/P:4001
a = 1234
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

print(rev)

# Q10. Write a program to find if the given number is palindrome or not

# Example:1
# I/P:110011
# 0/P: 110011 is a palindrome.

# Example:2
# I/P:1234
# O/P: 1234 is not a palindrome. 
a = 110011
temp=a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10
print("Palindrome" if rev==temp else "Not palindrome")






